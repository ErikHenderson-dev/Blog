# from django.shortcuts import render
from rest_framework import viewsets
from . import serializers
from . import models

class PostsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PostsSerializer
    queryset = models.Posts.objects.all()
