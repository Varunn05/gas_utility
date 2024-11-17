from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from apps.service_requests.models import ServiceRequest, RequestUpdate
from .forms import RequestUpdateForm

def is_support_staff(user):
    return user.is_staff

@login_required
@user_passes_test(is_support_staff)
def support_dashboard(request):
    pending_requests = ServiceRequest.objects.filter(status='pending')
    in_progress_requests = ServiceRequest.objects.filter(status='in_progress')
    
    return render(request, 'customer_support/dashboard.html', {
        'pending_requests': pending_requests,
        'in_progress_requests': in_progress_requests
    })

@login_required
@user_passes_test(is_support_staff)
def update_request(request, pk):
    service_request = get_object_or_404(ServiceRequest, pk=pk)
    
    if request.method == 'POST':
        form = RequestUpdateForm(request.POST)
        if form.is_valid():
            update = form.save(commit=False)
            update.service_request = service_request
            update.created_by = request.user
            update.save()
            
            # Update service request status
            service_request.status = form.cleaned_data['new_status']
            service_request.save()
            
            messages.success(request, 'Request updated successfully!')
            return redirect('customer_support:dashboard')
    else:
        form = RequestUpdateForm()
    
    return render(request, 'customer_support/update_request.html', {
        'form': form,
        'service_request': service_request
    })