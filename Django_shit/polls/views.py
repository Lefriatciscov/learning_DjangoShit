import re
from django.shortcuts import render 
from django.template import loader
from django.http import HttpResponse



def index (request):
   template= loader.get_template("index.html")
   return HttpResponse(template.render(request=request))

def inicio (request):
   template= loader.get_template("inicio.html")
   return HttpResponse(template.render(request=request))