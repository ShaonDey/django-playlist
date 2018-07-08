from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    #return HttpResponse('this is a Homepage')
    return render(request, 'homepage.html')

def about(request):
    #return HttpResponse('its the about page')
    return render(request, 'about.html')
