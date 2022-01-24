from django.http import HttpResponse
from django.shortcuts import render  #import render is new here


def about(request):  #when user visits this about url then fires this function
    # return HttpResponse("this is about page")
    return render(request, "about.html")  #always follows with requests at first.

def homepage(request):  #when user visits this about url then fires this function
    # return HttpResponse("This is Home page")
    return render(request, "homepage.html") #always follows with requests at first.
    