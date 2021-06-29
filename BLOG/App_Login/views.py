from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from App_Login.forms import SignUpForm, UserProfileChange, ProfilePicForm


# Create your views here.

def sign_up(request):
    form = SignUpForm()
    registered = False
    if request.method =='POST':
        form =SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered = True
    dict = {'form':form,'registered':registered}

    return render(request,'App_Login/sign_up.html',context=dict)

def login_form(request):

    form = AuthenticationForm()
    if request.method == 'POST':

        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user:
                login(request,user)
                return HttpResponseRedirect(reverse('App_Blog:index'))
    dict={'form':form}

    return render(request,'App_Login/login.html',context=dict)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_Blog:index'))


@login_required
def profile(request):
    return render(request,'App_Login/profile.html')

@login_required
def change_profile(request):
    flag = False
    current_user = request.user
    form = UserProfileChange(instance=current_user)
    if request.method == 'POST':
        form = UserProfileChange(request.POST,instance=current_user)
        if form.is_valid():
            form.save()
            flag = True
            form = UserProfileChange(instance=current_user)

    return render(request,'App_Login/change_profile.html',context={'form':form,'flag':flag})



@login_required
def update_pro_pic(request):
    flag = False
    current_user = request.user
    profile_pic_form = ProfilePicForm()
    if request.method =='POST':
        profile_pic_form = ProfilePicForm(request.POST,request.FILES)
        if profile_pic_form.is_valid():
            user_obj=profile_pic_form.save(commit=False)
            user_obj.user = current_user
            user_obj.save()
            flag = True
            return HttpResponseRedirect(reverse('App_Login:profile'))

    return render(request,'App_Login/update_profile_pic.html',context={'profile_pic_form':profile_pic_form, 'flag':flag})

@login_required
def change_pro_pic(request):
    flag = False
    current_user = request.user
    profile_pic_form = ProfilePicForm()
    if request.method =='POST':
        profile_pic_form = ProfilePicForm(request.POST,request.FILES,instance=current_user.user_profile)
        if profile_pic_form.is_valid():
            profile_pic_form.save()
            return HttpResponseRedirect(reverse('App_Login:profile'))

    return render(request,'App_Login/update_profile_pic.html',context={'profile_pic_form':profile_pic_form, 'flag':flag})












@login_required
def pass_change(request):
    flag = False
    current_user = request.user
    form = PasswordChangeForm(current_user)
    if request.method == 'POST':
        form = PasswordChangeForm(current_user,data=request.POST)
        if form.is_valid():
            form.save()
            flag = True
    return render(request,'App_Login/pass_change.html',context={'form':form,'flag':flag})
