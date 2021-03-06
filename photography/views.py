from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

import re

PHOTO_DOMAIN="http://lanebarlow.s3.amazonaws.com/photography"

projects_by_path = {
  'powerlines-landscraped': {
    'title': "power lines: land, scraped",
    'desc': "inspired in significant part by phel steinmetz's 'landscrapes', this sequence investigates the role of power lines in the creation and destruction of landscapes",
    'url': "powerlines-landscraped",
    'bucket': "powerlines-landscraped",
    'photo_width': 926,
    'photo_height': 624,
    'images': [
      {
        'file': "_MG_4786.jpg",
        'title': "the ridge",
        'desc': 'inkjet on paper'
      },
      {
        'file': "_MG_4957.jpg",
        'title': "recent developments",
        'desc': 'inkjet on paper'
      },
      {
        'file': "_MG_5101.jpg",
        'title': "grove",
        'desc': "inkjet on paper"
      },
      {
        'file': "_MG_3917.jpg",
        'title': "obelisk",
        'desc': 'inkjet on paper'
      },
      {
        'file': "_MG_4363.jpg",
        'title': "road trip",
        'desc': "inkjet on paper"
      },
      {
        'file': "_MG_5062.jpg",
        'title': "sinew",
        "desc": 'inkjet on paper'
      },
      {
        'file': "_MG_4726.jpg",
        'title': "reprieve",
        'desc': 'inkjet on paper'
      }
    ]
  },

  'powerlines-sketches': {
    'title': "power lines: sketches",
    'desc': "a reduction of power lines to silhouette line drawings against dynamic canvases",
    'url': 'powerlines-sketches',
    'bucket': "powerlines-sketches",
    'photo_width': 624,
    'photo_height': 624,
    'images': [
      {
        'file': "_MG_2507.jpg",
        'title': "untitled (1)",
        'desc': 'inkjet on paper'
      },
      {
        'file': "_MG_4558.jpg",
        'title': "untitled (2)",
        'desc': 'inkjet on paper'
      },
      {
        'file': "_MG_2521.jpg",
        'title': "torn",
        'desc': 'inkjet on paper'
      },
      {
        'file': "_MG_4055.jpg",
        'title': "untitled (3)",
        'desc': 'inkjet on paper'
      },
      {
        'file': "_MG_4237.jpg",
        'title': "untitled (4)",
        'desc': 'inkjet on paper'
      },
      {
        'file': "_MG_4444.jpg",
        'title': "untitled (5)",
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
    'bucket_url': PHOTO_DOMAIN + '/' + project['bucket'],
    'project_name': project['title'],
    'images': project['images'],
    'photo_height': project['photo_height'],
    'photo_width': project['photo_width']
  }
  return HttpResponse(template.render(context, request))
