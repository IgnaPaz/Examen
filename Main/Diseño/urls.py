from django.urls import path
from . import views

urlpatterns = [
    path('', views.diseño_list, name='diseño_list'),
    path('diseño/<int:pk>/', views.diseño_detail, name='diseño_detail'),
    path('diseño/new/', views.diseño_create, name='diseño_create'),
    path('diseño/<int:pk>/edit/', views.diseño_update, name='diseño_update'),
    path('diseño/<int:pk>/delete/', views.diseño_delete, name='diseño_delete'),
]
