from django.shortcuts import render, render_to_response, get_object_or_404
from django.shortcuts import HttpResponse, Http404
from .models import Article


# Create your views here.
def article_detail(request, article_id):
    # try:
    #     obj = Article.objects.get(pk=article_id)
    #     context = {
    #         "obj":obj
    #     }
    #     # return render(request,'article_detail.html',context=context)
    #     return render_to_response('article_detail.html',context=context)
    # except Article.DoesNotExist:
    #     raise Http404('不存在')
    # return HttpResponse(f'<h2>文章标题:{obj.title}</h2>,<br>文章内容:{obj.content}')
    obj = get_object_or_404(Article, pk=article_id)

    context = {
        "obj": obj
    }
    return render_to_response('article_detail.html', context=context)

def article_list(request):
    articles = Article.objects.filter(is_deleted=False)
    context={
        "articles": articles
    }
    return render_to_response('article_list.html', context=context)

