from django.shortcuts import render
from .models import Projeto

# Create your views here.
def inicio(request):
    projetos = Projeto.objects.all()
    contexto = {"projetos": projetos}
    return render(request,"projetos/inicio.html", contexto)

def detalhe(request, pk):
    projeto = Projeto.objects.filter(id=pk).first()
    contexto={"projeto": projeto}
    return render(request,"projetos/detalhe.html", contexto)