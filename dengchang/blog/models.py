
# from django.db import models

# Create your models here.
import datetime
#第二次
# from django.db import models
from django.utils import timezone
# 第一次
from django.db import models

class Auth(models.Model):
    ''' 作者 '''
    username = models.CharField(max_length=30, verbose_name='用户')
    password = models.CharField(max_length=40, verbose_name='密码')

    def __str__(self):
        return self.username

class Article(models.Model):
    """ 文章 """
    title = models.CharField(max_length=300, verbose_name='标题')
    content = models.TextField(default='', verbose_name='内容')
    pub_date = models.DateTimeField('发布时间')
    author = models.ForeignKey(Auth, on_delete=models.CASCADE, verbose_name='作者')

    def __str__(self):
        return self.title

    def is_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=3)

class Comment(models.Model):
    ''' 评论模板 '''
    reviewer = models.CharField(max_length=30, verbose_name='评论者')
    content = models.CharField(max_length=1000, verbose_name='内容')
    cmt_date = models.DateTimeField('评论时间')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='文章')

    def __str__(self):
        return self.content
        