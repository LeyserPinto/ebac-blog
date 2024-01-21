from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display        = ("title", "description")
    list_filter         = ("title", "author", "categories")
    search_fields       = ["title", "description", "author", "categories"]
    prepopulated_fields = {"title": ("title",)}

admin.site.register(Post, PostAdmin)