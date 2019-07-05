
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.allblogs, name='allblogs'),

    #For us to get a detailed view of each writeup, we need to get the blog_id (the specific number of each blog eg: blog title url 1, 2, 3, )
    path('<int:blog_id>/', views.detail, name = 'detail'),

]
