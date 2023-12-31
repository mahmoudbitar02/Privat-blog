from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=10000)
    image= models.ImageField(upload_to="posts/")
    author= models.ForeignKey(User,related_name="post_author",on_delete=models.CASCADE)
    tags = TaggableManager()
    cattegory =models.ForeignKey('Cattegory',related_name='post_cattegory', on_delete= models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title




class Cattegory(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name



    
