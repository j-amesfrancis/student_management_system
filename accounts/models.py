import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


# Models

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    role = (
        ('hod', 'HOD'),
        ('staff', 'STAFF'),
        ('student', 'STUDENT')
    )
    user_roles = models.CharField(max_length=10, verbose_name='User Roles', choices=role,
                                  default='hod', )
