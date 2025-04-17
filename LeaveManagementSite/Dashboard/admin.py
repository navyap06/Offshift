from django.contrib import admin
from Dashboard.models import LeaveRequest,LeaveRequest1,Contact,Feedback


class LeaveRequestAdmin(admin.ModelAdmin):
    list_display=['employee_name','leave_type','start_date','end_date','status']


class LeaveRequest1Admin(admin.ModelAdmin):
    list_display=['employee_name','leave_type','start_date','end_date','status']

class ContactAdmin(admin.ModelAdmin):
    list_display=['name','email','message','submitted_at']


class FeedBackAdmin(admin.ModelAdmin):
    list_display=['name','email','rating','message','created_at']

admin.site.register(Contact,ContactAdmin)    
admin.site.register(LeaveRequest,LeaveRequestAdmin)
admin.site.register(LeaveRequest1,LeaveRequest1Admin)  
admin.site.register(Feedback,FeedBackAdmin)  