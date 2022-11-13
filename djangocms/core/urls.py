from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('post-detail/<int:pk>', views.PostDetail, name='post_detail'),

]
