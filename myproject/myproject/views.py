from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    #return HttpResponse('Hello World! Im Home')
    return render(request, 'home.html')

def about(request):
    #return HttpResponse("I'M About Page")
    return render(request, 'about.html')