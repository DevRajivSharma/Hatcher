from django.shortcuts import render, get_object_or_404 , redirect
from credentials.models import user_table  # Ensure correct model import
from .middlewares import auth

@auth
def home(request):
    # Retrieve user ID from session
    user_id = request.session.get('user_id')
    print(user_id)

    if user_id:
        # Fetch user instance from the database using user_id
        user_instance = user_table.objects.get(id=user_id)
        print('user')
        # Pass the user instance to the template
        return render(request, 'dashboard/home.html', {'user': user_instance})
    
    # If user_id not found in session, redirect to login or show an error
    return redirect('login')  # Replace 'login' with the actual login URL name
