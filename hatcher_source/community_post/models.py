from django.db import models
from credentials.models import *
from django.db.models.signals import *
from django.dispatch import receiver
# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(user_table, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    total_likes = models.IntegerField(default=0)
    def __str__(self):
        return f"Post by {self.user.email}({self.user.first_name} {self.user.last_name})"
    def is_liked_by_user(self, user):
        return self.likes.filter(user=user).exists()

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(user_table, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("post", "user")

    def __str__(self):
        return f"{self.user.email} likes Post {self.post.id}"
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(user_table, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.email} on {self.post.id}"
@receiver(post_save,sender=Like)
def increment_total_likes(sender, instance, created, **kwargs):
    if created:
        instance.post.total_likes += 1
        instance.post.save()

@receiver(post_delete, sender=Like)
def decrement_total_likes(sender, instance, **kwargs):
    instance.post.total_likes -= 1
    instance.post.save()
