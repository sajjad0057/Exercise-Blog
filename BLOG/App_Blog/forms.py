from django import forms
from App_Blog.models import Blog,Comment,Likes
from ckeditor.widgets import CKEditorWidget


class BlogForm(forms.ModelForm):
    blog_content = forms.CharField(widget=CKEditorWidget())
    class Meta():
        model = Blog
        fields = ('blog_title','blog_content','blog_image')


class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ['comment',]
    
    
