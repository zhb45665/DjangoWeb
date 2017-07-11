"""
Definition of views.
"""
#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpRequest
from datetime import datetime
from app.models import BlogPost
from django.http import Http404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib.syndication.views import Feed

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    postlist = BlogPost.objects.all()
    return render(
        request,
        'app/index.html',
        {   
            'title':'首页',
            'year':datetime.now().year,
            'postlist':postlist
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def demo(request):
    """Renders the demo page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/demo.html',
        {
            'title':'Demo',
            'message':'this is Demo page.',
            'year':datetime.now().year,
        }
    )
def content(request):
    """Renders the demo page."""
    assert isinstance(request, HttpRequest)
    posts = BlogPost.objects.all()
    paginator = Paginator(posts,3)
    page = request.GET.get('page')
    try:
        postlist = paginator.page(page)
    except PageNotAnInteger:
        postlist = paginator.page(1)
    except EmptyPage:
        postlist = paginator.page(paginator.num_pages)
    #try:
    #    postlist = BlogPost.objects.get(id=str(id))
    #except:
    #    raise Http404
    return render(
        request,
        'app/content.html',
        {
            'title':'随记',
            'postlist':postlist,
        }
    )

def detail(request,id):
    try:
        post = BlogPost.objects.get(id=str(id))
    except:
        raise Http404
    return render(
        request,
        'app/post.html',
        {
            'title':'博文',
            'post':post,
            }
        )

class RSSFeed(Feed):
    title = "RSS Feed"
    link = "http://zhb45665.cn/"
    description = "RSS Feed"
    def items(self):
        return BlogPost.objects.order_by('-timestamp')
    def item_title(self,item):
        return item.title
    def item_pubdate(self,item):
        return item.timestamp
    def item_description(self,item):
        return item.body
    def item_link(self,item):
        return item.get_absolute_url()
