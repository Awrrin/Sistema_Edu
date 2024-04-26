from django.shortcuts import render
from .models import Todo


def todo_list(request):
    pedidos = Todo.objects.all()
    return render(request, "todos/todo_list.html", {"pedidos": pedidos})
 