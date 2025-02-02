
import time
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404 , redirect
from credentials.models import user_table  # Ensure correct model import
from django.core.serializers import serialize
from .middlewares import auth
from employer.models import *
from django.db.models import Q
from django.utils import timezone
from datetime import timedelta
from complete_profile.models import *
from dashboard.models import *
from django.middleware.csrf import get_token
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.core.paginator import Paginator
import pickle
import base64
# import requests,json


def load_jobs(request):
    time.sleep(0.5)  # Simulate network latency
    
    page = request.GET.get('page', 1)  # Get page number from request
    jobs_per_page = 10  # Load 10 jobs at a time
    
    # Retrieve filter query stored in session, or use default if not present
    query = Q()  # Default empty query
    if 'job_filter_query' in request.session:
        try:
            query_str = request.session['job_filter_query']
            query = pickle.loads(base64.b64decode(query_str))
        except (pickle.UnpicklingError, ValueError, KeyError):
            query = Q()  # Fallback in case of invalid or corrupt data

    # Apply pagination on filtered query
    jobs = Job.objects.filter(query).distinct().order_by('created_at')
    jobs_val = jobs.values(
        'company__name','company__image','title','req_skill__imp_skill',
        'req_skill__education','salary_maximum','salary_minimum','location',
        'job_type','updated_at','location','id','work_type','experience',
        'perks','salary_disclose'
    )

    paginator = Paginator(jobs_val, jobs_per_page)

    # Check if the requested page exceeds the total pages
    if int(page) > paginator.num_pages:
        return JsonResponse({'jobs_html': ''})  # No more jobs to load

    jobs_page = paginator.page(page)

    # Render jobs to an HTML string
    jobs_html = render_to_string('partial/home_partial.html', context={'jobs': jobs_page})
    current_page = paginator.get_page(page)
    
    return JsonResponse({'jobs_html': jobs_html, 'total_jobs': paginator.count}, safe=False)
@auth
def home(request):
    # Retrieve user ID from session
    user_id = request.session.get('user_id')
    # 
# print(user_id)
    search_query = request.session.get('search_query', {})
    if user_id:
        # Fetch user instance from the database using user_id
        user_instance = user_table.objects.get(id=user_id)
        user_detail = UserDetail.objects.get(user=user_instance)
        jobs = Job.objects.all()
        jobs_val = jobs.values('company__name','company__image','title','req_skill__imp_skill','req_skill__education','salary_maximum','salary_minimum','location','job_type','updated_at','location','id','work_type','experience','perks','salary_disclose')

        return render(request, 'dashboard/home.html',context =  {'user': user_instance,'jobs':jobs_val,'search_query': search_query,'user_detail':user_detail,'total_jobs':jobs_val.count()})
    
    # If user_id not found in session, redirect to login or show an error
    return redirect('login')  # Replace 'login' with the actual login URL name

def job_search(request):
    user_id = request.session.get('user_id')
    user_instance = user_table.objects.get(id=user_id)
    keyword = request.GET.get('keyword', '').strip()
    keyword2 = keyword.split(' ')
    
# print(keyword2)
    location = request.GET.get('location', '').strip()

    request.session['search_query'] = {
    'keyword': keyword,
    'location': location,
    }
    search_query = request.session.get('search_query', {})
    # Filter jobs based on user input
    query = Q()

    if keyword:
        for k in keyword2:
            query &= (
                Q(title__icontains=k) |
                Q(description__icontains=k) |
                Q(company__name__icontains=k) |
                Q(company__description__icontains=k)
            )
    if location:
        query &= Q(location__icontains=location) | Q(company__city__icontains=location) |  Q(description__icontains=location)

    # Filter jobs based on the query
    query_str = base64.b64encode(pickle.dumps(query)).decode('utf-8')
    request.session['job_filter_query'] = query_str
    request.session.modified = True  # Ensure session is saved

    jobs = Job.objects.filter(query).distinct()
    jobs_val = jobs.values('company__name','company__image','title','req_skill__imp_skill','req_skill__education','salary_maximum','salary_minimum','location','job_type','updated_at','location','id','work_type','experience','perks','salary_disclose')
    # 
# print(jobs_val)
    return render(request, 'dashboard/home.html',context =  {'user': user_instance,'jobs':jobs_val,'search_query': search_query,'total_jobs':jobs_val.count()})
    # return redirect('home',context =  {'user': user_instance,'company':jobs_val})

def job_search_ajax(request):
    time.sleep(0.5)
    if request.method == "GET":
        search_query = request.session.get('search_query', {})
        keyword = search_query.get('keyword', '')
        location = search_query.get('location', '')

        experience = request.GET.get('experience', '')
        job_type = request.GET.get('job_type', '')
        salary = request.GET.get('salary', '')
        posted_in = request.GET.get('posted_in', '')
        work_type = request.GET.get('work_type','')
        query = Q()


        if (posted_in == '24'):
            posted_in_send = 'Last 24 hours'
        elif (posted_in == '72'):
            posted_in_send = 'Last 3 days'
        elif(posted_in == '168'):
            posted_in_send = 'Last 7 days'
        else:
            posted_in_send = ''
        

        request.session['all_filter'] = {
            'experience' : experience,
            'job_type': job_type,
            'salary':salary,
            'posted_in':posted_in_send,
            'work_type':work_type
        }
        all_filter = request.session.get('all_filter',{})
        
