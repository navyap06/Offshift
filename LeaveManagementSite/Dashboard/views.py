from django.shortcuts import render, redirect, get_object_or_404
from .models import LeaveRequest,LeaveRequest1 ,Contact, Feedback
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,  login , logout
from django.contrib import messages
from django.contrib.auth.models import User



def Dashboard_index(request):
    return render(request,"Dashboard_index.html")



def signUp(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        if password != cpassword:
            messages.error(request, 'Passwords do not match')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already used')
        else:

            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
            )
            messages.success(request, 'Registration successful! You can now login.')
            return redirect('login')

    return render(request, "signUp.html")


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        selected_role = request.POST.get('role')

        user = authenticate(request, username=username, password=password)
        if user:
            if selected_role == 'superadmin' and user.is_superuser:
                login(request, user)
                return redirect('home') 
            elif selected_role == 'admin' and user.is_staff and not user.is_superuser:
                login(request, user)
                return redirect('home') 
            elif selected_role == 'user' and not user.is_staff and not user.is_superuser:
                login(request, user)
                return redirect('home') 
            else:
                messages.error(request, "Invalid credentials: Role mismatch")
                return redirect('login')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')

    return render(request, 'login.html')


def explore(request):
    return render(request,"explore.html")


def AboutUs(request):
    return render(request,"AboutUs.html")


@login_required
def apply_leave(request):
    if request.method == 'POST':
        LeaveRequest.objects.create(
            employee_name=request.POST['employee_name'],
            leave_type=request.POST['leave_type'],
            start_date=request.POST['start_date'],
            end_date=request.POST['end_date']
        )
        return redirect('leave_request')  
    return render(request, 'apply_leave.html')

@login_required
def apply_leave1(request):
    if request.method == 'POST':
        LeaveRequest1.objects.create(
            employee_name=request.POST['employee_name'],
            leave_type=request.POST['leave_type'],
            start_date=request.POST['start_date'],
            end_date=request.POST['end_date']
        )
        return redirect('leave_request2')

    return render(request, 'apply_leave1.html')


@login_required
def leave_request(request):
    if request.user.is_staff:
        leave_requests = LeaveRequest.objects.all().order_by('-id')
    else:
        leave_requests = LeaveRequest.objects.filter(employee_name=request.user).order_by('-id')

    return render(request, 'leave_request.html', {'leave_requests': leave_requests})

@login_required
def leave_request2(request):
    leave_request2 = LeaveRequest1.objects.all().order_by('-id')
    return render(request, 'leave_request2.html', {'leave_request2': leave_request2})

@login_required
def leave_request1(request):
    if request.method == "POST":
        leave_id = request.POST.get('leave_id')
        action = request.POST.get('action')
        leave = get_object_or_404(LeaveRequest, id=leave_id)

        if action == "approve":
            leave.status = "Approved"
            leave.save()
        elif action == "reject":
            leave.status = "Rejected"
            leave.save()
        elif action == "delete":
            leave.delete()

        return redirect('leave_request1')  

    leave_requests = LeaveRequest.objects.all().order_by('-id')
    return render(request, 'leave_request1.html', {'leave_requests': leave_requests})


@login_required
def leave_request3(request):
    if request.method == "POST":
        leaves_id = request.POST.get('leaves_id')
        action = request.POST.get('action')
        leaves = get_object_or_404(LeaveRequest1, id=leaves_id)

        if action == "approve":
            leaves.status = "Approved"
            leaves.save()
        elif action == "reject":
            leaves.status = "Rejected"
            leaves.save()
        elif action == "delete":
            leaves.delete()

        return redirect('leave_request3')  

    leave_request2 = LeaveRequest1.objects.all().order_by('-id')
    return render(request, 'leave_request3.html', {'leave_request2': leave_request2})



@login_required
def profile_view(request):
    users=User.objects.all()
    return render(request,"profile.html",context={'users':users})


@login_required
def clear_leave_requests(request):
    if request.method == "POST":
        LeaveRequest.objects.all().delete()
    return redirect('leave_request') 

@login_required
def clear_leave_requests1(request):
    if request.method == "POST":
        LeaveRequest1.objects.all().delete()
    return redirect('leave_request2') 



@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')


@login_required
def contact_view(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        message = request.POST.get('message')


        if not username or not email or not message:
            return render(request, 'contact_Us.html', {'error': 'All fields are required!'})


        Contact.objects.create(name=username, email=email, message=message)
        
        return redirect('thank_you') 

    return render(request, 'contact_Us.html')


@login_required
def thank_you_view(request):
    return render(request, 'thank_you.html')



@login_required
def feedback_form(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        rating = request.POST.get('rating')
        message = request.POST.get('message')

        if name and email and rating and message:
            Feedback.objects.create(
                name=name,
                email=email,
                rating=int(rating),
                message=message
            )
            return redirect('feedback')  

   
    feedbacks = Feedback.objects.all().order_by('-created_at')
    return render(request, 'feedback.html', {'feedbacks': feedbacks})


def update_feedback(request, pk): 
    feedback = get_object_or_404(Feedback, pk=pk)

    if request.method == 'POST':
        feedback.name = request.POST.get('name')
        feedback.email = request.POST.get('email')
        feedback.rating = request.POST.get('rating')
        feedback.message = request.POST.get('message')
        feedback.save()
        return redirect('feedback') 

    return render(request, 'update_feedback.html', {'feedback': feedback})

def delete_feedback(request, pk):
    feedback = get_object_or_404(Feedback, id=pk)
    feedback.delete()
    return redirect('feedback')


