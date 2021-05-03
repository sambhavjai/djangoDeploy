from django.shortcuts import render
from basic_app.forms import UserForm,UserProfileInfoForm,LoginForm

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'basic_app/index.html')

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data = request.POST)
        userprofile_form = UserProfileInfoForm(data = request.POST)

        if user_form.is_valid() and userprofile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            user_profile = userprofile_form.save(commit = False)
            user_profile.user = user

            if 'profile_pic' in request.FILES:
                user_profile.profile_pic = request.FILES['profile_pic']

            user_profile.save()
            registered = True

        else:
            print(user_form.errors,userprofile_form.errors)
    else:
        user_form = UserForm()
        userprofile_form = UserProfileInfoForm()
    return render(request,'basic_app/registeration.html',{'user_form':user_form,'profile_form':userprofile_form,'registered':registered})

def user_login(request):

    if request.method == 'POST':
        login_form = LoginForm(data = request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username = username,password = password)
            if user:
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect(reverse('index'))
                else:
                    return HttpResponse('User not active')
            else:
                print('some malicious user tried to login')
                print('username:{} and password: {}'.format(username,password))
                return HttpResponse('Invalid Login Details')
    else:
        login_form = LoginForm()
    return render(request,'basic_app/login.html',{'login_form':login_form})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def other(request):
    return render(request,'basic_app/other.html')

def relative_url(request):
    return render(request,'basic_app/relative_url.html')
