from turtle import title
from django.shortcuts import render

posts = [
    {
        'author': 'Suraj Wate',
        'title': 'Blog Post 1',
        'content': 'Content of the first blog post.',
        'date_posted': 'January 17, 2022'
    },
    {
        'author': 'Kushal Wate',
        'title': 'Blog Post 2',
        'content': 'Content of the second blog post.',
        'date_posted': 'January 18, 2022'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})