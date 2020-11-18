from django.contrib import admin

from .models import Hod, Subject, Course, State, Student, StudentLeave


# Register your models here.
class HodAdmin(admin.ModelAdmin):
    search_fields = ['email', 'first_name', 'last_name']
    list_display = ['email', 'first_name', 'last_name']
    fieldsets = [
        ['User Info', {'fields': ['user', 'email']}],
        ['Personal Info', {'fields': ['first_name', 'last_name', 'profile_pic']}],

    ]


class SubjectAdmin(admin.ModelAdmin):
    search_fields = ['name']


class CourseAdmin(admin.ModelAdmin):
    search_fields = ['name']


admin.site.register(Hod, HodAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(State)
admin.site.register(Student)
admin.site.register(StudentLeave)
