from django.shortcuts import render_to_response
from read_statistics.utils import get_seven_days_read_data
from django.contrib.contenttypes.models import ContentType
from blog.models import Blog


def home(request):
    blog_content_type = ContentType.objects.get_for_model(Blog)
    dates, read_nums = get_seven_days_read_data(blog_content_type)
    return render_to_response('index.html', context={"read_nums": read_nums, "dates": dates})
