from django.db import models
import datetime as dt
from django.contrib.auth.models import User

# Create your models here.

class  Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    location = models.CharField(max_length=50, blank=True)
    photo = models.ImageField(upload_to='users/' , blank=True , default='../static/photos/profile.jpeg')
    bio = models.TextField(max_length=350, default="Hello their am using instagram_clone", blank=True)

    def save_profile(self):
        self.save()
        

    def delete_profile(self):
        self.delete()

    def __str__(self):
        return self.user.username

    @classmethod
    def search_profile(cls,name):
        profile = cls.objects.filter(user__username__icontains = name)
        return profile

    @classmethod
    def get_profile(cls,id):
        profile = cls.objects.get(id = id)
        return profile
    