# print(all_filter)
        if experience and experience != 'Any':
            
# print('experience',experience)
            query &= Q(experience__icontains=experience)
        if keyword:
            query &= (
                Q(title__icontains=keyword) |
                Q(description__icontains=keyword) |
                Q(company__name__icontains=keyword) |
                Q(company__description__icontains=keyword)
            )
        if location:
            query &= Q(location__icontains=location) | Q(company__city__icontains=location)


        if job_type:
            job_type_list = job_type.split(',')
            if len(job_type_list) > 1:
                # Use OR logic for multiple job types
                job_type_query = Q()
                for j_type in job_type_list:
                    job_type_query |= Q(job_type__icontains=j_type)  # OR logic
                query &= job_type_query  # Combine with existing query
            else:
                # Use AND logic for a single job type
                query &= Q(job_type__iexact=job_type.strip())  # Exact match for a single type

        if work_type:
            work_type_list = work_type.split(',')
            
# print(work_type_list)
            if len(work_type_list) > 1:
                # Use OR logic for multiple job types
                work_type_query = Q()
                for w_type in work_type_list:
                    work_type_query |= Q(work_type__icontains=w_type)  # OR logic
                query &= work_type_query  # Combine with existing query
            else:
                # Use AND logic for a single job type
                query &= Q(work_type__iexact=work_type.strip())  # Exact match for a single type
        if salary and salary != '-1':
            
# print('salary is',int(salary))
            query &= Q(salary_maximum__gte=int(salary))
        if posted_in and posted_in != '-1':
            time_threshold = timezone.now() - timedelta(hours=int(posted_in))
            query &= Q(created_at__gte=time_threshold)

        query_str = base64.b64encode(pickle.dumps(query)).decode('utf-8')
        request.session['job_filter_query'] = query_str
        request.session.modified = True  # Ensure session is saved
        jobs = Job.objects.filter(query).distinct()

        job_partial = jobs.values('company__name','company__image','title','req_skill__imp_skill','req_skill__education','salary_maximum','salary_minimum','location','job_type','updated_at','location','id','work_type','experience','perks','salary_disclose')

        job_html =  render_to_string('partial/home_partial.html',context={'jobs':job_partial,})
        return JsonResponse({'jobs': job_html,'all_filter':all_filter,'total_jobs':job_partial.count()}, safe=False)

    return JsonResponse({'error': 'Invalid request'}, status=400)


def job_detail(request, job_id):
    user_id = request.session.get('user_id')
    user_instance = user_table.objects.get(id=user_id)
    job = Job.objects.filter(id=job_id)
    applied_jobs = Application.objects.filter(user=user_instance, job__in=job)
    if applied_jobs:
        apply_job = True
    else:
        apply_job = False
    job_val = Job.objects.filter(id=job_id).values(
            'company__name', 'company__image', 'title', 'req_skill__imp_skill',
            'req_skill__education', 'salary_maximum', 'salary_minimum', 'location',
            'job_type', 'created_at', 'location', 'id', 'work_type', 'experience', 'description'
        ).first()
    return render(request, 'dashboard/job_detail.html', context={'user': user_instance, 'job': job_val, 'apply_job': apply_job})


def apply_job(request, job_id): 
    user_id = request.session.get('user_id')
    
# print('user_id is ', user_id)
    user_instance = user_table.objects.get(id=user_id)
    job = Job.objects.get(id=job_id)
    job.current_application += 1
    job.save()
    job_application = Application.objects.create(
        job=job,
        user=user_instance,
    )
    job_application.save()
    email_message = render_to_string('email_temp/job_application_success.html', {'user': user_instance, 'job': job})
    subject = 'Job Application Successful'
    try:
        send_mail(
            subject,
            '',
            settings.EMAIL_HOST_USER,
            [user_instance.email],
            fail_silently=False,
            html_message=email_message,  
        )
    except Exception as e:
        print(e)
    return JsonResponse({'status': 'success'}, status=200)



def applications(request):
    user_id = request.session.get('user_id')
    user_instance = user_table.objects.get(id=user_id)
    applications = Application.objects.filter(user=user_instance)
    applications_val = applications.values('job__company__name','job__company__image', 'job__title', 'job__location', 'job__job_type', 'job__work_type', 'job__experience', 'job__salary_maximum', 'job__salary_minimum', 'job__created_at', 'job__location', 'job__id', 'status')
    
# print(applications_val)
    
# print('applications')
    return render(request, 'dashboard/applications.html', context={'user': user_instance, 'applications': applications_val})

def profile(request):
    user_id = request.session.get('user_id')
    
# print('user_id in profile', user_id)
    user_instance = user_table.objects.get(id=user_id)
    user_detail = UserDetail.objects.get(user=user_instance)
    user_resume,created = userResume.objects.get_or_create(user = user_instance)
    return render(request, 'dashboard/profile.html', context={'user': user_instance,'user_detail' : user_detail,'user_resume':user_resume})