# authentication_middleware.py

from django.shortcuts import redirect
from django.urls import reverse

class auth  :
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Define the URLs that don't require login
        # Redirect to login if accessing dashboard without being logged in
        print('Inside the auth')
        if not request.session.get('is_authenticated') :
            return redirect('login')

        response = self.get_response(request)
        return response
