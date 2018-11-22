from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.
from django.http import Http404
from .models import Article
from .models import Auth
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
# 修改urlconf 
from django.views import generic

# 
class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_article_list'
    def get_queryset(self):
        return Article.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Article
    template_name = 'blog/detail.html'
    
class AuthorIntroduceView(generic.DetailView):
    model = Auth
    template_name = 'blog/introduce.html'

class AuthorBlogsView(generic.ListView):
    template_name = 'blog/blogs.html'
    context_object_name = 'auth_article_list'
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Article.objects.filter(author__id=pk)
        
def bbt(request):
    context = {}
    return render(request, 'blog/bbt.html', context)
def save(request):
    try:
        title = request.POST['title']
        content = request.POST['content']
        author = Auth.objects.get(username='admin')
        article = Article(title=title, content=content, auth=author, pub_date=timezone.now())
        article.save()
        return HttpResponseRedirect(reverse('blog:blog_detil', args=(article.id,)))
    except KeyError:
        content = {'error_message': '好像没有参数'}
        return render(request, 'blog/bbt.html', content)
        
