from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Veiculo(models.Model):
    choices_combustivel = (('G','Gasolina'),
                                            ('A','Alcool'),
                                            ('D','Diesel'),
                                            ('E', 'Eletrico'), 
                                            ('F','Flex'))

    imagem1 = models.FileField(upload_to='img')
    imagem2 = models.ImageField(upload_to='img')
    imagem3 = models.ImageField(upload_to='img')
    valor = models.FloatField()
    modelo = models.CharField(max_length=30)
    kmRodados = models.IntegerField()
    ano = models.PositiveIntegerField()
    cor = models.CharField(max_length=30)
    tipo_combustivel = models.CharField(choices=choices_combustivel, max_length=1)
    descricao = models.TextField(max_length=255)
    cidade = models.CharField(max_length=60)
    bairro = models.CharField(max_length=60)
    rua = models.CharField(max_length=60)

