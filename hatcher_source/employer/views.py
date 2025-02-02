from django.shortcuts import render,redirect
from .models import *
from .middleware import *
from django.contrib import messages
from django.contrib.auth.hashers import check_password,make_password
from django.db.models import Q
from credentials.models import user_table
from complete_profile.models import UserDetail,userResume
from django.template.loader import render_to_string
from django.http import JsonResponse,HttpResponse
from dashboard.models import *
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
        return redirect('employer:employer_login')
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
            print(password.strip(), employer.password)
            if check_password(password.strip(), employer.password):
                print('Employer authenticated')
                request.session['is_emp_authenticated'] = True
                request.session['employer_id'] = employer.id
                return redirect('employer:employer_dashboard')  # Redirect to dashboard after login
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
    # Fetch employer instance from the database using user_id
    users = user_table.objects.all()
    employer_id = request.session.get('employer_id')
    company_register = company.objects.filter(recruiter__id=employer_id)
    return render(request, 'emp_dashboard/home.html',context={'users':users,'company_register':company_register})

@company_exist
def add_job(request):
    employer_id = request.session.get('employer_id')
    emp_table = employer_table.objects.get(id=employer_id) 
    emp_companies = company.objects.filter(cmp_email=emp_table.email)
    emp_cmp_name = emp_companies.values_list('name')
    
    if request.method == 'POST':
        form = request.POST
        f_cmp = form.get('company')
        print(f_cmp)
        try:
            cmp = company.objects.get(name=f_cmp)
        except company.DoesNotExist:
            print('There is no such company')
            return render(request, 'emp_dashboard/add_job.html', context={'Message': 'There is no such company'})
        
        # Handle salary disclosure
        salary_disclose = form.get('salary_disclose') == 'disclose'
        salary_minimum = form.get('salary_minimum') if salary_disclose else None
        salary_maximum = form.get('salary_maximum') if salary_disclose else None
        print(form.get('job_type'))
        data = {
            'company': cmp,
            'job_type': form.get('job_type'),
            'work_type': form.get('work_type'),
            'title': form.get('title'),
            'experience': form.get('experience'),
            'total_vacancy': form.get('total_vacancy'),
            'description': form.get('description'),
            'location': form.get('location'),
            'salary_disclose': salary_disclose,
            'salary_minimum': salary_minimum,
            'salary_maximum': salary_maximum,
            'perks':form.get('perks')
        }
        job = Job.objects.create(**data)
        job.save()
        data2 = {
            'job': job,
            'imp_skill': form.get('imp_skill'),
            'skill_2': form.get('skill_2'),
            'skill_3': form.get('skill_3'),
            'skill_4': form.get('skill_4'),
            'education': form.get('education'),
            'speak_lng_1': form.get('speak_lng_1'),
            'speak_lng_2': form.get('speak_lng_2'),
        }
        req_skill.objects.create(**data2)
        
        return redirect('employer:employer_dashboard')
    
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
        return redirect('employer:employer_dashboard')
    return render(request,'emp_dashboard/company_form.html')

def search_candidate(request):
    if request.method == 'GET':
        employer_id = request.session.get('employer_id')
        keyword = request.GET.get('search_keyword', '').strip()  # Get the keyword keyword from POST request
        request.session['search_keyword'] = keyword
        if keyword:
            query = Q(
                Q(first_name__icontains=keyword) |
                Q(last_name__icontains=keyword) |
                Q(details__bio__icontains=keyword) |
                Q(details__applying_for__icontains=keyword) |
                Q(details__gender__icontains=keyword) |
                Q(details__location__icontains=keyword) |
                Q(details__education_level__icontains=keyword) |
                Q(details__diploma_degree__icontains=keyword) |
                Q(details__iti_degree__icontains=keyword) |
                Q(details__graduate_degree__icontains=keyword) |
                Q(details__postgraduate_degree__icontains=keyword) |
                Q(details__specialization__icontains=keyword) |
                Q(details__college_name__icontains=keyword) |
                Q(details__school_medium__icontains=keyword) |
                Q(details__job_title__icontains=keyword) |
                Q(details__job_role__icontains=keyword) |
                Q(details__company_name__icontains=keyword) |
                Q(details__industry__icontains=keyword) |
                Q(details__notice_period__icontains=keyword) |
                Q(details__experience__icontains=keyword) |
                Q(details__other_languages__icontains=keyword) |
                Q(details__skills__icontains=keyword)
            )
            candidates = user_table.objects.filter(query).distinct()
            print('Here are the candidates')
            company_register = company.objects.filter(recruiter__id=employer_id)
            return render(request, 'emp_dashboard/home.html',context={'users':candidates,'company_register':company_register,'search_keyword':keyword})
        else:
            candidates = user_table.objects.all()
            company_register = company.objects.filter(recruiter__id=employer_id)
            return render(request, 'emp_dashboard/home.html',context={'users':candidates,'company_register':company_register})
        
