from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from faq_app.views import FAQViewSet, SupportedLanguagesView

router = DefaultRouter()
router.register(r'faqs', FAQViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include(router.urls)),
    path('api/supported-languages/', SupportedLanguagesView.as_view(),
    name='supported-languages'),
]
