from django.db import models
from uuid import uuid4

# Create your models here.

class Anime(models.Model):

    objects = None
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=100)
    ano = models.IntegerField()

