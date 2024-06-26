from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/anexo')   
    
    if request.method == 'GET':
        return render(request, 'login/login.html')
    
    elif request.method == 'POST':
        nome = request.POST.get('usuario')
        senha = request.POST.get('senha')

        user = authenticate(username=nome,
                            password=senha)
        if user is not None:
            login(request, user)
            return render(request, 'anexo/anexo.html', { 'user': user })    
        else:
            return render(request, 'login/login.html')

def logout_view(request):
    logout(request)
    return redirect('/')

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        email_parceiro = request.POST.get('email_parceiro')
        integrador = request.POST.get('integrador')


    return render(request, 'cadastro/cadastro.html')

@login_required
def anexo(request):
    return render(request, 'anexo/anexo.html')
