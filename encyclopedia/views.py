from django.shortcuts import render
from django.http import HttpResponse
from markdown2 import Markdown

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", { 
        "entries": util.list_entries()
    })
  
# def link(request, name):
#     return render(request, f"entries/{name}.md")

def entry(request, title):
  theEntry = util.get_entry(title)
  markdowner = Markdown()
  return render(request, "encyclopedia/index.html", {
    "title": markdowner.convert(theEntry)
  })



