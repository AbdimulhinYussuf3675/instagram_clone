from django.test import TestCase
from .models import Profile,Comment,Image
from django.contrib.auth.models import User

class ImageTest(TestCase):
    def setUp(self):
        self.new_user = User.objects.create(username ='Hamisi')
        self.new_profile = Profile.objects.create(user= self.new_user)
        self.new_image = Image(profile = self.new_profile , caption ="New caption")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))
        self.assertTrue(isinstance(self.new_user,User))
        self.assertTrue(isinstance(self.new_profile,Profile))

    def test_save_method(self):
        self.new_image.save_image()
        
        images = Image.objects.all()
        self.assertTrue(len(images)== 1)

    def test_delete_method(self):
        self.new_image.save_image()

        self.new_image.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images)==0)

    def test__init(self):
        self.assertEqual(self.new_image.caption,"New caption")


    

        
    



        
       

