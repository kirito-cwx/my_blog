from django.db import models
from django.contrib.auth.models import User
# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models.fields import exceptions
from django.contrib.contenttypes.models import ContentType
from read_statistics.models import ReadNumExbandMethod


# Create your models here.

class Blog_Type(models.Model):
    type_name = models.CharField(max_length=15)

    def __str__(self):
        return self.type_name


class Blog(models.Model, ReadNumExbandMethod):
    title = models.CharField(max_length=30)
    blog_type = models.ForeignKey(Blog_Type, on_delete=models.DO_NOTHING, related_name='blog_blog')
    content = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    create_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)

    # 第一种计数方法
    # def read_num(self):
    #     try:
    #         return self.readnum.read_num
    #     except exceptions.ObjectDoesNotExist:
    #         return 0

    # 第二种创建新应用ContentType
    # def read_num(self):
    #     try:
    #         ct = ContentType.objects.get_for_model(self)
    #         readnum = ReadNum.objects.get(content_type=ct, object_id=self.id)
    #         return readnum.read_num
    #     except exceptions.ObjectDoesNotExist:
    #         return 0

    def __str__(self):
        return f'<Blog: {self.title}>'

    class Meta:
        ordering = ['-last_update_time', ]


'''
第一种计数方法
class ReadNum(models.Model):
    read_num = models.IntegerField(default=0)
    blog = models.OneToOneField(Blog, on_delete=models.DO_NOTHING)
'''
