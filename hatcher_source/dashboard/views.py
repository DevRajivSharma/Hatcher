from django.shortcuts import render, get_object_or_404 , redirect
from credentials.models import user_table  # Ensure correct model import
from .middlewares import auth
from employer.models import *
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
        jobs_val = jobs.values('company__name','company__image','title','req_skill__imp_skill','req_skill__education','salary','location','job_type','updated_at','location','salary','id')
        # print('jobs is ',jobs_val)
        # Pass the user instance to the template
        return render(request, 'dashboard/home.html',context =  {'user': user_instance,'company':jobs_val})
    
    # If user_id not found in session, redirect to login or show an error
    return redirect('login')  # Replace 'login' with the actual login URL name


def j_search(request):
    user_id = request.session.get('user_id')
    user_instance = user_table.objects.get(id=user_id)
    job_type = request.GET.get('job_type').strip()
    keyword = request.GET.get('keyword', '').strip()
    location = request.GET.get('location', '').strip()
    print(job_type)
    print(keyword)
    print(location)
    # Filter jobs based on user input
    jobs = Job.objects.all()
    # print(jobs)
    if job_type:
        jobs = jobs.filter(job_type__icontains=job_type)
    # print(jobs)
    if keyword:
        jobs = jobs.filter(title__icontains=keyword) | jobs.filter(company__name__icontains=keyword)
    # print(jobs)
    if location:
        jobs = jobs.filter(location__icontains=location)
    # print(jobs)

    jobs_val = jobs.values_list(
        'company__name', 'company__image', 'title', 
        'req_skill__imp_skill', 'req_skill__education', 
        'salary', 'location'
    )
    # print(jobs_val)
    return render(request, 'dashboard/home.html',context =  {'user': user_instance,'company':jobs_val})
    # return redirect('home',context =  {'user': user_instance,'company':jobs_val})
