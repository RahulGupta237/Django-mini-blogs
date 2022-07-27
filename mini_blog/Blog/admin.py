from django.contrib import admin

# Register your models here.
from .models import post

@admin.register(post)
class AdminPost(admin.ModelAdmin):
    list_display=['id','title','description']