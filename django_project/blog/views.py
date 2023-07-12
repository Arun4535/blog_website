from django.forms.models import BaseModelForm
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView
)

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

class PostListView(ListView):
    model=Post #model class that we want to show data from
    template_name='blog/home.html'#template name where the list will be <app_name>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering=['-date_posted']

class PostDetailView(DetailView):
    model=Post #model class that we want to show data from

class PostCreateView(CreateView):
    model=Post #model class that we want to show data from\\
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    


def about(request):
    return render(request , 'blog/about.html',{'title' : 'About'})

