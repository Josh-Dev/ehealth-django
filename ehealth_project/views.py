from django.shortcuts import render
from django.contrib.auth.models import User
from ehealth_project.models import UserProfile
from ehealth_project.forms import UserForm,UserProfileForm,UserFinderForm
from ehealth_project.medLine_search import run_queryMed
from ehealth_project.healthFinder_search import run_queryHF
from ehealth_project.bing_Search import run_query
from django.http import HttpResponseRedirect, HttpResponse
import random

def saved_pages(request):
    return render(request,'ehealth_project/base.html', {})

def manage_account(request):
    return render(request,'ehealth_project/base.html', {})

def user_finder(request):
    qd = request.GET
    users = User.objects.all().order_by('-username')[:-1]
    query_string = None

    if u'search_bar' in qd:
        query_string = str(qd[u'search_bar']).strip()

        users = users.filter(username__contains = query_string)



    return render(request,'ehealth_project/user_finder.html', {'users': users})



def searchBing(request):

    result_list = []

    if request.method == 'POST':
        query = request.POST['query'].strip()

        if query:
            # Run our Bing function to get the results list!
            result_list = run_query(query)

    #return render(request, 'ehealth_project/search.html', {'result_list': result_list})

def searchHealthFinder(request):

    result_list = []

    if request.method == 'POST':
        query = request.POST['query'].strip()

        if query:
            # Run our Bing function to get the results list!
            result_list = run_queryHF(query)

    #return render(request, 'ehealth_project/search.html', {'result_list': result_list})

def searchMedLine(request):

    result_list = []

    if request.method == 'POST':
        query = request.POST['query'].strip()

        if query:
            # Run our medLine function to get the results list!
            result_list = run_queryMed(query)

    #return render(request, 'ehealth_project/search.html', {'result_list': result_list})

def searchAll(request):
    result_list = []

    if request.method == 'POST':
        query = request.POST['searchTerms'].strip()
        if query:
            results_Bing = run_query(query)
            results_HF = run_queryHF(query)
            results_Med = run_queryMed(query)
            result_list.extend(results_Bing)
            result_list.extend(results_HF)
            result_list.extend(results_Med)
    random.shuffle(result_list,random.random)
    return render(request,'ehealth_project/search.html',{'result_list':result_list})

def register(request):
    registered = False


    if request.method == 'POST':

        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        
        if user_form.is_valid() and profile_form.is_valid():
            
            user = user_form.save()

            
            user.set_password(user.password)
            user.save()

            
            profile = profile_form.save(commit=False)
            profile.user = user

         
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

           
            profile.save()

           
            registered = True

        
        else:
            print user_form.errors, profile_form.errors


    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

   
    return render(request,
            'ehealth_project/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )


def advanced_search(request):
    return render(request,'ehealth_project/base.html', {})

def basic_search(request):
    context_dict = {}
    return render(request, 'ehealth_project/search.html',context_dict)

def about(request):
    context_dict = {}
    return render(request, 'ehealth_project/search.html',context_dict)

def how(request):
    context_dict = {}
    return render(request, 'ehealth_project/search.html',context_dict)
