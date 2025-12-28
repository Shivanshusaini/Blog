from django.shortcuts import render , HttpResponse,redirect
from .models import Blogs,  Category
from django.shortcuts import get_list_or_404 ,get_object_or_404
from django.db.models import Q
def posts_by_category(request,category_id):
    
    posts = Blogs.objects.filter(status='Published' ,category= category_id)
    try:
        category = Category.objects.get(pk= category_id)
    except:
        return redirect('home')
    # use try and except when need to perfrom alternated work
    # print(posts)
    
    # category = get_list_or_404(Category,pk= category_id)
    context = {
        'posts':posts,
        'category':category
    }
    return render(request , 'posts_by_category.html' ,context)

# blogs for slug

def blogs(request,slug):
    # get_list_or_404(Blogs , slug=slug , status='Published')
    single_post= get_object_or_404(Blogs , slug=slug , status='Published')
    context = {
        'single_post':single_post
    }
    return render(request,'blogs.html', context)

def search(request):
    keyword = request.GET.get('keyword','').strip()
    blog = Blogs.objects.filter(Q(title__icontains=keyword)|Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword) , status='Published')
    context = {
        'keyword':keyword,
        'blog':blog
    }
    return render(request, 'search.html',context)

