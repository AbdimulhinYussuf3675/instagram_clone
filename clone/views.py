from django.shortcuts import render,redirect
from .models import Profile
from django.http import HttpRequest,HttpResponse,HttpResponseRedirect
from .forms import loginForm,UserRegistratinForm,UserEditForm,ProfileEditForm,ImageForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from  django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.

def reqister(request):
    if request.method == 'POST':
        USER_FORM = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit= False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            messages.Success(request ,'Account created successfully')
            return redirect('dashboard')

        else:
            messages.error(request, 'Error creating your account')
            return render(request,'account/register.html', {'user_form':user_form})

    else:
        user_form = UserRegistratinForm()
        return render(request, 'account/register.html' , {'user_form':user_form})

        
