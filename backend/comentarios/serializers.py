from rest_framework import serializers
from . import models

class ComentariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comentarios
        fields = '__all__'