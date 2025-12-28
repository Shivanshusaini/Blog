from django.shortcuts import render
from blogs.models import Category,Blogs
# Create your views here.
def dashboards(request):
    category_count = Category.objects.all().count()
    blogs_count = Blogs.objects.all().count()
    context = {
       
       'category_count':category_count,
       'blogs_count':blogs_count
    }
  
    return  render(request ,'dashboards/dashboard.html',context)