from django.shortcuts import render_to_response, get_object_or_404
from .models import Blog, Blog_Type
from django.core.paginator import Paginator
from django.conf import settings


# Create your views here.
def blog_list(request):
    blogs_all_list = Blog.objects.all()
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
    blog_types = Blog_Type.objects.all()
    context = {"page_of_blogs": page_of_blogs,
               "blog_types": blog_types,
               'page_range': page_range}
    return render_to_response("blog/blog_list.html", context=context)


def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    context = {"blog": blog}
    return render_to_response("blog/blog_detail.html", context=context)


def blog_detail_type_name(request, blog_type_id):
    blog_type = get_object_or_404(Blog_Type, pk=blog_type_id)

    blogs_all_list = Blog.objects.filter(blog_type=blog_type)
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
    blog_types = Blog_Type.objects.all()
    context = {"page_of_blogs": page_of_blogs,
               "blog_types": blog_types,
               "blog_type": blog_type,
               'page_range': page_range}

    return render_to_response("blog/blog_detail_type_name.html", context=context)
