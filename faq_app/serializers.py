from rest_framework import serializers
from .models import FAQ
from .utils import get_supported_languages

class FAQSerializer(serializers.ModelSerializer):
    question = serializers.CharField(
        style={'base_template': 'textarea.html', 'rows': 4, 'placeholder': 'Enter question here'}
    )
    translated_question = serializers.SerializerMethodField()
    answer = serializers.CharField(style={'base_template': 'textarea.html', 'rows': 6})
    translated_answer = serializers.SerializerMethodField()

    class Meta:
        model = FAQ
        fields = ['id', 'question', 'translated_question', 'answer', 'translated_answer']

    def get_translated_question(self, obj):
        lang = self.context['request'].query_params.get('lang', 'en')
        return obj.get_translated_question(lang)

    def get_translated_answer(self, obj):
        lang = self.context['request'].query_params.get('lang', 'en')
        return obj.get_translated_answer(lang)

class FAQListSerializer(serializers.Serializer):
    count = serializers.IntegerField()
    next = serializers.URLField(allow_null=True)
    previous = serializers.URLField(allow_null=True)
    results = serializers.SerializerMethodField()
    available_languages = serializers.ListField(child=serializers.CharField(), read_only=True)

    def get_results(self, obj):
        return FAQSerializer(obj['results'], many=True, context=self.context).data

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['available_languages'] = get_supported_languages()
        return data