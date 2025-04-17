from django.contrib import admin
from .models import Payroll
from .models import Announcement, Application, Payroll


@admin.register(Payroll)
class PayrollAdmin(admin.ModelAdmin):
    list_display = ('employee', 'salary', 'deductions', 'total_pay', 'month')
    readonly_fields = ('total_pay',)  

class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at',)


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'age', 'reason', 'user')
    search_fields = ('name', 'skills')
    list_filter = ('status',)


admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(Application, ApplicationAdmin)
