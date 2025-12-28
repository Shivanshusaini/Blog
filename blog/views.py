from django.http import HttpResponse
from django.shortcuts import render ,redirect
from blogs.models import Category ,Blogs
from .forms import RegisterationForm
from django.contrib import auth

from django.contrib.auth.forms import AuthenticationForm
def home(request):
    # return HttpResponse("Welcome to the Blog Home Page!")
    categories= Category.objects.all()
    featured_post = Blogs.objects.filter(is_featured=True,status='Published')
    post= Blogs.objects.filter(is_featured=True,status='Published')

    # print(post)
    # terminal show
    # <QuerySet [<Blogs: How AI Coding Assistants Are Changing Software Development>]>
    context ={
        'categories': categories,
        'featured_post':  featured_post,
        'post':post
        
    }
    return render(request , 'home.html' ,context)

def register(request):
    if request.method=="POST":
        form =RegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
    else:
        form =RegisterationForm()
    context ={
            'form':form
    }
    return render(request, 'register.html',context)


def login(request):
    if request.method=="POST":
        form =AuthenticationForm(request,request.POST)
        if form.is_valid():
            username= form.cleaned_data['username']
            password= form.cleaned_data['password']

            user =auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('dashboards')

    else:
        form =AuthenticationForm()
    context ={
            'form':form
    }
    return render(request,'login.html',context)

def logout(request):
    auth.logout(request)
    return redirect('home')