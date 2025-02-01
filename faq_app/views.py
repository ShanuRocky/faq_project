from rest_framework import viewsets, views
from rest_framework.response import Response
from .models import FAQ
from .serializers import FAQSerializer, FAQListSerializer
from .utils import get_supported_languages  # Add this import

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        
        # Get the language from query parameters
        lang = request.query_params.get('lang', 'en')
        
        if page is not None:
            serializer = FAQListSerializer({
                'count': self.paginator.page.paginator.count,
                'next': self.paginator.get_next_link(),
                'previous': self.paginator.get_previous_link(),
                'results': page
            }, context={'request': request})
            return self.get_paginated_response(serializer.data)

        serializer = FAQListSerializer({
            'count': queryset.count(),
            'next': None,
            'previous': None,
            'results': queryset
        }, context={'request': request})
        return Response(serializer.data)

class SupportedLanguagesView(views.APIView):
    def get(self, request):
        languages = get_supported_languages()
        return Response({"supported_languages": languages})