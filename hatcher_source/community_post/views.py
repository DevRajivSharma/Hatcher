from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from dashboard.models import *
def post_list(request):
    posts = Post.objects.select_related('user').all()
    # Precompute whether the user has liked each post
    user_id = request.session.get('user_id')
    user = user_table.objects.get(id=user_id)
    liked_posts =  Post.objects.filter(likes__user=user).all()
    liked_post_ids = liked_posts.values_list('id', flat=True)  # Get a list of liked post IDs
    print(f'liked post id list is :{liked_post_ids}')
    return render(request, 'dashboard/community_post.html', {'posts': posts, 'liked_post_ids': liked_post_ids})
def add_post(request):
    if request.method == 'POST':
        # Get the content from the form
        content = request.POST.get('new_post')
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
@csrf_exempt
def toggle_like(request, post_id):
    user_id = request.session.get('user_id')
    user = user_table.objects.get(id=user_id)
    post = Post.objects.get(id=post_id)

    if request.method == "POST":
        print(f'{post_id} is post id')
        # Check if the user already liked the post
        like_exists = Like.objects.filter(user=user, post=post).exists()
        print(like_exists)
        if like_exists:
            # Remove the like if it exists
            Like.objects.filter(user=user, post=post).delete()
            liked = False
        else:
            # Add a like if it doesn't exist
            like = Like.objects.create(user=user, post=post)
            like.save()
            liked = True

        return JsonResponse({"success": True, "liked": liked})
    return JsonResponse({"success": False}, status=400)