from pyexpat import model
from django.contrib import admin
from .models import Post
from django.contrib import admin

model_list = [Post]
admin.site.register(model_list)

