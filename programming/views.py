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
        'desc': "this shit solves those plynml cngrncs"
      }
    ]
  }
  return HttpResponse(template.render(context, request))