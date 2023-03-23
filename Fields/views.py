from django.shortcuts import render,get_object_or_404, redirect
from .models import Field
from .forms import FieldForm
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