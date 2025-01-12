from django.shortcuts import render,redirect
from .models import *
from .middleware import *
from django.contrib import messages
from django.contrib.auth.hashers import check_password,make_password



# Create your views here.


def employer_register(request):
    if request.method == "POST":
        employer = request.POST
        Password = make_password(employer.get('Password'))
        data = {
            'first_name':employer.get('FirstName'),
            'last_name':employer.get('LastName'),
            'email':employer.get('Email'),
            'password':Password,
        }
        # Save theemployer instance
        employer_instant = employer_table.objects.create(**data)
        employer_instant.save()
        # Pass the user instance to the template
        return redirect('employer_login')
    return render(request, 'credentials/employer_register.html')


def employer_login(request):
    if request.method == "POST":
        email =  request.POST.get('Email')
        password = request.POST.get('Password')
        print(email,password)
        try:
            employer = employer_table.objects.get(email=email.strip())
            # Check if the provided password matches the hashed password in the database
            print(employer.password)
            
            if check_password(password.strip(), employer.password):
                request.session['is_emp_authenticated'] = True
                request.session['employer_id'] = employer.id
                return redirect('employer_dashboard')  # Redirect to dashboard after login
            else:
                return render(request, 'credentials/employer_login.html', {'error': 'Invalid credentials'})
        except employer_table.DoesNotExist:
            print('Employer not found')
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
        cmp  = company.objects.filter(cmp_email=employer_instance.email)
        company_names = cmp.values_list('name', flat=True)
        jobs = Job.objects.filter(company__name__in=company_names)
        print('company  is ',cmp)
        print('company name is ',company_names)
        print(jobs)
        return render(request, 'emp_dashboard/home.html',context={'employer':employer_instance,'posted_job':jobs,'companies':cmp})
    return redirect('employer_login')

@company_exist
def start_hiring(request):
    employer_id = request.session.get('employer_id')
    emp_table = employer_table.objects.get(id = employer_id) 
    emp_companies = company.objects.filter(cmp_email = emp_table.email)
    emp_cmp_name = emp_companies.values_list('name')
    if request.method == 'POST':
        form = request.POST
        f_cmp = form.get('company')
        print(f_cmp)
        try :
            cmp = company.objects.get(name=f_cmp)
        except :
            print('There is so such company')
            return redirect('employer_dashboard')
        data = {
            'company' : cmp,
            'job_type':form.get('job_type'),
            'title' : form.get('title'),
            'description' : form.get('description'),
            'location' : form.get('location'),
            'salary' : form.get('salary'),
        }
        job = Job.objects.create(**data)
        data2 = {
            'job':job,
            'imp_skill' : form.get('imp_skill'),
            'skill_2' : form.get('skill_2'),
            'skill_3' : form.get('skill_3'),
            'skill_4' : form.get('skill_4'),
            'education' : form.get('education'),
            'speak_lng_1' : form.get('speak_lng_1'),
            'speak_lng_2' : form.get('speak_lng_2'),
        }
        re_skill = req_skill.objects.create(**data2)
        return redirect('employer_dashboard')
    return render(request, 'emp_dashboard/add_job.html', context={'emp_cmp_name': emp_cmp_name})

def company_register(request):
    if request.method == 'POST':
        form = request.POST
        image = request.FILES.get('image')
        employer_id = request.session.get('employer_id')
        emp_table = employer_table.objects.get(id = employer_id) 
        print(f'ID = {employer_id} , USERNAME = {emp_table.email}')
        print('creating company with this data')
        if (image == None):
            data = {
            'recruiter': emp_table,
            'cmp_email' : emp_table.email,
            'name' : form.get('name'),
            'description' : form.get('bio'),
            'total_staff' : form.get('employees'),
            'city' : form.get('address'),
        }
        else :
            data = {
            'recruiter': emp_table,
            'cmp_email' : emp_table.email,
            'name' : form.get('name'),
            'description' : form.get('bio'),
            'total_staff' : form.get('employees'),
            'image' : image,
            'city' : form.get('address'),
            }
        
        print(data)
        company.objects.create(**data)
        print(emp_table.company_exist)
        emp_table.company_exist = True
        emp_table.save()
        return redirect('employer_dashboard')
    return render(request,'emp_dashboard/company_form.html')