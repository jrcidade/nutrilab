from django.shortcuts import render


def cadastro(request):
    return render(request, 'cadastro.html')

def logar(request):
    return render(request, 'logar.html')


