from django.contrib import admin
from .models import Diseño

@admin.register(Diseño)
class DiseñoAdmin(admin.ModelAdmin):
    list_display = ('diseñador', 'diseño', 'descripcion')
