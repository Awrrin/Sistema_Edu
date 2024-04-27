from django.shortcuts import render
from .models import Pedidos


def pedidos_list(request):
    pedidos = Pedidos.objects.all()
    return render(request, "pedidos/pedidos_lista.html", {"pedidos": pedidos})
 