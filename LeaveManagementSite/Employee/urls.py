from django.urls import path
from . import views

app_name = 'Employee'

urlpatterns = [
    path('', views.home_employee, name='home_employee'),
    path('announcements/', views.announcement_list, name='announcement_list'),
    path('apply/', views.apply_work, name='apply_work'),  
    path('application/', views.application, name='application'), 
    path('application/update/<int:pk>/', views.update_application, name='update_application'),
    path('application/status/<int:pk>/<str:new_status>/', views.update_status, name='update_status'),
    path('application/clears/',views.clear_requests,name="clears"),
    path('payroll/', views.payroll, name='payroll'),
    path('payroll_list/', views.payroll_list, name='payroll_list'),
    path('add/', views.add_payroll, name='add'),
    path('announcements/clear/',views.clear_request,name="clear"),
]
