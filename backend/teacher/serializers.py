from django.forms import ValidationError
from rest_framework import serializers
from teacher.models import Professor, Aula

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
    class User(AbstractUser):
        username = models.CharField(db_index=True, max_length=255, unique=True, default="")
        email = models.EmailField(db_index=True, unique=True, null=True, blank=True, default="")
        firstname = models.CharField(max_length=150, blank=True, default="")
        lastname = models.CharField(max_length=150, blank=True, default="")
        is_active = models.BooleanField(default=True)
        is_staff = models.BooleanField(default=False)
        created = models.DateTimeField(default=now)
        updated = models.DateTimeField(auto_now=True)

        USERNAME_FIELD = 'email'
        REQUIRED_FIELDS = ['username']

        def __str__(self):
            return f"{self.email}"