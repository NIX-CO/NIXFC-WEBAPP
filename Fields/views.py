from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.http import require_POST
from .forms import FieldForm,FieldDeleteForm
from .models import Field
# Create your views here.

def field_list(request):
    fields = Field.objects.all()
    return render(request, 'showFields.html', {'fields': fields})

def field_update(request, pk):
    field = get_object_or_404(Field, pk=pk)
    if request.method == 'POST':
        form = FieldForm(request.POST, request.FILES, instance=field)
        if form.is_valid():
            form.save()
            return redirect('field_detail', pk=field.pk)
    else:
        form = FieldForm(instance=field)
    return render(request, 'updateFields.html', {'form': form})
    
def create_field(request):
    if request.method == 'POST':
        form = FieldForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = FieldForm()
    return render(request, 'createField.html', {'form': form})

def delete_field(request):
    if request.method == 'POST':
        form = FieldDeleteForm(request.POST)
        if form.is_valid():
            field_id = form.cleaned_data['field_id']
            field = get_object_or_404(Field, pk=field_id)
            field.delete()
            return redirect('home')
    else:
        form = FieldDeleteForm()
    return render(request, 'deleteField.html', {'form': form})
      