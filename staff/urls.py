from django.urls import path

from . import views

urlpatterns = [
    path('', views.staff_dashboard, name='staff-dashboard'),
    path('students/', views.staff_student, name='staff-students'),
    path('guardian/', views.staff_guardian, name='staff-guardian'),
]
