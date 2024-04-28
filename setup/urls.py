from django.contrib import admin
from django.urls import path
from pedidos.views import PedidosListView, PedidosCreateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", PedidosListView.as_view(), name="pedidos_lista"),
    path("pedidos.novo", PedidosCreateView.as_view(), name="pedidos_novo"),
]
