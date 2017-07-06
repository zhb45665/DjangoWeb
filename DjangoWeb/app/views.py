"""
Definition of views.
"""
#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from app.models import BlogPost

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
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
def user(request):
    """Renders the demo page."""
    assert isinstance(request, HttpRequest)
    postlist = BlogPost.objects.all()
    return render(
        request,
        'app/user.html',
        {
            'postlist':postlist
        }
    )