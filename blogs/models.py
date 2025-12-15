from django.db import models
 
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