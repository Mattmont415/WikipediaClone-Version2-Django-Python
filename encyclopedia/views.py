from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from markdown2 import Markdown
from django.urls import reverse
from django import forms

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
  if theEntry is None:
    return render(request, "encyclopedia/noentry.html", {
      "entryTitle": title})
  else: 
    return render(request, "encyclopedia/index.html", {
      "title": markdowner.convert(theEntry),
      "entryTitle": title
  })

# def search(request):
#   value = request.GET.get('q','')


