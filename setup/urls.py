from django.contrib import admin
from django.urls import path
from pedidos.views import pedidos_list

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", pedidos_list),
]
