from django.shortcuts import render,redirect
from dashboard.middlewares import auth
from datetime import datetime,date
# Create your views here.
from .models import UserDetail,userResume
from credentials.models import user_table
@auth
def basic_detail(request):
    if request.method == 'POST':
        data = request.POST
        print('Inside')
        print(data)
        user_id = request.session.get('user_id')
        user = user_table.objects.get(id=user_id)
        user_detail, created = UserDetail.objects.get_or_create(user=user)

        # Only update attributes if they are present in data and not empty
        if 'birth_date' in data and data['birth_date']:
            birth_date_str = data['birth_date']
            try:
                user_detail.birth_date = datetime.strptime(birth_date_str, '%Y-%m-%d').date()
            except ValueError:
                print("Invalid date format. Please use 'yyyy-mm-dd'.")

        if 'bio' in data and data['bio']:
            user_detail.bio = data['bio']
        if 'gender' in data and data['gender']:
            user_detail.gender = data['gender']
        if 'location' in data and data['location']:
            user_detail.location = data['location']
        if 'student' in data and data['student']:
            user_detail.student = data['student'] == 'true'
        if 'education_level' in data and data['education_level']:
            user_detail.education_level = data['education_level']
        if 'diploma_degree' in data and data['diploma_degree']:
            user_detail.diploma_degree = data['diploma_degree']
        if 'iti_degree' in data and data['iti_degree']:
            user_detail.iti_degree = data['iti_degree']
        if 'graduateDegree' in data and data['graduateDegree']:
            user_detail.graduate_degree = data['graduateDegree']
        if 'postgraduateDegree' in data and data['postgraduateDegree']:
            user_detail.postgraduate_degree = data['postgraduateDegree']
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
        if 'current_working' in data and data['current_working']:
            user_detail.current_working = data['current_working'] == 'true'
        if 'notice_period' in data and data['notice_period']:
            user_detail.notice_period = data['notice_period']
        if 'salary' in data and data['salary']:
            user_detail.salary = data['salary']
        if 'work_start_date' in data and data['work_start_date']:
            user_detail.work_start_date = data['work_start_date']
        if 'work_end_date' in data and data['work_end_date']:
            user_detail.work_end_date = data['work_end_date']
        if 'experience' in data and data['experience']:
            user_detail.experience = data['experience']
        if 'english' in data and data['english']:
            user_detail.english = data['english'] == 'true'
        if 'other_language' in data and data['other_language']:
            user_detail.other_languages = data['other_language']
        if 'day_shift' in data and data['day_shift']:
            user_detail.day_shift = data['day_shift'] == 'true'
        if 'night_shift' in data and data['night_shift']:
            user_detail.night_shift = data['night_shift'] == 'true'
        if 'work_form_home' in data and data['work_form_home']:
            user_detail.work_from_home = data['work_form_home'] == 'true'
        if 'work_from_office' in data and data['work_from_office']:
            user_detail.work_from_office = data['work_from_office'] == 'true'
        if 'field_job' in data and data['field_job']:
            user_detail.field_job = data['field_job'] == 'true'
        if 'full_time' in data and data['full_time']:
            user_detail.full_time = data['full_time'] == 'true'
        if 'part_time' in data and data['part_time']:
            user_detail.part_time = data['part_time'] == 'true'
        if 'hourly' in data and data['hourly']:
            user_detail.hourly = data['hourly'] == 'true'

        user_detail.save()
        return redirect('complete_profile:resume')

    return render(request, 'profile/complete_profile.html')


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