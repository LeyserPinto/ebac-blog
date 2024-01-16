from django.contrib import admin

# Register your models here.
from .models import Person

class PersonAdmin(admin.ModelAdmin):
    list_display        = ("first_name", "last_name")
    list_filter         = ("first_name", "last_name")
    search_fields       = ["first_name", "last_name"]
    prepopulated_fields = {"last_name": ("last_name",)}

admin.site.register(Person, PersonAdmin)