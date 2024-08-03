from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='home'),
    path('createblog/', views.createeblog, name='createblog'),
    path('singleBlog/', views.singleblog, name='singleBlog'),
    path('<slug:slug>/', views.singleblog, name='singleblog'),
    path('update/<slug:slug>/', views.updateblog, name='updateblog'),
]
