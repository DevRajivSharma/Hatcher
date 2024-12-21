from django.shortcuts import render, get_object_or_404 , redirect
from credentials.models import user_table  # Ensure correct model import
from .middlewares import auth
from employer.models import *
@auth
def home(request):
    # Retrieve user ID from session
    user_id = request.session.get('user_id')
    print(user_id)

    if user_id:
        # Fetch user instance from the database using user_id
        user_instance = user_table.objects.get(id=user_id)
        print('user')
        jobs = Job.objects.all()
        jobs_val = jobs.values_list('company__name','company__image','title','req_skill__imp_skill','req_skill__education')
        print('jobs is ',jobs_val)
        print(jobs_val[0][0])
        # Pass the user instance to the template
        return render(request, 'dashboard/home.html',context =  {'user': user_instance,'company':jobs_val})
    
    # If user_id not found in session, redirect to login or show an error
    return redirect('login')  # Replace 'login' with the actual login URL name
