from django.shortcuts import render

from ehealth_project.models import UserProfile
#from ehealth_project.forms import UserFinderForm

def register(request):
    return render(request,'ehealth_projects/base.html', {})

def advanced_search(request):
    return render(request,'ehealth_projects/base.html', {})

def search(request):
    context_dict = {}
    return render(request, 'ehealth_project/search.html',context_dict)

