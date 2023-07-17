import datetime
from django.contrib.contenttypes.models import ContentType
from .models import ReadNum, ReadDetail
from django.utils import timezone
from django.db.models import Sum


def read_statistics_once_read(request, obj):
    ct = ContentType.objects.get_for_model(obj)
    key = f'{ct.model}_{obj.pk}_read'
    if not request.COOKIES.get(key):
        # ReadNum存在记录

        # if ReadNum.objects.filter(content_type=ct, object_id=obj.pk).count():
        #     read_num = ReadNum.objects.get(content_type=ct, object_id=obj.pk)
        # # 不存在添加
        # else:
        #     read_num = ReadNum(content_type=ct, object_id=obj.pk)
        read_num, created = ReadNum.objects.get_or_create(content_type=ct, object_id=obj.pk)
        read_num.read_num += 1
        read_num.save()
        date = timezone.now().date()

        # 当天阅读数加一
        read_num_detail, created = ReadDetail.objects.get_or_create(content_type=ct, object_id=obj.pk, date=date)

        read_num_detail.read_num += 1
        read_num_detail.save()

    return key


def get_seven_days_read_data(content_type):
    today = timezone.now().date()
    read_nums = []
    dates = []
    for i in range(7, 0, -1):
        date = today - datetime.timedelta(days=i)
        dates.append(date.strftime('%m/%d'))
        read_details = ReadDetail.objects.filter(content_type=content_type, date=date)
        result = read_details.aggregate(read_num_sum=Sum('read_num'))
        read_nums.append(result['read_num_sum'] or 0)

    return dates,read_nums
