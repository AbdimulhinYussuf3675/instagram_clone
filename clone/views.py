from django.shortcuts import render,redirect
from .models import Profile,Image,Comment
from django.http import HttpRequest,HttpResponse,HttpResponseRedirect
from .forms import UserRegistratinForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from  django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.

def register(request):
    if request.method == 'POST':
        user_form = UserRegistratinForm(request.POST)
        
        if user_form.is_valid():
            # create a new user object but avoid saving it yet
            new_user = user_form.save(commit= False)
            # set the chose password
            new_user.set_password(user_form.cleaned_data['password'])
            # save the new user
            new_user.save()
            Profile.objects.create(user= new_user)
            messages.success(request ,'Account created successfully you can login')
            return redirect('dashboard')

        else:
            messages.error(request ,'This account already exist')
            return render(request,'account/register.html' , {'user_form':user_form})


    else:
        user_form = UserRegistratinForm()

        return render(request,'account/register.html' , {'user_form':user_form})



@login_required
def dashboard(request):
    posts = Image.objects.all()
    comments = Comment.objects.all()
    

    return render(request,'account/dashboard.html', {'posts':posts , 'comments':comments})      
