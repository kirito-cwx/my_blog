from django.contrib import admin
from .models import Article
# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # 显示
    list_display = ("id","title","content","read_num","is_deleted","author","last_update_time","create_time")
    ordering = ("-id",)

# admin.site.register(Article,ArticleAdmin)
