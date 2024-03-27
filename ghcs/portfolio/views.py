from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. Este é o meu primeiro projeto Django! Chamado Portfolio.")

# Path: ghcs/portfolio/urls.py
