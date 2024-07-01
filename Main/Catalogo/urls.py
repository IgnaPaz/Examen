# Catalogo/urls.py

from django.urls import path
from .views import producto_list, producto_create, producto_update, producto_delete, producto_detail

urlpatterns = [
    path('', producto_list, name='producto_list'),
    path('nuevo/', producto_create, name='producto_create'),
    path('editar/<int:pk>/', producto_update, name='producto_update'),
    path('borrar/<int:pk>/', producto_delete, name='producto_delete'),
    path('<int:pk>/', producto_detail, name='producto_detail'),
]
