from django.db import models
import uuid
from django.utils import timezone

from accounts.models import User
from hod.models import Subject
from hod.models import Student


# Create your models here.
class Staff(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to='staff', default='user.svg')
    class_coordinator = models.BooleanField(default=False)

    def __str__(self):
        if self.first_name and self.last_name:
            return str(self.first_name + ' ' + self.last_name)
        return self.email

    def is_class_coordinator(self):
        return self.class_coordinator

    def get_full_name(self):
        if self.first_name and self.last_name:
            return str(self.first_name + ' ' + self.last_name)
        return self.email


class Guardian(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.OneToOneField(Student, on_delete=models.CASCADE, null=True)
    guardian_name = models.CharField(max_length=200)
    guardian_email = models.EmailField(max_length=200)
    mobile_number = models.PositiveBigIntegerField(unique=True)

    def __str__(self):
        return self.guardian_name


class StaffLeave(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    leave_subject = models.CharField(max_length=255)
    leave_message = models.TextField()
    leave_date = models.DateField()

    def __str__(self):
        return str(self.staff) + ", " + self.leave_subject


class StaffAttendance(models.Model):
    CHOICE = (
        ('Present', 'Present'),
        ('Absent', 'Absent'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=CHOICE, default='Absent')
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.staff)


class StudentAttendance(models.Model):
    CHOICE = (
        ('Present', 'Present'),
        ('Absent', 'Absent'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=CHOICE, default='Present')
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.student)

# class TimeTable(models.Model):
#     CHOICE = (
#         ('Monday', 'Monday'),
#         ('Tuesday', 'Tuesday'),
#         ('Wednesday', 'Wednesday'),
#         ('Thursday', 'Thursday'),
#         ('Friday', 'Friday'),
#     )
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     time_period = models.CharField(max_length=11, help_text='08:10-08:50')
#     subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
#     day = models.CharField(max_length=10, choices=CHOICE, default='Monday')
#     date_created = models.DateTimeField(default=timezone.now)
#
#     def __str__(self):
#         return self.day
