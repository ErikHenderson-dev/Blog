from rest_framework import serializers
from . import models

class CategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Categoria
        fields = '__all__'