from django.urls import path
from App_Login import views


app_name='App_Login'

urlpatterns =[
    path('sign_up/',views.sign_up,name='sign_up'),
    path('login/',views.login_form,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('change_profile/',views.change_profile,name='change_profile'),
    path('change_password/',views.pass_change,name='change_password'),
    path('update_pro_pic/',views.update_pro_pic,name='update_pro_pic'),
    path('change_pro_pic/',views.change_pro_pic,name='change_pro_pic'),


]
