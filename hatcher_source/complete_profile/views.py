from pyexpat.errors import messages
from django.shortcuts import render,redirect
from dashboard.middlewares import auth
from datetime import datetime,date
# Create your views here.
from .models import UserDetail,userResume
from credentials.models import user_table
@auth
def basic_detail(request):
    user_id = request.session.get('user_id')
    user = user_table.objects.get(id=user_id)
    user_detail, created = UserDetail.objects.get_or_create(user=user)
    if request.method == 'POST':
        data = request.POST
        user_detail = UserDetail.objects.get(user=user)

        # Parse and update boolean fields
        boolean_fields = [
            'student', 'current_working', 'english', 'day_shift', 
            'night_shift', 'work_from_home', 'work_from_office', 
            'field_job', 'full_time', 'part_time', 'hourly'
        ]
        for field in boolean_fields:
            user_detail.__setattr__(field, field in data)

        # Update other fields
        if 'birth_date' in data and data['birth_date']:
            try:
                user_detail.birth_date = datetime.strptime(data['birth_date'], '%Y-%m-%d').date()
            except ValueError:
                print("Invalid date format. Please use 'yyyy-mm-dd'.")

        if 'bio' in data and data['bio']:
            user_detail.bio = data['bio']
        if 'applying_for' in data and data['applying_for']:
            user_detail.applying_for = data['applying_for']
        if 'gender' in data and data['gender']:
            user_detail.gender = data['gender']
        if 'location' in data and data['location']:
            user_detail.location = data['location']
        if 'education_level' in data and data['education_level']:
            user_detail.education_level = data['education_level']
        if 'graduateDegree' in data and data['graduateDegree']:
            user_detail.graduate_degree = data['graduateDegree']
        if 'specialization' in data and data['specialization']:
            user_detail.specialization = data['specialization']
        if 'college_name' in data and data['college_name']:
            user_detail.college_name = data['college_name']
        if 'school_medium' in data and data['school_medium']:
            user_detail.school_medium = data['school_medium']
        if 'work_experience' in data and data['work_experience']:
            user_detail.work_experience = data['work_experience']
        if 'jobTitle' in data and data['jobTitle']:
            user_detail.job_title = data['jobTitle']
        if 'jobRole' in data and data['jobRole']:
            user_detail.job_role = data['jobRole']
        if 'companyName' in data and data['companyName']:
            user_detail.company_name = data['companyName']
        if 'industry' in data and data['industry']:
            user_detail.industry = data['industry']
        if 'notice_period' in data and data['notice_period']:
            user_detail.notice_period = data['notice_period']
        if 'salary' in data and data['salary']:
            try:
                user_detail.salary = int(data['salary'].replace(",", ""))
            except ValueError:
                print("Invalid salary format.")
        if 'work_start_date' in data and data['work_start_date']:
            try:
                user_detail.work_start_date = datetime.strptime(data['work_start_date'], '%Y-%m-%d').date()
            except ValueError:
                print("Invalid work start date format.")
        if 'college_start_date' in data and data['college_start_date']:
            try:
                user_detail.college_start_date = datetime.strptime(data['college_start_date'], '%Y-%m-%d').date()
            except ValueError:
                print("Invalid work start date format.")
        if 'college_end_date' in data and data['college_end_date']:
            try:
                user_detail.college_end_date = datetime.strptime(data['college_end_date'], '%Y-%m-%d').date()
            except ValueError:
                print("Invalid work start date format.")
        if 'work_end_date' in data and data['work_end_date']:
            try:
                user_detail.work_end_date = datetime.strptime(data['work_end_date'], '%Y-%m-%d').date()
            except ValueError:
                print("Invalid work end date format.")
        if 'experience' in data and data['experience']:
            user_detail.experience = data['experience']
        if 'other_language' in data and data['other_language']:
            user_detail.other_languages = data['other_language']

        user_detail.save()
        return redirect('complete_profile:resume')

    return render(request, 'profile/complete_profile.html',context={'user_detail':user_detail})


@auth
def resume(request):
    if request.method == 'POST':
        uploaded_file = request.FILES.get('resume')
        if uploaded_file:  # Ensure a file was uploaded
            user_id = request.session.get('user_id')
            user = user_table.objects.get(id=user_id)
            userResume_instance, created = userResume.objects.get_or_create(user=user)
            
            # Assign the uploaded file to the FileField
            userResume_instance.resume_file = uploaded_file
            userResume_instance.save()

            return redirect('dashboard:home')
    return render(request, 'profile/resume.html')

@auth
def skip(request):
    return redirect('dashboard:home')

def edit_job_preference(request):
    
    return redirect('dashboard:profile')

def delete_resume(request, resume_id):
    if request.method == "POST":
        user_resume = userResume.objects.get(id=resume_id)
        user_resume.resume_file.delete()  # Deletes the file from the storage
        user_resume.delete()  # Deletes the record from the database
        return redirect('dashboard:profile')
    return redirect('profile')  # Replace with your profile view name

def update_profile_image(request):
    if request.method == 'POST':
        print('Inside update profile image')
        image = request.FILES.get('profile_image')
        if image:
            print('Got Image')
            print(image)
            user_id = request.session.get('user_id')
            user = user_table.objects.get(id=user_id)
            user.user_profile_image = image
            user.save()
            return redirect('dashboard:profile')
        return redirect('dashboard:profile')