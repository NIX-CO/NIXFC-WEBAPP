# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Organization
from .forms import OrganizationForm

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
