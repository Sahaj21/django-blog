from django.contrib import admin
from django.db import models
from .models import Post
from tinymce.widgets import TinyMCE


# Register your models here.

class PostAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Title/Slug/Author", {'fields': ["title", "slug","author"]}),
        ("Content/Status", {"fields": ["content","status"]})
    ]

    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }


admin.site.register(Post,PostAdmin)
