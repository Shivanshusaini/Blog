from django.contrib import admin
from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category_name", "is_created", "is_updated")

# admin.site.register(Category,CategoryAdmin)
# does not this work the same as the decorator above?