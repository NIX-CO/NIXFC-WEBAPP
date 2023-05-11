from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.http import require_POST
from .forms import FieldForm,FieldDeleteForm
from .models import Field
from reservation.models import Reservation
from .serializers import FieldSerializer
from rest_framework import generics
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

def field_list(request):
    fields = Field.objects.all()
    return render(request, 'showFields.html', {'fields': fields})

@api_view(['GET'])
def FieldList(request):
    fields = Field.objects.all()
    serializer =FieldSerializer(fields,many=True)
    return Response(serializer.data)

def field_update(request, pk):
    field = get_object_or_404(Field, pk=pk)
    if request.method == 'POST':
        form = FieldForm(request.POST, request.FILES, instance=field)
        if form.is_valid():
            form.save()
            return redirect('/', pk=field.pk)
    else:
        form = FieldForm(instance=field)
    return render(request, 'updateFields.html', {'form': form})
    
def create_field(request):
    if request.method == 'POST':
        form = FieldForm(request.POST, request.FILES)
        if form.is_valid():
            field = form.save(commit=False)
            field.save()
            messages.success(request, 'Field created successfully!')
            return redirect('field_list')
        else:
            messages.error(request, 'Error creating field.')
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
            return redirect('/')
    else:
        form = FieldDeleteForm()
    return render(request, 'deleteField.html', {'form': form})

def field_detail(request, pk):
    field = get_object_or_404(Field, pk=pk)
    return render(request, 'showFieldDetails.html', {'field': field})

######search


def search(request):
    if request.method == 'POST':
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        reservations = Reservation.objects.filter(start_time__lte=end_time, end_time__gte=start_time)
        fields = Field.objects.exclude(id__in=reservations.values_list('field_id', flat=True))
        return render(request, 'showFields.html', {'fields': fields})
    else:
        messages.success(request, 'there is no available fields!')
def show_reserved_fields(request):
    reservations = Reservation.objects.all()
    fields = Field.objects.filter(id__in=reservations.values_list('field_id', flat=True))
    # return render(request, 'search_results.html', {'fields': fields})
    return render(request, 'showFields.html', {'fields': fields})
