# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Organization
from .forms import OrganizationForm
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import OrganizationSerializer

def organization_list(request):
    organizations = Organization.objects.all()
    return render(request, 'organization_list.html', {'organizations': organizations})

def organization_create(request):
    form = OrganizationForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('organization_list')
    return render(request, 'organization_form.html', {'form': form})

def organization_update(request, pk):
    organization = get_object_or_404(Organization, id=pk)
    form = OrganizationForm(request.POST or None, request.FILES or None, instance=organization)
    if form.is_valid():
        form.save()
        return redirect('organization_list')
    return render(request, 'organization_form.html', {'form': form})

def organization_delete(request, pk):
    organization = get_object_or_404(Organization, id=pk)
    if request.method == 'POST':
        organization.delete()
        return redirect('organization_list')
    return render(request, 'organization_confirm_delete.html', {'organization': organization})

def organization_detail(request, pk):
    organization = get_object_or_404(Organization, id=pk)
    return render(request, 'organization_details.html', {'organization': organization})


@api_view(['GET'])
def organization_list(request):
    organizations = Organization.objects.all()
    serializer = OrganizationSerializer(organizations, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def organization_create(request):
    serializer = OrganizationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def organization_update(request, pk):
    organization = get_object_or_404(Organization, id=pk)
    serializer = OrganizationSerializer(instance=organization, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def organization_delete(request, pk):
    organization = get_object_or_404(Organization, id=pk)
    organization.delete()
    return Response(status=204)

@api_view(['GET'])
def organization_detail(request, pk):
    organization = get_object_or_404(Organization, id=pk)
    serializer = OrganizationSerializer(organization)
    return Response(serializer.data)
