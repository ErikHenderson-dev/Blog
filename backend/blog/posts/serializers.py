from rest_framework import serializers
from . import models

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = '__all__'