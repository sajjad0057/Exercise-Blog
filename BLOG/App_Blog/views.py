from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, ListView, DetailView, View, TemplateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from App_Blog.models import Blog,Likes,Comment
from App_Blog.forms import CommentForm,BlogForm
from django.urls import reverse,reverse_lazy
from ckeditor.fields import RichTextField


# Create your views here.
def index(request): 
    return HttpResponseRedirect(reverse('App_Blog:blog_list'))

def blog_list(request):
    return render(request,'App_Blog/blog_list.html',context={})

class CreateBlog(LoginRequiredMixin,CreateView):
    model=Blog  
    form_class = BlogForm
    template_name= 'App_Blog/create_blog.html'

    def form_valid(self,form):
        blog_obj = form.save(commit=False)
        blog_obj.author = self.request.user
        blog_obj.save()
        return HttpResponseRedirect(reverse('App_Blog:index'))


class BlogList(ListView):
    context_object_name = 'blogs'
    model = Blog
    template_name = 'App_BLog/blog_list.html'
    def get_context_data(self, **kwargs):
    # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['r_blogs'] = Blog.objects.all()[0:3]
        #print("context---->: ",context)
        return context

@login_required
def blog_details(request,slug):
    blog = Blog.objects.get(slug=slug)
    form = CommentForm()
    already_liked = Likes.objects.filter(blog=blog,user=request.user)
    if already_liked:
        liked = True
    else:
        liked = False
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.blog = blog
            comment.save()
            return HttpResponseRedirect(reverse('App_Blog:blog_details',kwargs={'slug':slug}))


    return render(request,'App_Blog/blog_details.html',context={'blog':blog,'form':form, 'liked':liked})

class MyBlogs(LoginRequiredMixin,TemplateView):
    template_name = 'App_Blog/profile.html'



@login_required
def liked(request,pk):
    blog = Blog.objects.get(pk=pk)
    user = request.user
    already_liked = Likes.objects.filter(blog=blog, user=user)
    if not already_liked:
        liked_post = Likes(blog=blog,user=user)
        liked_post.save()
    return HttpResponseRedirect(reverse('App_Blog:blog_details',kwargs={'slug':blog.slug}))

@login_required
def unliked(request,pk):
    blog = Blog.objects.get(pk=pk)
    user = request.user
    already_liked = Likes.objects.filter(blog=blog, user=user)
    already_liked.delete()
    return HttpResponseRedirect(reverse('App_Blog:blog_details',kwargs={'slug':blog.slug}))


class UpdateBlog(LoginRequiredMixin,UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = 'App_Blog/edit_blog.html'
    def get_context_data(self,**kwargs):
        x = super().get_context_data(**kwargs)
        x['update_blog']='update_blog'
        return x
        
    
    def get_success_url(self,**kwargs):
        return reverse_lazy('App_Blog:blog_details',kwargs={'slug':self.object.slug})




    
class DeleteBlog(DeleteView):
    model = Blog
    template_name = 'App_Blog/delete_blog.html'
    success_url = reverse_lazy('App_Login:profile')
        
    
    
    

