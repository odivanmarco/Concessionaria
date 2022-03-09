from multiprocessing import context
from operator import mod
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from plataforma.forms import VeiculoForm

from plataforma.models import Cidade, Veiculo


# Create your views here.
@login_required(login_url='/auth/logar/')
def home(request):
    preco_minimo = request.GET.get('preco_minimo')
    preco_maximo = request.GET.get('preco_maximo')
    cidade = request.GET.get('cidade')
    cidades = Cidade.objects.all()
    if preco_minimo or preco_maximo or cidade:
        
        if not preco_minimo:
            preco_minimo = 0
        if not preco_maximo:
            preco_maximo = 999999999

        veiculos = Veiculo.objects.filter(valor__gte=preco_minimo)\
        .filter(valor__lte=preco_maximo)\
        .filter(cidade=cidade)
    else:
        veiculos = Veiculo.objects.all()
    
    return render(request, 'home.html', {'veiculos': veiculos, 'cidades': cidades})
    
def contato(request):
    return render(request,'contato.html')

def sobre(request):
    return render(request,'sobre.html')

def veiculo(request, id):
    veiculo = get_object_or_404(Veiculo, id=id)
    sugestoes = Veiculo.objects.filter(cidade=veiculo.cidade).exclude(id=id)[:2]
    return render(request, 'veiculo.html', {'veiculo': veiculo, 'sugestoes': sugestoes, 'id': id})


def anuncie(request):
    if request.method=="GET":
        cidades = Cidade.objects.all()
        return render(request, 'anuncie.html', {'cidades': cidades})
    else:
        cidades = Cidade.objects.all()
        contact = Veiculo
        modelo = request.POST.get('name')
        valor = request.POST.get('emailC')
        kmRodados = request.POST.get('kmRodados')
        ano = request.POST.get('ano')
        cor = request.POST.get('cor')
        tipo_combustivel = request.POST.getlist('tipo_combustivel')
        cidade = request.POST.getlist('cidade')
        telefone = request.POST.get('telefone')
        descricao = request.POST.get('descricao')

        contact.modelo = modelo
        contact.valor = valor
        contact.kmRodados = kmRodados
        contact.ano = ano
        contact.cor = cor
        contact.tipo_combustivel = tipo_combustivel
        contact.cidade = cidade
        contact.telefone = telefone
        contact.mensagem = descricao
        contact.save()
        return render(request,'anuncie.html', {'cidades': cidades})