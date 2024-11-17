from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import ServiceRequest
from .forms import ServiceRequestForm

@login_required
def create_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user
            service_request.save()
            messages.success(request, 'Service request created successfully!')
            return redirect('service_requests:list')
    else:
        form = ServiceRequestForm()
    
    return render(request, 'service_requests/create.html', {'form': form})

@login_required
def service_request_list(request):
    service_requests = ServiceRequest.objects.filter(customer=request.user)
    return render(request, 'service_requests/list.html', {
        'service_requests': service_requests
    })

@login_required
def service_request_detail(request, pk):
    service_request = get_object_or_404(ServiceRequest, pk=pk, customer=request.user)
    return render(request, 'service_requests/detail.html', {
        'service_request': service_request
    })