from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def bah_tche(request):
  # Buscar dados de base
  # Manipular dados
  # Mandar emails...
  return render(request, 'index.html')#HttpResponse('bao')