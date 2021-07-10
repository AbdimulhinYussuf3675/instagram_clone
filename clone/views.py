from django.shortcuts import render,redirect

# Create your views here.

def reqister(request):
    if request.method == 'POST':
        USER_FORM = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit= False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            
