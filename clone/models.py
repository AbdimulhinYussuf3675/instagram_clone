from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField

# Create your models here.

class  Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    location = models.CharField(max_length=50, blank=True)
    photo = models.ImageField(upload_to='media/users/' , blank=True , default='../static/photos/profile.jpeg')
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

class Image(models.Model):
    name = models.CharField(max_length=30, blank=True)
    image = models.ImageField(upload_to='posts', blank=True)
    caption = models.TextField(blank=True)
    profile = models.ForeignKey(Profile , on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='likes', blank=True, )
    created_at =models.DateTimeField(auto_now_add=True,blank=True,null =True)

    class Meta:
        ordering = ['-pk']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def all_likes(self):
        return self.likes.count()
        
    def __str__(self):
        return self.name
    

    @classmethod
    def update_caption(cls,pk,caption_update):
        image = cls.objects.get(pk = pk)
        image.update(caption = caption_update)

    @classmethod
    def get_image(cls,id):
        image = cls.objects.get(id = id)
        return image

class Comment(models.Model):
    commenting = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    comment = models.TextField()
    post = models.ForeignKey(Image, on_delete=models.CASCADE)

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()


class Follow(models.Model):
    user_from = models.ForeignKey(User , related_name = 'rel_from_set' , on_delete=models.CASCADE)
    user_to = models.ForeignKey(User , related_name ='rel_to_set' ,on_delete=models.CASCADE)

User.add_to_class('following',
                  models.ManyToManyField('self',
                                        through=Follow,
                                        related_name='followers',
                                        symmetrical=False
                                        ))

# class Post(models.Model):
#     image = models.ImageField(upload_to='posts/')
#     name = models.CharField(max_length=250, blank=True)
#     caption = models.CharField(max_length=250, blank=True)
#     likes = models.ManyToManyField(User, related_name='likes', blank=True, )
#     user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')
#     created = models.DateTimeField(auto_now_add=True, null=True)
#     image = CloudinaryField('image')

#     class Meta:
#         ordering = ["-pk"]

#     def get_absolute_url(self):
#         return f"/post/{self.id}"

#     @property
#     def get_all_comments(self):
#         return self.comments.all()

#     def save_image(self):
#         self.save()

#     def delete_image(self):
#         self.delete()

#     def total_likes(self):
#         return self.likes.count()

#     def __str__(self):
#         return f'{self.user.name} Post'