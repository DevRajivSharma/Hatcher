
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
    search_query = request.session.get('search_query', {})
    if user_id:
        # Fetch user instance from the database using user_id
        user_instance = user_table.objects.get(id=user_id)
        # print('user')
        jobs = Job.objects.all()
        jobs_val = jobs.values('company__name','company__image','title','req_skill__imp_skill','req_skill__education','salary_maximum','salary_minimum','location','job_type','updated_at','location','id','work_type','experience','perks','salary_disclose')
        # print('jobs is ',jobs_val)
        # Pass the user instance to the template
        return render(request, 'dashboard/home.html',context =  {'user': user_instance,'jobs':jobs_val,'search_query': search_query,})
    
    # If user_id not found in session, redirect to login or show an error
    return redirect('login')  # Replace 'login' with the actual login URL name


def job_search(request):
    user_id = request.session.get('user_id')
    user_instance = user_table.objects.get(id=user_id)
    experience = request.GET.get('experience', '')
    keyword = request.GET.get('keyword', '').strip()
    keyword2 = keyword.split(' ')
    print(keyword2)
    location = request.GET.get('location', '').strip()

    request.session['search_query'] = {
    'experience': experience,
    'keyword': keyword,
    'location': location,
    }
    search_query = request.session.get('search_query', {})
    # Filter jobs based on user input
    query = Q()

    # Add conditions for filtering
    if experience and experience != 'Any':
        query &= Q(experience__icontains=experience)
    if keyword:
        for k in keyword2:
            query &= (
                Q(title__icontains=k) |
                Q(description__icontains=k) |
                Q(company__name__icontains=k) |
                Q(company__description__icontains=k)
            )
    if location:
        query &= Q(location__icontains=location) | Q(company__city__icontains=location)

    # Filter jobs based on the query
    jobs = Job.objects.filter(query).distinct()
    jobs_val = jobs.values('company__name','company__image','title','req_skill__imp_skill','req_skill__education','salary_maximum','salary_minimum','location','experience','updated_at','work_type','id','job_type')
    # print(jobs_val)
    return render(request, 'dashboard/home.html',context =  {'user': user_instance,'jobs':jobs_val,'search_query': search_query,})
    # return redirect('home',context =  {'user': user_instance,'company':jobs_val})

def job_search_ajax(request):
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
        print(experience)
        # posted_in_send = ''
        print(posted_in)
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
        print(all_filter)
        if experience and experience != 'Any':
            print('experience',experience)
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
            for j_type in job_type_list:
                query |= Q(job_type__icontains=j_type)
        if work_type:
            work_type_list = work_type.split(',')
            for w_type in work_type_list:
                print(w_type)
                query |= Q(work_type=w_type)
        if salary and salary != '-1':
            print('salary is',int(salary))
            query &= Q(salary_maximum__gte=int(salary))
        if posted_in and posted_in != '-1':
            time_threshold = timezone.now() - timedelta(hours=int(posted_in))
            query &= Q(created_at__gte=time_threshold)

        jobs = Job.objects.filter(query).distinct()
        jobs_val = list(jobs.values('company__name','company__image','title','req_skill__imp_skill','req_skill__education','salary_maximum','salary_minimum','location','job_type','updated_at','location','id','work_type','experience'))
        return JsonResponse({'jobs': jobs_val,'all_filter':all_filter}, safe=False)

    return JsonResponse({'error': 'Invalid request'}, status=400)


def job_detail(request, job_id):
    user_id = request.session.get('user_id')
    user_instance = user_table.objects.get(id=user_id)
    job = Job.objects.filter(id=job_id)
    job_val = Job.objects.filter(id=job_id).values(
            'company__name', 'company__image', 'title', 'req_skill__imp_skill',
            'req_skill__education', 'salary_maximum', 'salary_minimum', 'location',
            'job_type', 'created_at', 'location', 'id', 'work_type', 'experience', 'description'
        ).first()
    print(job_val)
    return render(request, 'dashboard/job_detail.html', context={'user': user_instance, 'job': job_val})