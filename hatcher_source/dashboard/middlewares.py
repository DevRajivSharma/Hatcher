# authentication_middleware.py

from django.shortcuts import redirect
from django.urls import reverse

class auth  :
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Define the URLs that don't require login
        allowed_urls = [reverse('login'), reverse('landing_page'),reverse('register'),reverse('employer_register'),reverse('employer_login')]
        print(allowed_urls)
        # Redirect to login if accessing dashboard without being logged in
        if not request.session.get('is_authenticated') and request.path not in allowed_urls:
            return redirect('login')

        response = self.get_response(request)
        return response
