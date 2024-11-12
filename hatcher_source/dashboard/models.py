from django.db import models

# Create your models here.
class user_table(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=10,unique=True)
    user_bio = models.CharField(max_length=500)
    user_profile_image = models.ImageField(upload_to='user_profile_image', blank=True, null=True)
    email =  models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    username = 'email'
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    age = models.CharField(max_length=10,null=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.email

class Post(models.Model):
    user = models.ForeignKey(user_table, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    total_likes = models.IntegerField(default=0)
    def __str__(self):
        return f"Post by {self.user.email}"

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(user_table, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("post", "user")

    def __str__(self):
        return f"{self.user.email} likes Post {self.post.id}"
    
    
class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    company_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    salary = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Application(models.Model):
    user = models.ForeignKey(user_table, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    application_date = models.DateField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user.email} - {self.job.title}"
class Internship(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    company_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    stipend = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
class Skill(models.Model):
    skill_name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.skill_name

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(user_table, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.email} on {self.post.id}"
