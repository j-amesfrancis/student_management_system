from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import *
from .forms import *
from accounts.decorators import user_redirect


# Create your views here.


@login_required(login_url='login')
@user_redirect
def hod_home(request):
    course = Course.objects.all()
    context = {'course': course}
    return render(request, 'hod_dashboard.html', context)


@login_required(login_url='login')
@user_redirect
def hod_staff(request):
    staff = Staff.objects.all()
    staff_leave = StaffLeave.objects.all()
    staff_attendance = StaffAttendance.objects.all()
    context = {'staff': staff, 'staff_leave': staff_leave,
               'staff_attendance': staff_attendance}
    return render(request, 'hod_dashboard_staff.html', context)


@login_required(login_url='login')
@user_redirect
def hod_student(request):
    student = Student.objects.all()
    student_leave = StudentLeave.objects.all()
    student_attendance = StudentAttendance.objects.all()
    context = {'student': student, 'student_leave': student_leave,
               'student_attendance': student_attendance}
    return render(request, 'hod_dashboard_student.html', context)


@login_required(login_url='login')
@user_redirect
def hod_courses(request):
    course = Course.objects.all()
    context = {'course': course}
    return render(request, 'hod_dashboard_course.html', context)


@login_required(login_url='login')
@user_redirect
def hod_subjects(request):
    subject = Subject.objects.all()
    context = {'subject': subject}
    return render(request, 'hod_dashboard_subject.html', context)


@login_required(login_url='login')
@user_redirect
def add_subject(request):
    subject_form = SubjectForm()
    if request.method == 'POST':
        subject_form = SubjectForm(request.POST)
        if subject_form.is_valid():
            subject_form.save()
            return redirect('hod-subjects')
    context = {'subject_form': subject_form}
    return render(request, 'hod_dashboard_add_subject.html', context)


@login_required(login_url='login')
@user_redirect
def add_course(request):
    course_form = CourseForm()
    if request.method == 'POST':
        course_form = CourseForm(request.POST)
        if course_form.is_valid():
            course_form.save()
            return redirect('hod-courses')
    context = {'course_form': course_form}
    return render(request, 'hod_dashboard_add_course.html', context)


@login_required(login_url='login')
@user_redirect
def delete_course(request, pk):
    course = Course.objects.get(id=pk)
    course.delete()
    return redirect('hod-courses')


@login_required(login_url='login')
@user_redirect
def update_course(request, pk):
    course_instance = Course.objects.get(id=pk)
    if request.method == 'POST':
        course_form = CourseForm(request.POST, instance=course_instance)
        if course_form.is_valid():
            course_form.save()
            return redirect('hod-courses')
    context = {'course_instance': course_instance}
    return render(request, 'hod_dashboard_add_course.html', context)


@login_required(login_url='login')
@user_redirect
def delete_subject(request, pk):
    subject = Subject.objects.get(id=pk)
    subject.delete()
    return redirect('hod-subjects')


@login_required(login_url='login')
@user_redirect
def update_subject(request, pk):
    subject_instance = Subject.objects.get(id=pk)
    if request.method == 'POST':
        subject_form = SubjectForm(request.POST, instance=subject_instance)
        if subject_form.is_valid():
            subject_form.save()
            return redirect('hod-subjects')
    context = {'subject_instance': subject_instance}
    return render(request, 'hod_dashboard_add_subject.html', context)


@login_required(login_url='login')
@user_redirect
def staff_details(request):
    staff_list = Staff.objects.all()
    context = {'staff_list': staff_list}
    return render(request, 'hod_dashboard_staff_details.html', context)


@login_required(login_url='login')
@user_redirect
def staff_update(request, pk):
    staff_instance = Staff.objects.get(id=pk)
    staff_form = HodStaffUpdateForm(instance=staff_instance)
    subject = Subject.objects.all()
    if request.method == 'POST':
        staff_form = HodStaffUpdateForm(request.POST, request.FILES, instance=staff_instance)
        if staff_form.is_valid():
            staff_form.save()
            return redirect('staff-details')
    context = {'staff_form': staff_form, 'subject': subject, 'staff_instance': staff_instance}
    return render(request, 'hod_dashboard_staff_update.html', context)


@login_required(login_url='login')
@user_redirect
def add_staff(request):
    staff_form = UserForm()
    if request.method == 'POST':
        staff_form = UserForm(request.POST)
        if staff_form.is_valid():
            staff_form.save()
            return redirect('staff-details')
    context = {'staff_form': staff_form}
    return render(request, 'hod_dashboard_add_staff.html', context)


@login_required(login_url='login')
@user_redirect
def delete_staff(request, pk):
    staff = Staff.objects.get(id=pk)
    staff.delete()
    return redirect('staff-details')
