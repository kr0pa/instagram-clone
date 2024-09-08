from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, EditForm
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


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(data=request.POST, files=request.FILES)
        
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('app_post:home')
    else:
        form = PostForm()
    
    return render(request, 'create_post.html', {'form': form})


def view_edit_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    form = EditForm(instance=post)
    
    if request.method == 'POST':
        form = EditForm(data=request.POST, instance=post)
        
        if form.is_valid():
            form.save()
            return redirect('app_post:home')
    
    return render(request, 'view_post.html', {'post': post, 'form': form})


def handler404(request, exception):
    
    return render(request, '404.html', status=404)