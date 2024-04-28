
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .models import Pedidos



class PedidosListView(ListView):
    model = Pedidos


class PedidosCreateView(CreateView):
    model = Pedidos
    fields = ["title", "deadline"]
    success_url = reverse_lazy("pedidos_lista")
