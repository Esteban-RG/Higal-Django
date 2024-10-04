from django.shortcuts import render
from .models import Promocion, Categoria

# Create your views here.

def index(request):

    promotions = Promocion.objects.all()
    categorias = Categoria.objects.all()
    
    context = {
        'promotions' : promotions,
        'categorias' : categorias,
    }

    return render(request, "base.html",context)