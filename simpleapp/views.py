from django.http import HttpResponse
from django.shortcuts import render  #import render is new here


def about(request):  #when user visits this about url then fires this function
    # return HttpResponse("this is about page")
    return render(request, "about.html")  #always follows with requests at first.

def homepage(request):  #when user visits this about url then fires this function
    # return HttpResponse("This is Home page")
    return render(request, "homepage.html") #always follows with requests at first.

def mypage(request):
    return render(request, "my_page.html")

def mypage(request):
    data = {
        'title':'Home New',
        'bdata':'Welcome to WS Cube',
        'clist':['PHP', 'JAVA', 'Django'],
        'student_details':[
            {'name':'pradeep', 'phone':9856203598,},
            {'name':'testing', 'phone':9852059546},
        ]

    }
    return render(request, "my_page.html", data)



    