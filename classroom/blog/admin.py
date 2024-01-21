from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display        = ("name", "description")
    list_filter         = ("name", "author", "categories")
    search_fields       = ["name", "description", "author", "categories"]
    prepopulated_fields = {"name": ("name",)}

admin.site.register(Post, PostAdmin)