from django.db import models
from datetime import datetime


# Create your models here.

class PostModel(models.Model):
    username = models.CharField(max_length=50)
    created_datetime:datetime = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=2000)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.username} - {self.title}"
    
class LikesModel(models.Model):
    username = models.CharField(max_length=50)
    post_id = models.ForeignKey('PostModel', on_delete=models.CASCADE, related_name='likes_set')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['username', 'post_id'], name='unique_user_post_like')
        ]