from django.urls import path

from hod import views

urlpatterns = [
    path('', views.hod_home, name='hod-dashboard'),
    path('staff/', views.hod_staff, name='hod-staff'),
    path('add-staff/', views.add_staff, name='add-staff'),
    path('staff-details/', views.staff_details, name='staff-details'),
    path('staff-update/<str:pk>', views.staff_update, name='staff-update'),
    path('staff-delete/<str:pk>', views.delete_staff, name='staff-delete'),
    path('student/', views.hod_student, name='hod-student'),
    path('courses/', views.hod_courses, name='hod-courses'),
    path('subjects/', views.hod_subjects, name='hod-subjects'),
    path('add-subject/', views.add_subject, name='add-subject'),
    path('add-course/', views.add_course, name='add-course'),
    path('delete-course/<str:pk>/', views.delete_course, name='delete-course'),
    path('update-course/<str:pk>/', views.update_course, name='update-course'),
    path('delete-subject/<str:pk>/', views.delete_subject, name='delete-subject'),
    path('update-subject/<str:pk>/', views.update_subject, name='update-subject'),
]
