from django.db import models
from accounts.models import User
class Buildings (models.Model):

    matricula = models.IntegerField(null=False, unique=True)
    tamanho = models.IntegerField(null=False)
    endereco = models.CharField(max_length=255, null=False)
    bairro = models.CharField(max_length=255, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="buildings")