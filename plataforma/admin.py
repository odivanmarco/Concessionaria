from django.contrib import admin
from plataforma.models import Cidade, Veiculo, Imagem

# Register your models here.
admin.site.register(Imagem)
admin.site.register(Veiculo)
admin.site.register(Cidade)