def posted_jobs(request):
    emp_id = request.session.get('employer_id')
    employer_instance = employer_table.objects.get(id=emp_id)
    posted_jobs = Job.objects.filter(company__recruiter=employer_instance)
    posted_jobs_val = posted_jobs.values(
        'company__name', 'company__image', 'title', 'req_skill__imp_skill',
        'req_skill__education', 'salary_maximum', 'salary_minimum', 'location',
        'job_type', 'created_at', 'location', 'id', 'work_type', 'experience', 'description','current_application'
    )
    return render(request, 'emp_dashboard/Posted_job.html', context={ 'posted_jobs': posted_jobs_val}) 
@auth
def applications(request):
    emp_id = request.session.get('employer_id')
    employer_instance = employer_table.objects.get(id=emp_id)
    posted_jobs = Job.objects.filter(company__recruiter=employer_instance)
    job_with_applications = posted_jobs.filter(current_application__gt=0)
    posted_jobs = posted_jobs.filter(current_application__gt=0)
    # posted_jobs_val = posted_jobs.values(
    #         'company__name', 'company__image', 'title', 'req_skill__imp_skill',
    #         'req_skill__education', 'salary_maximum', 'salary_minimum', 'location',
    #         'job_type', 'created_at', 'location', 'id', 'work_type', 'experience', 'description','current_application'
    #     )
    posted_jobs_val = posted_jobs.values(
            'company__name', 'company__image', 'title', 'req_skill__imp_skill',
            'req_skill__education', 'salary_maximum', 'salary_minimum', 'location',
            'job_type', 'created_at', 'location', 'id', 'work_type', 'experience', 'description','current_application'
        )
    job_with_applications_values = job_with_applications.values(
            'company__name', 'company__image', 'title', 'req_skill__imp_skill',
            'req_skill__education', 'salary_maximum', 'salary_minimum', 'location',
            'job_type', 'created_at', 'location', 'id', 'work_type', 'experience', 'description','current_application'
        )
    # applications = Application.objects.filter(job__company__recruiter=employer_instance)
    # applications_val = applications.values('job__company__name','job__company__image', 'job__title', 'job__location', 'job__job_type', 'job__work_type', 'job__experience', 'job__salary_maximum', 'job__salary_minimum', 'job__created_at', 'job__location', 'job__id', 'status')
    # print(applications_val)
    # print('applications')
    return render(request, 'emp_dashboard/applications.html', context={ 'posted_jobs': posted_jobs_val,
    'job_with_applications':job_with_applications_values}) 

def applicants_user(request, job_id):
    job = Job.objects.get(id=job_id)
    applications = Application.objects.filter(job=job)
    candidates = user_table.objects.filter(applications__in=applications)

    # Prepare a dictionary to store the application statuses for each candidate
    candidates_status = {
        candidate.id: Application.objects.filter(user=candidate, job=job).first().status
        for candidate in candidates
    }

    return render(request, 'emp_dashboard/applicant_user.html', context={'users': candidates, 'candidates_status': candidates_status, 'job': job})



def user_profile(request,id):
    print(id)
    user_instance = user_table.objects.get(id=id)
    user_detail = UserDetail.objects.get(user=user_instance)
    user_resume,created = userResume.objects.get_or_create(user = user_instance)
    return render(request, 'emp_dashboard/candidates_profile.html', context={'user': user_instance,'user_detail' : user_detail,'user_resume':user_resume})

def accept_applicant(request, job_id, user_id):
    if request.method == 'POST':
        job = Job.objects.get(id=job_id)
        user = user_table.objects.get(id=user_id)
        application = Application.objects.filter(job=job, user=user).first()
        application.status = 'Accepted'
        application.save()
        return redirect('employer:applicants_user', job_id=job_id)

def reject_applicant(request, job_id, user_id):
    if request.method == 'POST':
        job = Job.objects.get(id=job_id)
        user = user_table.objects.get(id=user_id)
        application = Application.objects.filter(job=job, user=user).first()
        application.status = 'Rejected'
        application.save()
        return redirect('employer:applicants_user', job_id=job_id)
    
def edit_company(request, cmp_id):
    company_instance = company.objects.get(id=cmp_id)
    if request.method == 'POST':
        form = request.POST
        image = request.FILES.get('image')
        company_instance.name = form.get('name')
        company_instance.description = form.get('bio')
        company_instance.total_staff = form.get('employees')
        company_instance.city = form.get('address')

        if image:  # Only update image if a new one is provided
            company_instance.image = image

        company_instance.save()  # Save the changes to the database
        return redirect('employer:employer_dashboard')
    return render(request,'emp_dashboard/edit_company_form.html', context={'cmp': company_instance})

def delete_company(request, cmp_id):
    company_instance = company.objects.get(id=cmp_id)
    company_instance.delete()
    return redirect('employer:employer_dashboard')