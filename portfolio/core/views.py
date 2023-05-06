from django.shortcuts import render
from django.http import HttpResponse

# views


def index(request):
    return render(request, "index.html")

def contact(request):
    return render(request, "contact.html")

def projects(request):
    return render(request, "projects.html")

def resume(request):
    return render(request, "resume.html")
