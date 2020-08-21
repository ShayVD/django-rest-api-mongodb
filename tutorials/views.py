from django.shortcuts import render

from rest_framework import viewsets, renderers
from rest_framework.response import Response

from tutorials.models import Tutorial
from tutorials.serializers import TutorialSerializer
from rest_framework.decorators import action

# Create your views here.

class TutorialsViewSet(viewsets.ModelViewSet):
    queryset = Tutorial.objects.all()
    serializer_class = TutorialSerializer

    def list(self, request, *args, **kwargs):
        title = request.GET.get('title', None)
        if title:
            tutorials = self.queryset.filter(title__icontains=title)
            serializer = self.serializer_class(tutorials, many=True)
            return Response(serializer.data)  
        super().list(request, *args, **kwargs)

    @action(detail=False)
    def published(self, request, *args, **kwargs):
        published = self.queryset.filter(published=True)
        serializer = self.serializer_class(published, many=True)
        return Response(serializer.data)
