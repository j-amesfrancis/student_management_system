from django.contrib import admin

from .models import Staff, Guardian, StaffLeave, StaffAttendance, StudentAttendance


# Register your models here.

class StaffAdmin(admin.ModelAdmin):
    search_fields = ['email', 'first_name', 'last_name']
    list_display = ['email', 'first_name', 'last_name']
    list_filter = ['class_coordinator']
    fieldsets = [
        ['User Info', {'fields': ['user', 'email']}],
        ['Personal Info', {'fields': ['first_name', 'last_name', 'profile_pic']}],
        ['Subject', {'fields': ['subject']}],
        ['Class Coordinator', {'fields': ['class_coordinator']}]
    ]


class AttendanceAdmin(admin.ModelAdmin):
    list_filter = ['status']


admin.site.register(Staff, StaffAdmin)
admin.site.register(Guardian)
admin.site.register(StaffLeave)
admin.site.register(StaffAttendance, AttendanceAdmin)
admin.site.register(StudentAttendance, AttendanceAdmin)
# admin.site.register(TimeTable)
