from django.db import models

class Professor(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    valor_hora = models.DecimalField(max_digits=9, decimal_places=2, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    foto = models.URLField(max_length=255, blank=False, null=False)

class Aula(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=False)
    professor = models.ForeignKey(to=Professor, on_delete=models.CASCADE, related_name="aulas", null=False, blank=False)

class User(models.Model):
    username = models.CharField(db_index=True, max_length=255, unique=True, default="")
    email = models.EmailField(db_index=True, unique=True, null=True, blank=True, default="")
    firstname = models.CharField(max_length=150, blank=True, default="")
    lastname = models.CharField(max_length=150, blank=True, default="")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f"{self.email}"