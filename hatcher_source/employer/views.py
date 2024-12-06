from django.shortcuts import render,redirect
from .models import *
from .middleware import *
from django.contrib import messages



# Create your views here.
def employer_login(request):
    return

def employer_register(request):
    if request.method == "POST":
        employer = request.POST
        
        data = {
            'first_name':employer.get('FirstName'),
            'last_name':employer.get('LastName'),
            'phone_no':employer.get('phone_number'),
            'email':employer.get('Email'),
            'password':employer.get('Password'),
            'age' :employer.get('Age'),
        }
        # Save theemployer instance
        employer_instant = employer_table.objects.create(**data)
        employer_instant.save()
        request.session['is_authenticated'] = True 
        request.session['employer_id'] = employer_instant.id 
        # Pass the user instance to the template
        return redirect('employer_login')
    return render(request, 'credentials/employer_register.html')
def employer_login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            
            employer = employer_table.objects.get(email=email, password=password)
            request.session['is_emp_authenticated'] = True 
            request.session['employer_id'] = employer.id 
            return redirect('employer_dashboard')  # Redirect to dashboard after login
        except employer_table.DoesNotExist:
            return render(request, 'credentials/employer_login.html', {'error': 'Invalid credentials'})
    return render(request, 'credentials/employer_login.html')

def employer_logout(request):
    request.session.flush()
    return render(request, 'credentials/employer_login.html')


@auth
def employer_dashboard(request):
    # Retrieve employer ID from session
    employer_id = request.session.get('employer_id')
    print(employer_id)
    if employer_id:
        # Fetch employer instance from the database using user_id
        employer_instance = employer_table.objects.get(id=employer_id)
        
        # Pass theemployer instance to the template
        return render(request, 'emp_dashboard/home.html', {'employer':employer_instance})
    return redirect('employer_login')

@company_exist
def start_hiring(request):
    
    return render(request,'emp_dashboard/add_job.html')

def company_register(request):
    if request.method == 'POST':
        form = request.POST
        image = request.FILES.get('image')
        employer_id = request.session.get('employer_id')
        emp_table = employer_table.objects.get(id = employer_id) 
        print(f'ID = {employer_id} , USERNAME = {emp_table.username}')
        print('creating company with this data')
        data = {
            'hr' : emp_table.username,
            'name' : form.get('name'),
            'bio' : form.get('bio'),
            'employees' : form.get('employees'),
            'image' : image,
            'address' : form.get('address'),
        }
        print(data)
        company.objects.create(**data)
        company.save()
        print(emp_table.company_exist)
        emp_table.company_exist = True
        emp_table.save()
        return redirect(employer_dashboard)
    return render(request,'emp_dashboard/company_form.html')