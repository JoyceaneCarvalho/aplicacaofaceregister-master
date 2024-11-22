from rest_framework import serializers
from appfaceregister import models

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
            model = models.Aluno
            fields = '__all__'

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Professor
        fields = '__all__'  # Inclui todos os campos do modelo Professor
