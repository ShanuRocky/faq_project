from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
from django.core.cache import cache
from .utils import translate_text
import logging

logger = logging.getLogger(__name__)

class FAQ(models.Model):
    question = models.TextField(_("Question"))
    answer = RichTextField(_("Answer"))

    class Meta:
        ordering = ['id']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._original_question = self.question
        self._original_answer = self.answer

    def get_translated_question(self, lang):
        if lang == 'en':
            return self.question
        
        cache_key = f'faq_{self.id}_question_{lang}'
        if cached := cache.get(cache_key):
            return cached
            
        translation = translate_text(self.question, lang)
        if translation:
            cache.set(cache_key, translation, 86400)
        return translation or self.question

    def get_translated_answer(self, lang):
        if lang == 'en':
            return self.answer
        
        cache_key = f'faq_{self.id}_answer_{lang}'
        if cached := cache.get(cache_key):
            return cached
            
        translation = translate_text(self.answer, lang)
        if translation:
            cache.set(cache_key, translation, 86400)
        return translation or self.answer

    def save(self, *args, **kwargs):
        is_new = not self.pk
        super().save(*args, **kwargs)
        
        if is_new or self.question != self._original_question:
            cache.delete_pattern(f'faq_{self.id}_question_*')
        
        if is_new or self.answer != self._original_answer:
            cache.delete_pattern(f'faq_{self.id}_answer_*')
        
        self._original_question = self.question
        self._original_answer = self.answer

    def __str__(self):
        return self.question[:50]