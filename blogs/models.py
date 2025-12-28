from django.db import models
from django.contrib.auth.models import User 

# Importing User model to link with author field

# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=50 ,unique= True)
    is_created=models.DateTimeField(auto_now_add=True)
    is_updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_name
        
    class Meta:
        # verbose_name='category'
        verbose_name_plural='categories'

STATUS_CHOICE=(
    ('draft','Draft'),
    ('Published','Published'),
)

class Blogs(models.Model):
    title= models.CharField(max_length=200 ,unique=True)
    slug= models.SlugField(unique=True, blank=True)
    # slug will be generated automatically from title
    # slug is used in url instead of id
    # slug is the part of url which is used to identify page on  the blog website
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    # ForeignKey is used to create a relationship between two models
    # cascade means if category is deleted then all the blogs under that category will be deleted

    author= models.ForeignKey(User, on_delete=models.CASCADE)
    blog_image=models.ImageField(upload_to='uploads/%y/%m/%d/%H/%M/%S/')
    # upload_to is used to specify the path where the image will be stored

    short_description=models.TextField(max_length=1000)
    blog_body=models.TextField(max_length=3000)
    status=models.CharField(choices=STATUS_CHOICE,default='draft',max_length=100)
    is_featured=models.BooleanField(default=False)
    is_created=models.DateTimeField(auto_now_add=True)
    is_updated=models.DateTimeField(auto_now=True)

    def __str__(self):
            return self.title
    
    class Meta:
        verbose_name_plural='blogs'

    def __str__(self):
         return self.title