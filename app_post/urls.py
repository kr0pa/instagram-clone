from django.urls import path
from . import views

app_name = 'app_post'
urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_post, name='create_post'),
]