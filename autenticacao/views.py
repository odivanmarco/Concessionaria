from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib import auth

# Create your views here.

def register(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'register.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if len(username.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0:
            messages.add_message(request,constants.ERROR,'Preencha os campos corretamente')
            return redirect('/auth/register')

        user = User.objects.filter(username=username)
        print(user)

        if user.exists():
            messages.add_message(request,constants.ERROR,'Já existe usuário com esse username')
            return redirect('/auth/register')


        try:
            user = User.objects.create_user(username=username, email=email,password=senha)
            user.save()
            messages.add_message(request,constants.SUCCESS,'Cadastro realizado com sucesso')
            return redirect('/auth/login')
        except:
            messages.add_message(request,constants.ERROR,'Erro intero no sistema, tente novamente mais tarde')
            return redirect('/auth/register')

        return HttpResponse(f'{username} {email} {senha}')
        


def login(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')

    usuario = auth.authenticate(username=username, password=senha)
    if not usuario:
        messages.add_message(request, constants.ERROR, 'Usuário ou senha invalidos')
        return redirect('/auth/login')
    else: 
        auth.login(request, usuario)
        return redirect('/')

def logout(request):
    auth.logout(request)
    return redirect('/auth/login')