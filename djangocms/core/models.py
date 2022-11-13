from distutils.command.upload import upload
from tabnanny import verbose
from turtle import title
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Post Title')
    category = models.CharField(max_length=50, choices=[('0','featured'), ('1','normal')])
    fram = models.CharField(max_length=50, choices=[('0','django'), ('1','flask'),('3','featured')])
    thumbnail = models.ImageField(upload_to='')
    body = RichTextUploadingField(verbose_name='Compose Content')
    summary = models.TextField(verbose_name='Post Summary')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
