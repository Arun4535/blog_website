from django.forms.models import BaseModelForm
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin


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
    model=Post 

class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post #model class that we want to show data from\\
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
# we used login_required decorator for function, decorater cant be applied to class so LoginRequiredMixin do the same
# UserPassesTestMixin - make sure that login user has access to post created by himself as author - for that test_func() is mandatory

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post #model class that we want to show data from\\
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request , 'blog/about.html',{'title' : 'About'})

