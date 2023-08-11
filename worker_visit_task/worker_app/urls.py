from django.urls import path
from . import views

urlpatterns = [
    path('units/<int:worker_id>/', views.GetUnitsAPIView.as_view(), name='units-list'),
    path('visits/create/', views.CreateVisitAPIView.as_view(), name='visits'),
]