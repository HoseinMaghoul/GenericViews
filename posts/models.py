from django.db import models

# Create your models here.

class PostLiveManage(models.Manager):
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_enable=True)
        return queryset

class Post(models.Model):
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=30)
    text = models.TextField()
    upload_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    live = PostLiveManage()


    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.author


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=20)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.author


