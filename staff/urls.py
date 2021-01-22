from django.urls import path

from . import views

urlpatterns = [
    path('', views.staff_dashboard, name='staff-dashboard'),
    path('students/', views.staff_student, name='staff-students'),
    path('add-student/', views.add_student, name='add-student'),
    path('guardian/', views.staff_guardian, name='staff-guardian'),
    path('total-students/', views.total_students, name='total-students'),
]
