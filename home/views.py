from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact 
# Create your views here.
def index(Request):
    context = {
        "variable1":"variable is sent",
        "variable2":"variable is sent again"
    }
    #return HttpResponse("this is home page")
    return render(Request, "index.html",context)

def about(Request):
    return render(Request, "about.html")
    #return HttpResponse("this is about page")

def services(Request):
    return render(Request, "services.html")
    #return HttpResponse("this is services page")

def contact(Request):
    if(Request.method=="POST"):
        name=Request.POST.get('name')
        email=Request.POST.get('email')
        phone=Request.POST.get('phone')
        desc=Request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,
        desc=desc,date=datetime.today())
        contact.save()   

    return render(Request, "contact.html")
    #return HttpResponse("this is services page")

def counselling(Request):
    return render(Request, "counselling.html")