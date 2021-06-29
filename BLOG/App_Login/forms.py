from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from App_Login.models import UserProfile


# create Forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    class Meta():
        model = User
        fields = ('username','email','password1','password2')

class UserProfileChange(UserChangeForm):
    password = None
    class Meta():
        model = User
        fields = ('username','first_name','last_name','email')


class ProfilePicForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields =('profile_pic',)
