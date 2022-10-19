from django.forms import ValidationError
from rest_framework import serializers
from teacher.models import Professor, Aula, User

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'

class CadastrarAulaSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    nome = serializers.CharField(max_length=100)

    def validate_nome(self, value):
        if len(value) < 3:
            raise ValidationError("Deve ter pelo menos três caracteres")
        return value 


class AulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aula
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance