# from django.shortcuts import render
from rest_framework import viewsets
from . import serializers
from . import models

class ComentariosViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ComentariosSerializer
    queryset = models.Comentario.objects.all()
