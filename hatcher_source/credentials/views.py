from django.shortcuts import render,redirect
# Create your views here.
from dotenv import load_dotenv
import os
from dashboard.models import *
from .middleware import check_session
load_dotenv()

def landing_page(request):
    return render(request,'credentials/landing_page.html')

def register(request):
    if request.method == "POST":
        print('inside register')
        user = request.POST
        data = {
            'first_name': user.get('FirstName'),
            'last_name': user.get('LastName'),
            'email': user.get('Email'),
            'password': user.get('Password')
        }
        try:
            user_instance = user_table.objects.create(**data)
            user_instance.save()
            print('Registeration Done')
            request.session['is_authenticated'] = True 
            request.session['user_id'] = user_instance.id 
            return redirect('complete_profile:basic_detail')
        except Exception as e:
            render(request, 'credentials/register.html', {'error': 'Invalid credentials'})
    return render(request, 'credentials/register.html',)

def login(request):
    if request.method == "POST":
        email = request.POST.get('Email')
        password = request.POST.get('Password')
        # Validate email and password
        try:
            user = user_table.objects.get(email=email, password=password)
            print(user) # Set session flag
            request.session['is_authenticated'] = True 
            request.session['user_id'] = user.id        # Store user ID in session (optional)
            print(user.id)
            return redirect('dashboard:home')  # Redirect to dashboard after login
        except user_table.DoesNotExist:
            return render(request, 'credentials/login.html', {'error': 'Invalid credentials'})
    return render(request, 'credentials/login.html')

def logout(request):
    request.session.flush()
    return render(request, 'credentials/login.html')

def feedback(request):
    
    if request.method == "POST":
        feedback = request.POST
        data = {
            'name': feedback.get('name'),
            'email': feedback.get('email'),
            'feedback': feedback.get('feedback')
        }
        print(data)
        feedback_instance = FeedBack.objects.create(**data)
        feedback_instance.save()
        return render(request, 'credentials/landing_page.html')
    return render(request, 'credentials/landing_page.html')

