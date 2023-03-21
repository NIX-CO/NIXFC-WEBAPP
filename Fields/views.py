from django.shortcuts import render
from .models import Field
# Create your views here.

def field_list(request):
    fields = Field.objects.all()
    return render(request, 'showFields.html', {'fields': fields})
