from django.contrib.contenttypes.models import ContentType
from .models import ReadNum

def read_statistics_once_read(request,obj):
    ct = ContentType.objects.get_for_model(obj)
    key = f'{ct.model}_{obj.pk}_read'
    if not request.COOKIES.get(key):

        # ReadNum存在记录

        if ReadNum.objects.filter(content_type=ct, object_id=obj.pk).count():
            readnum = ReadNum.objects.get(content_type=ct, object_id=obj.pk)
        # 不存在添加
        else:
            readnum = ReadNum(content_type=ct, object_id=obj.pk)
        readnum.read_num += 1
        readnum.save()
    return key
