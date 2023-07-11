from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
# blog (app) -> templates -> blog -> templates.html

posts = [
    {
        'author' : 'Arun',
        'title' : 'GenAI',
        'content': "This is a Genetic Algorithm based project which uses machine learning to generate music",
        'date_posted' : 'July 06 2023'
    },
    {
        'author' : 'Rinkal',
        'title' : 'Chatbot POC',
        'content' : 'Creating a chatbot using GenAI',
        'date_posted' : 'July 06 2023'
    }
]
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request , 'blog/home.html' , context)



def about(request):
    return render(request , 'blog/about.html',{'title' : 'About'})

