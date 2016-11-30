from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

import re

projects_by_path = {
  'powerlines-landscraped': {
    'title': "power lines: land, scraped",
    'desc': "an investigation of the role of power lines in the creation of landscapes",
    'url': "powerlines-landscraped",
    'images': [
      {
        'url': "http://lanebarlow.s3.amazonaws.com/_MG_4785.jpg",
        'title': "morning on the ridge",
        'desc': 'inkjet on paper'
      },
      {
        'url': "http://lanebarlow.s3.amazonaws.com/_MG_4957.jpg",
        'title': "recent developments",
        'desc': 'inkjet on paper'
      },
      {
        'url': "http://lanebarlow.s3.amazonaws.com/_MG_3916.jpg",
        'title': "obelisk",
        'desc': 'inkjet on paper'
      },
      {
        'url': "http://lanebarlow.s3.amazonaws.com/_MG_4725.jpg",
        'title': "reprieve",
        'desc': 'inkjet on paper'
      }
    ]
  },

  'powerlines-sketches': {
    'title': "Power Lines: Sketches",
    'desc': "line drawings on the sky",
    'url': 'powerlines-sketches',
    'images': [
      {
        'url': "http://lanebarlow.s3.amazonaws.com/_MG_2507.jpg",
        'title': "untitled (1)",
        'desc': 'inkjet on paper'
      },
      {
        'url': "http://lanebarlow.s3.amazonaws.com/_MG_4052.jpg",
        'title': "untitled (2)",
        'desc': 'inkjet on paper'
      },
      {
        'url': "http://lanebarlow.s3.amazonaws.com/_MG_2519.jpg",
        'title': "torn",
        'desc': 'inkjet on paper'
      },
      {
        'url': "http://lanebarlow.s3.amazonaws.com/_MG_4559.jpg",
        'title': "untitled (3)",
        'desc': 'inkjet on paper'
      },
      {
        'url': "http://lanebarlow.s3.amazonaws.com/_MG_4237.jpg",
        'title': "untitled (4)",
        'desc': 'inkjet on paper'
      }
    ]
  }
}

def index(request):
  template = loader.get_template('cvsite/proj-index.html')

  context = {
    'page_name': "photography",
    'projects': projects_by_path.values
  }
  return HttpResponse(template.render(context, request))

def project(request):
  template = loader.get_template('photography/photo-project.html')

  project_path = re.search('/photography/(.*)', request.path).group(1)
  project = projects_by_path[project_path]

  context = {
    'project_name': project['title'],
    'images': project['images'],
    'photo_height': 624,
    'photo_width': 926
  }
  return HttpResponse(template.render(context, request))