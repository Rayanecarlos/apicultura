

from django.shortcuts import render



def login(request):
    return render(request, 'login.html')

def cadastro(request):
  return render(request, 'cadastro.html')

def menu (request):
          return render (request, 'menu.html')