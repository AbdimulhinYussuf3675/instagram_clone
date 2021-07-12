from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse,HttpResponseRedirect
from .forms import loginForm,UserRegistratinForm,UserEditForm,ProfileEditForm,ImageForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from .models import Profile,Image,Comment,Follow
from  django.contrib import messages
from django.contrib.auth.models import User



def register(request):
    if request.method == 'POST':
        user_form = UserRegistratinForm(request.POST)
        
        if user_form.is_valid():
           
            new_user = user_form.save(commit= False)
           
            new_user.set_password(user_form.cleaned_data['password'])
            
            new_user.save()
            Profile.objects.create(user= new_user)
            messages.success(request ,'Account created successfully')
            return redirect('dashboard')

        else:
            messages.error(request ,'Error creating your account')
            return render(request,'account/register.html' , {'user_form':user_form})


    else:
        user_form = UserRegistratinForm()

        return render(request,'account/register.html' , {'user_form':user_form})



@login_required
def dashboard(request):
    posts = Image.objects.all()
    comments = Comment.objects.all()
    

    return render(request,'account/dashboard.html', {'posts':posts , 'comments':comments})

@login_required
def edit(request):
    if request.method == 'POST':
        user_form =UserEditForm(instance=request.user , data=request.POST)
        profile_form =ProfileEditForm(instance = request.user.profile, data =request.POST, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request ,'Profie updated successfully')
        
        else:
            messages.error(request,'Error updating profile')

    else:
        user_form = UserEditForm(instance=request.user)
        profile_form=ProfileEditForm(instance=request.user.profile)

    return render(request, 'account/edit.html', {'user_form':user_form , 'profile_form':profile_form})

@login_required
def create(request):
    if request.method == 'POST':
        image_form = ImageForm(request.POST,request.FILES)
        profile = Profile.objects.get(user__id = request.user.id)

        if image_form.is_valid():
            post = image_form.save(commit = False)
            post.profile = profile
            post.save()

            messages.success(request ,'New Post added successfully')
            return redirect('dashboard')

    else:
        image_form= ImageForm()
        return render(request,'account/post.html', {'image_form':image_form})

def profile(request):
    profile = Profile.objects.get(user__id = request.user.id)
    images = Image.objects.filter(profile = profile)

    followers = Follow.objects.filter(user_to = request.user).count()
    following = Follow.objects.filter(user_from = request.user).count()
    return render(request ,'account/profile.html' , {'profile':profile , 'images':images , "followers":followers,"following":following})


def get_profile(request,username):
  
    profile = Profile.objects.get(user__username = username) 
    images = Image.objects.filter(profile = profile)
    user = User.objects.get(username=username)

    if Follow.objects.filter(user_from=request.user,user_to = user).exists():
        is_follow =True
    else:
        is_follow =False
    
    followers = Follow.objects.filter(user_to = user).count()
    following = Follow.objects.filter(user_from = user).count()

    return render(request ,'account/profile.html' , {'profile':profile , 'images':images , "is_follow":is_follow,"followers":followers,"following":following})


def comment(request,pk):
    post = Image.objects.get(pk =pk)

    if request.POST.get('comment'):
        new_comment = Comment(comment =request.POST.get('comment'))
        new_comment.commentor = request.user
        new_comment.post = post
        new_comment.save()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    else:

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def follow(request,user_to):

    user = User.objects.get(id=user_to)
    is_follow = False
    rel = Follow.objects.filter(user_from = request.user , user_to = user)
    if rel.exists():
        rel.delete()
        is_follow = False
    else:
        Follow(user_from = request.user, user_to = user).save()
        is_follow =True

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    

def like(request):
    
    data = json.loads(request.body)
    post_id = data['postId']
    action = data['action']

    post = Image.objects.get(id =post_id)
    data = {}

    if post.likes.filter(id = request.user.id).exists():
        post.likes.remove(request.user)
        data = {'is_liked':False}
          
        
    else:
        post.likes.add(request.user)
        data = {'is_liked':True}

    print(post_id)
    print(action)
    
    return JsonResponse(data)

def searches(request):
    if request.GET.get('search'):
        search = request.GET['search']
        profiles = Profile.objects.filter(user__username__icontains = search)
        searchterm = f'{search}'
        return render(request,'account/searches.html' , {'profiles':profiles, 'searchterm':searchterm})
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    




    


    