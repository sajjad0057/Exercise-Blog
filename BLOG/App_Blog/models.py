from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Blog(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name='post_author')
    blog_title = models.CharField(max_length=264, verbose_name='Put a Title')
    slug = models.SlugField(max_length=264, unique=True,allow_unicode=True)
    blog_content = RichTextUploadingField(verbose_name='What Is Your Mind ...?')
    blog_image = models.ImageField(upload_to = 'blog_images', verbose_name='Set Image')
    published_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta():
        ordering = ['-published_date',]

  
    def __str__(self):
        return f'{self.blog_title}'

    def _generate_unique_slug(self):
        unique_slug = slugify(self.blog_title,allow_unicode=True)
        num = 10101
        while Blog.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(unique_slug, num)
            num += 30
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._generate_unique_slug()
        super().save(*args, **kwargs)

    


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    class Meta():
        ordering = ['-comment_date',]

    def __str__(self):
        return f'{self.comment}'

class Likes(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='liked_blog')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='liker_user')

    def __str__(self):
        return f'{self.user} Likes {self.blog}'
    
