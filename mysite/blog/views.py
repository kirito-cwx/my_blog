from django.shortcuts import get_object_or_404, render_to_response
from .models import Blog, Blog_Type
from django.core.paginator import Paginator
from django.conf import settings
from django.db.models import Count
from django.contrib.contenttypes.models import ContentType
from read_statistics.models import ReadNum
from read_statistics.utils import read_statistics_once_read


def get_blog_list_common_data(request, blogs_all_list):
    paginator = Paginator(blogs_all_list, settings.EACH_PAGE_BLOG_NUMBER)
    page_num = request.GET.get('page', 1)

    page_of_blogs = paginator.get_page(page_num)
    current_page_num = page_of_blogs.number
    page_range = list(range(max(current_page_num - 2, 1), current_page_num)) + list(range(current_page_num,
                                                                                          min(current_page_num + 2,
                                                                                              paginator.num_pages) + 1))
    # 加上省略页码
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')

    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')
    # if page_range[-1]
    # 加上首页和尾页
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)
    blog_types = Blog_Type.objects.annotate(blog_count=Count('blog_blog'))
    '''
    添加博客分类对应的数量
    blog_types = Blog_Type.objects.all()
    blog_types_list = []
    for blog_type in blog_types:
        blog_type.count = Blog.objects.filter(blog_type=blog_type).count()
        blog_types_list.append(blog_type)
    '''
    # 获取日期对应的数量
    # blog_dates = Blog.objects.dates('last_update_time', 'month', order='DESC').annotate(
    #     blog_count=Count('last_update_time'))
    blog_dates_dict = {}
    blog_dates = Blog.objects.dates('last_update_time', 'month', order='DESC')
    blog_dates_dict = {}
    for blog_date in blog_dates:
        blog_count = Blog.objects.filter(last_update_time__year=blog_date.year,
                                         last_update_time__month=blog_date.month).count()
        blog_dates_dict[blog_date] = blog_count
    context = {"page_of_blogs": page_of_blogs,
               "blog_types": blog_types,
               'page_range': page_range,
               'blog_dates': blog_dates_dict, }
    return context


# Create your views here.
def blog_list(request):
    blogs_all_list = Blog.objects.all()
    context = get_blog_list_common_data(request, blogs_all_list)
    return render_to_response("blog/blog_list.html", context=context)


def blog_detail_type_name(request, blog_type_id):
    blog_type = get_object_or_404(Blog_Type, pk=blog_type_id)

    blogs_all_list = Blog.objects.filter(blog_type=blog_type)
    context = get_blog_list_common_data(request, blogs_all_list)
    context["blog_type"] = blog_type

    return render_to_response("blog/blog_detail_type_name.html", context=context)


def blog_with_date(request, year, month):
    blogs_all_list = Blog.objects.filter(last_update_time__year=year, last_update_time__month=month)
    context = get_blog_list_common_data(request, blogs_all_list)
    context['blogs_with_date'] = f'{year}年{month}月'

    return render_to_response("blog/blog_with_date.html", context=context)


def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    key = read_statistics_once_read(request,blog)

    next_blog = Blog.objects.filter(last_update_time__gt=blog.last_update_time).last()
    previous_blog = Blog.objects.filter(last_update_time__lt=blog.last_update_time).first()
    context = {"blog": blog,
               "next_blog": next_blog,
               "previous_blog": previous_blog}
    response = render_to_response("blog/blog_detail.html", context=context)
    response.set_cookie(key, 'true', max_age=24 * 3600 * 7)
    return response
