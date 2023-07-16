from django.contrib import admin
from .models import Blog_Type, Blog


# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'blog_type','get_read_num', "author", "last_update_time")


@admin.register(Blog_Type)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ("type_name",)


# @admin.register(ReadNum)
# class ReadNumAdmin(admin.ModelAdmin):
#     list_display = ("read_num", 'blog')
