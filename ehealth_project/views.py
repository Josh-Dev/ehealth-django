from django.shortcuts import render

from ehealth_project.models import UserProfile
#from ehealth_project.forms import UserFinderForm

def register(request):
    render(request,'ehealth_projects/base.html', {})

def advanced_search(request):
    render(request,'ehealth_projects/base.html', {})

def search(request):
    context_dict = {}
    render(request, 'ehealth_project/search.html',context_dict)

