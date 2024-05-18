from django.shortcuts import render
from .forms import PostForm
import requests


def home(request):
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

    return render(request, 'home.html', {'people': people})


def create_post(request):
    form = PostForm()
    
    return render(request, 'create_post.html', {'form': form})