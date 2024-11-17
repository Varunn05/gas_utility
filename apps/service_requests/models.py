from django.db import models
from django.conf import settings

class ServiceRequestCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class ServiceRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed'),
    ]
    REQUEST_TYPES = [
        ('gas_leak', 'Gas Leak'),
        ('connection_issue', 'Connection Issue'),
        ('billing_query', 'Billing Query'),
        ('maintenance', 'Maintenance'),
        ('new_connection', 'New Connection'),
    ]
    
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(ServiceRequestCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    attachment = models.FileField(upload_to='service_requests/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    priority = models.IntegerField(default=3)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_requests'
    )
    
    def __str__(self):
        return f"{self.request_type} - {self.customer.username} - {self.status}"

class RequestUpdate(models.Model):
    service_request = models.ForeignKey(ServiceRequest, on_delete=models.CASCADE)
    comment = models.TextField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Update for {self.service_request} at {self.created_at}"