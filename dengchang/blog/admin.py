from django.contrib import admin

# Register your models here.

from .models import Auth, Article, Comment

class AuthAdmin(admin.ModelAdmin):
    """docstring for AuthAdmin"""
    fields = ['username']
# 将提示名称行放， 而StackedInline它没有
class CommentInline(admin.TabularInline):
    model = Comment
    # 要添加几个评论区
    extra = 2

class ArticleAdmin(admin.ModelAdmin):
    """docstring for ArticleAdmin"""
    fieldsets = [
        (None, {'fields': ['title', 'content']}),
        ('附属信息', {'fields': ['author', 'pub_date']})
    ]
    # 关联文章信息
    inlines = [CommentInline]
    # 美化article，显示全部信息
    list_display = ('title', 'content', 'pub_date', 'is_published_recently')

admin.site.register(Auth, AuthAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)


        
