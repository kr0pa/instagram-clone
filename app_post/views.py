from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
import requests
from django.contrib.auth.decorators import login_required
from .models import Post


def home(request):
    posts = Post.objects.all()
    response = requests.get('https://randomuser.me/api/?results=35')
    data = response.json()

    people = []
    if 'results' in data:
        for user in data['results']:
            first_name = user['name']['first']
            last_name = user['name']['last']
            username = user['login']['username']
            picture = user['picture']['medium']
            city = user['location']['city']
            
            people.append({
                'first_name': first_name, 
                'last_name': last_name,
                'username': username,
                'picture': picture,
                'city': city
                 })
    else:
        print('Nie udało się pobrać danych użytkowników')

    return render(request, 'home.html', {'people': people, 'posts': posts})


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('app_post:home')
    else:
        form = PostForm()
    
    return render(request, 'create_post.html', {'form': form})


def handler404(request, exception):
    
    return render(request, '404.html', status=404)