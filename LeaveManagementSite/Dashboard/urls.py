from django.urls import path
from . import views


urlpatterns = [
    path('',views.Dashboard_index,name="home"),
    path('signUp/',views.signUp,name="signUp"),
    path('login/',views.login_view,name="login"),
    path('logout/', views.logout_view, name='logout'),
    path('explore/',views.explore,name="explore"),
    path('AboutUs/',views.AboutUs,name="AboutUs"),
    path('apply_leave/',views.apply_leave,name="apply_leave"),
    path('apply_leave1/',views.apply_leave1,name="apply_leave1"),
    path('leave_request/',views.leave_request,name="leave_request"),
    path('clear_leaves/',views.clear_leave_requests,name="clear_leaves"),
    path('clear_leaves1/',views.clear_leave_requests1,name="clear_leaves1"),
    path('leave_request1/',views.leave_request1,name="leave_request1"),
    path('leave_request2/',views.leave_request2,name="leave_request2"),
    path('leave_request3/',views.leave_request3,name="leave_request3"),
    path('profile/', views.profile_view, name='profile'),
    path('contact/', views.contact_view, name='contact'),
    path('thank_you/', views.thank_you_view, name='thank_you'),
    path('feedback/', views.feedback_form, name='feedback'),
    path('update/<int:pk>/', views.update_feedback, name='update'),
    path('delete/<int:pk>/', views.delete_feedback, name='delete'),

]
