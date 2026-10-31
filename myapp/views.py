from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Hello, World! This is the home page of my Django application.</h1>")

def about(request):
    return HttpResponse("<h1>About Page</h1><p>This is the about page of my Django application.</p>")

def cats(request):
    return HttpResponse("<h1>i like cats :)</h1>")