# authentication_middleware.py
from django.shortcuts import redirect
from django.urls import reverse
from .models  import *
from django.contrib import messages
class auth  :
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Define the URLs that don't require login
        allowed_urls = [reverse('employer_login'), reverse('landing_page'),reverse('employer_register')]

        # Redirect to login if accessing dashboard without being logged in
        if not request.session.get('is_emp_authenticated') and request.path not in allowed_urls:
            return redirect('employer_login')

        response = self.get_response(request)
        return response
    
class company_exist :
    def __init__(self,get_response):
        self.response = get_response
    def __call__(self,request):
        emp_id = request.session.get('employer_id')
        Emp = employer_table.objects.get(id = emp_id)
        if not Emp.company_exist:
            print('There is no company setup.')
            return redirect('company_register')
        return self.response(request)