from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

def index(request):
  template = loader.get_template('photography/index.html')
  context = {
    'projects': [
      {
        'title': "Power Lines: Land Scraped",
        'url': "powerlines-landscraped",
        'desc': "pwrln mfn lndscps"
      },

      {
        'title': "Power Lines: Sketches",
        'url': "powerlines-sketches",
        'desc': "sum dang pwrln slhtts"
      }
    ]
  }
  return HttpResponse(template.render(context, request))

def project(request):
  template = loader.get_template('photography/project.html')
  context = {
    'project_name': 'Power Lines',
    'images': [
      {
        'url': "http://lanebarlow.s3.amazonaws.com/_MG_0998.jpg",
        'title': "pwrln1",
        'desc': 'archival inkjet on canvas'
      },
      {
        'url': "http://lanebarlow.s3.amazonaws.com/_MG_1001.jpg",
        'title': "pwrln2"
      },
      {
        'url': "http://lanebarlow.s3.amazonaws.com/_MG_2154.jpg",
        'title': "pwrln3"
      }
    ],
    'photo_height': 624,
    'photo_width': 926
  }
  return HttpResponse(template.render(context, request))