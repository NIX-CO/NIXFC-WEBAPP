from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .forms import FieldForm
from .models import Field

def create_field(request):
    if request.method == 'POST':
        form = FieldForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = FieldForm()
    return render(request, 'create_field.html', {'form': form})

@require_POST
def delete_field(request, field_id):
    field = Field.objects.get(pk=field_id)
    field.delete()
    return redirect('/')