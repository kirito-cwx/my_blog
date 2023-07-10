from django.shortcuts import render_to_response, get_object_or_404
from .models import Blog, Blog_Type


# Create your views here.
def blog_list(request):
    blogs = Blog.objects.all()
    blog_types = Blog_Type.objects.all()
    context = {"blogs": blogs,
               "blog_types": blog_types}
    return render_to_response("blog/blog_list.html", context=context)


def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    context = {"blog": blog}
    return render_to_response("blog/blog_detail.html", context=context)


def blog_detail_type_name(request, blog_type_id):
    blog_type = get_object_or_404(Blog_Type, pk=blog_type_id)
    blog_types = Blog_Type.objects.all()
    blogs = Blog.objects.filter(blog_type=blog_type)
    context = {"blogs": blogs,
               "blog_type": blog_type,
               "blog_types": blog_types}

    return render_to_response("blog/blog_detail_type_name.html", context=context)
