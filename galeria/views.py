from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #return HttpResponse('<h1>Django Space</h1><p>Bem vindo ao espaco</p>')
    return render(request, 'galeria/index.html')

def imagem(request):
    return render(request, 'galeria/imagem.html')
