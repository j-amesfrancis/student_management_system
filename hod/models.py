import uuid
from django.db import models
from django.utils import timezone

from accounts.models import User


# Create your models here.


class Hod(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to='hod', default='user.svg')

    def __str__(self):
        if self.first_name and self.last_name:
            return str(self.first_name + ' ' + self.last_name)
        return self.email


class Subject(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return str(self.name)


class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    code_name = models.CharField(max_length=10, unique=True)
    date_created = models.DateTimeField(default=timezone.now, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Category(models.Model):
    name = models.CharField(max_length=200)


class Asset(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)


class State(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return str(self.name)


class Student(models.Model):
    GENDER = (
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    address = models.TextField()
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    mobile_number = models.PositiveBigIntegerField(unique=True)
    pin_code = models.PositiveIntegerField()
    aadhar_card_number = models.PositiveBigIntegerField(unique=True, null=True, blank=True)
    token_no = models.CharField(max_length=15, unique=True)
    course_name = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    gender = models.CharField(max_length=10, choices=GENDER, default='MALE')
    date_of_birth = models.DateField()
    session_start_date = models.DateField()
    session_end_date = models.DateField()
    profile_pic = models.ImageField(null=True, blank=True,
                                    upload_to='student', default='user.svg')

    def __str__(self):
        if self.first_name and self.last_name:
            return str(self.first_name + ' ' + self.last_name)
        return self.email


class StudentLeave(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    leave_subject = models.CharField(max_length=255)
    leave_message = models.TextField()
    leave_date = models.DateField()

    def __str__(self):
        return str(self.student) + ", " + self.leave_subject
