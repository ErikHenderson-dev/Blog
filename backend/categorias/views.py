# from django.shortcuts import render
from rest_framework import viewsets
from . import serializers
from . import models

class CategoriasViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CategoriasSerializer
    queryset = models.Categorias.objects.all()
