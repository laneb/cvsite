from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

def index(request):
  return HttpResponse("look at my Power Lines project - it's right <a href=\"powerlines\">here</a>")

def project(request):
  template = loader.get_template('photography/project.html')
  context = {
    'project_name': 'Power Lines',
    'images': [
      "http://lanebarlow.s3.amazonaws.com/_MG_0998.jpg",
      "http://lanebarlow.s3.amazonaws.com/_MG_1001.jpg",
      "http://lanebarlow.s3.amazonaws.com/_MG_2154.jpg"
    ]
  }
  return HttpResponse(template.render(context, request))