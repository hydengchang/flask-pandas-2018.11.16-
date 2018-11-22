from django.urls import path
from . import views

# 添加应用命名空间Url
app_name = 'blog'
# 路由
# urlpatterns = [
#     # path('a', views.index, name='index'),
#     path('', views.index, name='index'),
#     path('<int:article_id>', views.blog_detil, name='blog_detil'),
#     path('auth/<int:auth_id>', views.auth_introduce, name='auth_introduce'),
#     path('auth/<int:auth_id>/blogs', views.auth_blogs, name='auth_blogs'),
#     path('bbt', views.bbt, name='bbt_blog'),
#     path('save', views.save, name='save_blog'),

# ]
# URLcof修改2
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>', views.DetailView.as_view(), name='blog_detil'),
    path('auth/<int:pk>', views.AuthorIntroduceView.as_view(), name='auth_introduce'),
    path('auth/<int:pk>/blogs', views.AuthorBlogsView.as_view(), name='auth_blogs'),
    path('bbt', views.bbt, name='bbt_blog'),
    path('save', views.save, name='save_blog'),

]