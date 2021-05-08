from django.urls import path
from . import views
urlpatterns = [
    path('', views.signup, name='signup'),
    path('artical', views.artical_your, name='artical'),
    path('user', views.logins, name='login'),
    path('login', views.check_user, name='check_user'),
    path('logout', views.logouth, name='logout'),
    path('insert', views.insert_blog, name='insert'),
]