from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('blog_type/<int:blog_type_id>/', views.blog_detail_type_name, name='blog_detail_type_name'),
    path('date/<int:year>/<int:month>/', views.blog_with_date, name='blog_with_date'),
]
