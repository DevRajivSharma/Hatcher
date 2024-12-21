from django.shortcuts import render,redirect
# Create your views here.

from dashboard.models import user_table
def landing_page(request):
    return render(request,'credentials/landing_page.html')

def register(request):
    if request.method == "POST":
        print('inside register')
        user = request.POST
        profile_image = request.FILES.get('Profile_Image')
        data = {
            'first_name': user.get('FirstName'),
            'last_name': user.get('LastName'),
            'phone_no': user.get('phone_number'),
            'user_bio': user.get('Bio'),
            'age': user.get('age'),
            'user_profile_image': profile_image,
            'email': user.get('Email'),
            'password': user.get('Password')
        }
        # Save the user instance
        user_instance = user_table.objects.create(**data)
        user_instance.save()
        request.session['is_authenticated'] = True 
        request.session['user_id'] = user_instance.id 
        # Pass the user instance to the template
        return redirect('dashboard:home')
    return render(request, 'credentials/register.html')
def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Validate email and password
        try:
            
            print(email,password) 
            user = user_table.objects.get(email=email, password=password)
            request.session['is_authenticated'] = True 
            print(user) # Set session flag
            request.session['user_id'] = user.id        # Store user ID in session (optional)
            print(user.id)
            return redirect('dashboard:home')  # Redirect to dashboard after login
        except user_table.DoesNotExist:
            return render(request, 'credentials/login.html', {'error': 'Invalid credentials'})
    return render(request, 'credentials/login.html')
def logout(request):
    request.session.flush()
    return render(request, 'credentials/login.html')