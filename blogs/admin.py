from django.contrib import admin
from .models import Category, Blogs


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category_name", "is_created", "is_updated")

# admin.site.register(Category,CategoryAdmin)
# does not this work the same as the decorator above?

@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ('id','title','category','author','status','is_featured','is_created','is_updated')
    prepopulated_fields = {'slug':('title',)}
    search_fields = ('id', 'title', 'category__category_name', 'status')
    list_editable=('is_featured',)

# admin.site.register(Blogs,BlogsAdmin)