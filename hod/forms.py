from django import forms
from django.contrib.auth.forms import UserCreationForm
from staff.models import *
from student.models import *


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'user_roles']


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'


class HodStaffUpdateForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'
        exclude = ['email', 'user']
