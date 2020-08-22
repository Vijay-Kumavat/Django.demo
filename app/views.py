from django.shortcuts import render,redirect
from app.models import Contact
from django.contrib import messages
from django.contrib.auth import logout,login,authenticate 
from django.contrib.auth.models import User

# from datetime import datetime
# Create your views here.

def index(request):
    # context = {
    #     "variable" : "this is context"
    # }
    # return HttpResponse("This is App page")
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,('index.html'))

def about(request):
    # return HttpResponse("This is About page")
    return render(request,('about.html'))


def services(request):
    # return HttpResponse("This is services page")
    return render(request,('services.html'))

def loginuser(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request,user)
            return redirect('/') 
        else:
            return render(request,('login.html'))
            # No backend authenticated the credentials
        # return HttpResponse("This is services page")
    return render(request,('login.html'))

def logoutuser(request):
    logout(request)
    # return HttpResponse("This is services page")
    # return render(request,('login.html'))
    return redirect("/login")

def contact(request):
    # return HttpResponse("This is contact page")
    if request.method=="POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        phone= request.POST.get('phone')
        desc= request.POST.get('desc')
        # date= request.POST.get('date')
        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
        messages.success(request, 'Your message has been send !')        
    return render(request,('contact.html'))
      
        # name= request.POST.get('name')

    # contact=Contact(name=name,email=email,phone=phone,desc=desc)
    # contact.save()
    # return render(request,('contact.html'))
