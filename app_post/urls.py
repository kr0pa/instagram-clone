from django.urls import path
from . import views

app_name = 'app_post'
urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_post, name='create_post'),
    path('view/<pk>/', views.view_edit_post, name='view_post')
]