
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.allblogs, name='allblogs'),
    #For us to get a detailed view of each writeup, we need to get the blog_id
    path('<int:blog_id>/', views.detail, name = 'detail'),

]
