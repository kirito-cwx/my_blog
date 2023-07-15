from django.contrib import admin
from .models import Blog_Type, Blog


# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'blog_type', "author", "readed_num", "last_update_time")


@admin.register(Blog_Type)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ("type_name",)
