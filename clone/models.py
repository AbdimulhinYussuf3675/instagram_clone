from django.db import models
import datetime as dt
from django.contrib.auth.models import User

# Create your models here.

class  Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    date_of_birth = models.DateField(blank =True, null =True)
    photo = models.ImageField(upload_to='users/' , blank=True , default='../static/photos/profile.jpeg')
    bio = models.TextField(default="Hello everyone amusing insta-clone")

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
    
