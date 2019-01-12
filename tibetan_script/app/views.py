from django.shortcuts import render

# Create your views here.

def index(r):
    c = {}
    return render(r, 'app/index.html', c)
