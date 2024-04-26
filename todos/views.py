from django.shortcuts import render
from .models import Pedidos


def todo_list(request):
    pedidos = Pedidos.objects.all()
    return render(request, "todos/todos_lista.html", {"pedidos": pedidos})
 