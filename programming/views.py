from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

def index(request):
  template = loader.get_template('cvsite/proj-index.html')
  context = {
    'page_name': "programming",
    'projects': [
      {
        'title': "congruence solver",
        'url': "http://github.com/laneb/congruence_solver",
        'desc': "a C library and a ruby cli for solving polynomial congruences, a topic from elementary number theory"
      },
      {
        'title': "spark modularized view (smv)",
        'url': "http://github.com/tresamigossd/smv",
        'desc': "an extension of the spark big data framework that facilitates scalability, modularity, and rapid development of small and large applications"
      },
      {
        'title': "this website",
        'url': "http://github.com/laneb/cvsite",
        'desc': "the Django application that powers this site"
      }
    ]
  }
  return HttpResponse(template.render(context, request))