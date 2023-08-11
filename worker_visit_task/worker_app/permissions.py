from rest_framework import permissions
from .models import Unit, Worker 
from django.shortcuts import get_object_or_404

class IsWorker(permissions.BasePermission):
    """
    Custom permission to only allow workers to access their data.
    """
    def has_permission(self, request, view):
        # Read permissions are allowed to any worker,
        worker = Worker.objects.filter(
            id=view.kwargs['worker_id'],
            phone_number=request.GET.get('phone_number')
        ).first()
        return True if worker else False
    

class IsValidVisit(permissions.BasePermission):
    """
    Custom permission to only allow workers to access their data.
    """
    def has_permission(self, request, view):
        # This permission is to check given phone number linked with unit worker
        unit = Unit.objects.filter(
            id=request.data.get('unit'),
            worker__phone_number=request.GET.get('phone_number')
        ).first()
        return True if unit else False