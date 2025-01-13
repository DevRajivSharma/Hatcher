
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404 , redirect
from credentials.models import user_table  # Ensure correct model import
from django.core.serializers import serialize
from .middlewares import auth
from employer.models import *
from django.db.models import Q
from django.utils import timezone
from datetime import timedelta

# import requests,json
@auth
def home(request):
    # Retrieve user ID from session
    user_id = request.session.get('user_id')
    # print(user_id)

    if user_id:
        # Fetch user instance from the database using user_id
        user_instance = user_table.objects.get(id=user_id)
        # print('user')
        jobs = Job.objects.all()
        jobs_val = jobs.values('company__name','company__image','title','req_skill__imp_skill','req_skill__education','salary','location','job_type','updated_at','location','id','work_type','experience')
        # print('jobs is ',jobs_val)
        # Pass the user instance to the template
        return render(request, 'dashboard/home.html',context =  {'user': user_instance,'jobs':jobs_val})
    
    # If user_id not found in session, redirect to login or show an error
    return redirect('login')  # Replace 'login' with the actual login URL name


def job_search(request):
    user_id = request.session.get('user_id')
    user_instance = user_table.objects.get(id=user_id)
    job_type = request.GET.get('job_type', '')
    keyword = request.GET.get('keyword', '').strip()
    location = request.GET.get('location', '').strip()
    print(job_type)
    print(keyword)
    print(location)
    # Filter jobs based on user input
    query = Q()

    # Add conditions for filtering
    if job_type and job_type != 'Any':
        query &= Q(job_type__icontains=job_type)
    if keyword:
        query &= (
            Q(title__icontains=keyword) |
            Q(description__icontains=keyword) |
            Q(company__name__icontains=keyword) |
            Q(company__description__icontains=keyword)
        )
    if location:
        query &= Q(location__icontains=location) | Q(company__city__icontains=location)

    # Filter jobs based on the query
    jobs = Job.objects.filter(query).distinct()
    print(jobs)
    jobs_val = jobs.values('company__name','company__image','title','req_skill__imp_skill','req_skill__education','salary','location','job_type','updated_at','location','id')
    # print(jobs_val)
    return render(request, 'dashboard/home.html',context =  {'user': user_instance,'jobs':jobs_val})
    # return redirect('home',context =  {'user': user_instance,'company':jobs_val})

def job_search_ajax(request):
    if request.method == "GET":
        job_type = request.GET.get('job_type', '')
        salary = request.GET.get('salary', '')
        posted_in = request.GET.get('posted_in', '')
        work_type = request.GET.get('work_type','')
        query = Q()
        print(job_type,salary,posted_in,work_type)
        if job_type:
            print('inside_job_type')
            query &= Q(job_type__icontains=job_type)
        if work_type:
            print('inside_job_type')
            query &= Q(work_type__icontains=work_type)
        if salary and salary != '-1':
            print('inside_job_type')
            query &= Q(salary__gte=int(salary))
        if posted_in and posted_in != '-1':
            print('inside_job_type')
            time_threshold = timezone.now() - timedelta(hours=int(posted_in))
            print(time_threshold)
            query &= Q(updated_at__gte=time_threshold)

        jobs = Job.objects.filter(query).distinct()
        jobs_val = list(jobs.values(
            'company__name', 'company__image', 'title', 'salary',
            'location', 'job_type', 'updated_at', 'id'
        ))
        return JsonResponse({'jobs': jobs_val}, safe=False)

    return JsonResponse({'error': 'Invalid request'}, status=400)


def job_detail(request, job_id):
    user_id = request.session.get('user_id')
    user_instance = user_table.objects.get(id=user_id)
    job = get_object_or_404(Job, id=job_id)
    return render(request, 'dashboard/job_detail.html', context={'user': user_instance, 'job': job})