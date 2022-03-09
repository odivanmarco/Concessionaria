from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Imagem(models.Model):
    img = models.ImageField(upload_to='img')

    def __str__(self ) -> str:
        return self.img.url

class Cidade(models.Model):
    nome = models.CharField(max_length=60)

    def __str__(self) -> str:
        return self.nome

class Veiculo(models.Model):
    choices_combustivel = (('G','Gasolina'),
                                            ('A','Alcool'),
                                            ('D','Diesel'),
                                            ('E', 'Eletrico'), 
                                            ('F','Flex'))

    imagens = models.ManyToManyField(Imagem)
    valor = models.FloatField()
    modelo = models.CharField(max_length=30)
    kmRodados = models.IntegerField()
    ano = models.PositiveIntegerField()
    cor = models.CharField(max_length=30)
    tipo_combustivel = models.CharField(choices=choices_combustivel, max_length=1)
    descricao = models.TextField(max_length=255)
    cidade = models.ForeignKey(Cidade, on_delete=models.DO_NOTHING)
    bairro = models.CharField(max_length=60)
    rua = models.CharField(max_length=60)