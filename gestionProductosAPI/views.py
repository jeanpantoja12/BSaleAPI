import json
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Product,Category


# API's
#------------------------

# API de búsqueda de productos
# Recibe parámetros: order (orden),from_s (precio desde),to_s (precio hasta)

def search_api(request):
    # Parámetros
    # Palabra de búsqueda
    product = request.GET.get('s','')
    #Instancia de parámetro URL de Orden de la lista (ascendente o descendente) 
    order = request.GET.get('order',None)
    # Instancia de parámetro URL de "Precios desde"
    from_search = request.GET.get('from_s',None)
    # Instancia de parámetro URL de "Precios hasta"
    to_search = request.GET.get('to_s',None)

    # Validación de parámetros de filtro de precios y búsqueda en la base de datos
    if from_search and to_search:
        queryset = (Q(name__icontains=product,price__gte=from_search,price__lte=to_search))
    else:
        if from_search:
            queryset = (Q(name__icontains=product,price__gte=from_search))
        elif to_search:
            queryset = (Q(name__icontains=product,price__lte=to_search))
        else:
            queryset = (Q(name__icontains=product))

    # Validación del orden de la lista
    if order is not None:
        if order == 'asc':
            result = Product.objects.filter(queryset).order_by('price')
        elif order == 'desc':
            result = Product.objects.filter(queryset).order_by('-price')

    # Lista por defecto
    else:
        result = Product.objects.filter(queryset).order_by('-price')

    # Paginación de la lista
    paginator = Paginator(result, 10)
    actual_page = request.GET.get('page',1)
    page = paginator.get_page(actual_page)

    return JsonResponse({
        "results": [result.serialize() for result in page],
        "num_pages": paginator.num_pages,
        "has_next": page.has_next(),
        "has_prev": page.has_previous(),
    })

#------------------------

# API de obtención de todas las categorías
# No recibe parámetros

def categories_api(request):
    # Búsqueda de categorías en la base de datos
    categories = Category.objects.all()
    
    return JsonResponse({
        "categories": [category.serialize() for category in categories]     
    })

#------------------------

# API de búsqueda por categorías
# Recibe parámetros: cat (categoría), num (paginación) y order (orden)

def categorysearch_api(request,cat,num):
    # Validación de existencia de categoría
    try:
        category = Category.objects.get(name=cat)
    except Category.DoesNotExist:
        return JsonResponse({"error": "Categoria no encontrada."}, status=404)

    # Orden de la lista (ascendente o descendente) 
    order = request.GET.get('order', None)

    # Validación del orden de la lista
    if order is not None:
        if order == 'asc':
            results = Product.objects.filter(category=category).order_by('price')
        elif order == 'desc':
            results = Product.objects.filter(category=category).order_by('-price')
    else:
        results = Product.objects.filter(category=category).order_by('-price')

    # Paginación de la lista
    paginator = Paginator(results, 8)
    page = paginator.get_page(num)
    return JsonResponse({
        "results": [result.serialize() for result in page],
        "has_next": page.has_next()
    })

#------------------------