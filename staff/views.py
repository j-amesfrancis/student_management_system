from django.shortcuts import render, redirect

from accounts.models import *
from hod.models import *
from staff.models import *


# Create your views here.


def staff_dashboard(request):
    return redirect('staff-students')


def staff_student(request):
    student = Student.objects.all()
    student_leave = StudentLeave.objects.all()
    student_attendance = StudentAttendance.objects.all()
    context = {
        'student': student,
        'student_leave': student_leave,
        'student_attendance': student_attendance,
    }
    return render(request, 'staff_dashboard_student.html', context)


def staff_guardian(request):
    guardian = Guardian.objects.all()
    context = {
        'guardian': guardian
    }
    return render(request, 'staff_dashboard_guardian.html', context)


def total_students(request):
    student_list = Student.objects.all()

    context = {
        'student_list': student_list,
    }
    return render(request, 'staff_dashboard_total_students.html', context)


def add_student(request):
    return render(request, 'staff_dashboard_add_students.html')
