from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from webanime import serializers
from webanime import models

class AnimeViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AnimeSerializer
    queryset = models.Anime.objects.all()

