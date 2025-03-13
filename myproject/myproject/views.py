from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse("I'm home")
    return render(request, 'home.html')

def aboutpage(request):
    # return HttpResponse("About section")
    return render(request, 'about.html')