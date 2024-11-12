from django.shortcuts import render,redirect
from django.http import JsonResponse
from dashboard.models import user_table,Post
def post_list(request):
    posts = Post.objects.select_related('user').all() 
    return render(request, 'dashboard/community_post.html', {'posts': posts})
def add_post(request):
    if request.method == 'POST':
        # Get the content from the form
        content = request.POST.get('new_post')

        # Get the user ID from the session
        user_id = request.session.get('user_id')

        if not user_id:
            return JsonResponse({"error": "User not logged in."}, status=400)

        # Fetch the user from the user_table using the session-stored user ID
        try:
            user = user_table.objects.get(id=user_id)
        except user_table.DoesNotExist:
            return JsonResponse({"error": "User does not exist."}, status=400)

        if content:
            # Create a new post with the user and content
            post = Post(user=user, content=content)
            post.save()  # Save the post to the database

            # Return a success response (optional: for AJAX)
            return redirect('community_post:post_list')

        else:
            return JsonResponse({"error": "Content cannot be empty."}, status=400)

    # If it's a GET request, just redirect to the post list page
    return redirect('community_post:post_list')

