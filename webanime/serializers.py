from rest_framework import serializers
from webanime import models

class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Anime
        fields = '__all__'
