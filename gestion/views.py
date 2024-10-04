from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Promocion, Categoria, Platillo, Galeria

# Create your views here.

def index(request):

    promotions = Promocion.objects.all()
    categorias = Categoria.objects.prefetch_related('platillo_set').all()
    galeria = Galeria.objects.all()
    context = {
        'promotions' : promotions,
        'categorias' : categorias,
        'galeria' : galeria,
    }

    return render(request, "index.html",context)

@require_http_methods(["GET"])

def obtener_platillos(request, categoria_id):
    platillos = Platillo.objects.get(id=categoria_id)
    
    platillos_list = list(platillos)
    
    return JsonResponse(platillos_list, safe=False)