from django.dispatch import receiver
from django.db.models.signals import post_save

from accounts.models import User
from hod.models import Hod, Student
from staff.models import Staff


@receiver(post_save, sender=User)
def user_create(sender, instance, created, **kwargs):
    if created:
        instance.email = instance.username
        if instance.user_roles == 'hod':
            Hod.objects.create(
                user=instance,
                email=instance.username
            )
        elif instance.user_roles == 'staff':
            Staff.objects.create(
                user=instance,
                email=instance.username
            )
        elif instance.user_roles == 'student':
            Student.objects.create(
                user=instance,
                email=instance.username
            )
    else:
        if instance.user_roles == 'hod':
            instance.hod.first_name = instance.first_name
            instance.hod.last_name = instance.last_name
            instance.hod.save()
        elif instance.user_roles == 'staff':
            instance.staff.first_name = instance.first_name
            instance.staff.last_name = instance.last_name
            instance.staff.save()
        elif instance.user_roles == 'student':
            instance.student.first_name = instance.first_name
            instance.student.last_name = instance.last_name
            instance.student.save()
