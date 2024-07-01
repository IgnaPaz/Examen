from django.shortcuts import render, get_object_or_404, redirect
from .models import Diseño
from .forms import DiseñoForm

def diseño_list(request):
    diseños = Diseño.objects.all()
    return render(request, 'diseño/diseño_list.html', {'diseños': diseños})

def diseño_detail(request, pk):
    diseño = get_object_or_404(Diseño, pk=pk)
    return render(request, 'diseño/diseño_detail.html', {'diseño': diseño})

def diseño_create(request):
    if request.method == 'POST':
        form = DiseñoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('diseño_list')
    else:
        form = DiseñoForm()
    return render(request, 'diseño/diseño_form.html', {'form': form})

def diseño_update(request, pk):
    diseño = get_object_or_404(Diseño, pk=pk)
    if request.method == 'POST':
        form = DiseñoForm(request.POST, request.FILES, instance=diseño)
        if form.is_valid():
            form.save()
            return redirect('diseño_list')
    else:
        form = DiseñoForm(instance=diseño)
    return render(request, 'diseño/diseño_form.html', {'form': form})

def diseño_delete(request, pk):
    diseño = get_object_or_404(Diseño, pk=pk)
    if request.method == 'POST':
        diseño.delete()
        return redirect('diseño_list')
    return render(request, 'diseño/diseño_confirm_delete.html', {'diseño': diseño})
