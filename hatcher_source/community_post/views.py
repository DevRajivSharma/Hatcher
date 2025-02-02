from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from dashboard.models import *
from credentials.models import *
from community_post.models import *
from complete_profile.models import *
from django.template.loader import render_to_string
def post_list(request): 
    posts = Post.objects.select_related('user').all()        
    # Precompute whether the user has liked each post
    user_id = request.session.get('user_id')
    user = user_table.objects.get(id=user_id)
    liked_posts =  Post.objects.filter(likes__user=user).all()
    liked_post_ids = liked_posts.values_list('id', flat=True)  
    print(f'liked post id list is :{liked_post_ids}')
    return render(request, 'dashboard/community_post.html', {'user':user, 'posts': posts, 'liked_post_ids': liked_post_ids})


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
            print(user.first_name)
            print(content)
            # Create a new post with the user and content
            post = Post(user=user, content=content)
            post.save()  # Save the post to the database

            return redirect('community_post:post_list')

        else:
            return JsonResponse({"error": "Content cannot be empty."}, status=400)

    # If it's a GET request, just redirect to the post list page
    return render(request,'dashboard/add_post.html')

def edit_post(request, post_id):
    if request.method == 'POST':
        # Get the updated content from the form
        updated_content = request.POST.get('updated_content')
        user_id = request.session.get('user_id')
        user = user_table.objects.get(id=user_id)
        user_detail = UserDetail.objects.get(user = user)
        if not user_id:
            return JsonResponse({"error": "User not logged in."}, status=400)

        try:
            # Fetch the post by ID
            post = Post.objects.get(id=post_id, user_id=user_id)  # Ensure the post belongs to the logged-in user
        except Post.DoesNotExist:
            return JsonResponse({"error": "Post not found or you are not authorized to edit it."}, status=404)

        if updated_content:
            # Update the content of the post
            post.content = updated_content
            post.save()  # Save the updated post to the database

            return redirect('community_post:post_list')  # Redirect to the post list page

        else:
            return JsonResponse({"error": "Updated content cannot be empty."}, status=400)
    post = Post.objects.get(id=post_id)
    return render(request, 'dashboard/edit_post.html', {'post': post})
    
def my_post(request):
    print('Inside my post')
    user_id = request.session.get('user_id')
    user = user_table.objects.get(id=user_id)
    my_posts = Post.objects.filter(user=user)
    print(my_post)
    liked_posts = Post.objects.filter(likes__user=user)
    liked_post_ids = liked_posts.values_list('id', flat=True)

    # Render partial HTML for the posts
    post_html = render_to_string('partial/community_partial.html', {
        'user': user,
        'posts': my_posts,
        'liked_post_ids': liked_post_ids,
    })
    # Return JSON response
    return HttpResponse(post_html, content_type='text/html')

def delete_post(request):
    user_id = request.session.get('user_id')
    user = user_table.objects.get(id=user_id)
    post_id = request.GET.get('post_id')
    if not post_id:
        return JsonResponse({"error": "Post ID is missing"}, status=400)
    try:
        post = Post.objects.get(id=post_id)
        if post.user != user:
            return JsonResponse({"error": "You are not authorized to delete this post"}, status=403)
        post.delete()
    except Post.DoesNotExist:
        return JsonResponse({"error": "Post not found"}, status=404)
    
    my_posts = Post.objects.filter(user=user)
    liked_posts = Post.objects.filter(likes__user=user)
    liked_post_ids = liked_posts.values_list('id', flat=True)

    # Render partial HTML for the posts
    post_html = render_to_string('partial/community_partial.html', {
        'user': user,
        'posts': my_posts,
        'liked_post_ids': liked_post_ids,
    })
    # Return JSON response
    return HttpResponse(post_html, content_type='text/html')

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

def post_filter(request):
    user_id = request.session.get('user_id')
    if request.method == "POST":
        user = user_table.objects.get(id=user_id)
        post_by_user = Post.objects.filter(user__id = user_id)
        post_user_liked = Post.objects.filter()
        search_keyword = request.POST.get('search_keyword')
        liked_posts =  Post.objects.filter(likes__user=user).all()
        liked_post_ids = liked_posts.values_list('id', flat=True)  
        if search_keyword:
            post_by_search_keyword= Post.objects.filter(content__icontains = search_keyword) | Post.objects.filter(user__first_name__icontains = search_keyword) | Post.objects.filter(user__last_name__icontains = search_keyword)
            return render(request, 'dashboard/community_post.html', {'user':user, 'posts': post_by_search_keyword, 'liked_post_ids': liked_post_ids})
        