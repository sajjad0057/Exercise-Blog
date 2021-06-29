from django.urls import path
from App_Blog import views

app_name = 'App_Blog'

urlpatterns =[
    path('',views.index, name='index'),
    path('blog/',views.BlogList.as_view(),name='blog_list'),
    path('write/',views.CreateBlog.as_view(),name='create_blog'),
    path('details/<str:slug>/',views.blog_details,name='blog_details'),
    path('liked/<pk>/',views.liked,name='liked'),
    path('unliked/<pk>/',views.unliked,name='unliked'),
    path('edit_blog/<pk>/',views.UpdateBlog.as_view(),name='edit_blog'),
    path('delete_blog/<pk>/',views.DeleteBlog.as_view(),name='delete_blog'),


]

