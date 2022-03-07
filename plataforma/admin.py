from django.contrib import admin
from .models import DiasVisita,Imagem,Imovei,Cidade,Visitas,Horario

# Register your models here.
@admin.register(Imovei)
class ImoveiAdmin(admin.ModelAdmin):
    list_display = ('rua', 'valor', 'quartos', 'tamanho', 'cidade', 'tipo')
    list_editable = ('valor', 'tipo')
    list_filter = ('cidade', 'tipo')

admin.site.register(DiasVisita)
admin.site.register(Cidade)
admin.site.register(Visitas)
admin.site.register(Imagem)
admin.site.register(Horario)