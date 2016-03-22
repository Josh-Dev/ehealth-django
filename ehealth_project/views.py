from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from ehealth_project.models import UserProfile,Folder,Page
from ehealth_project.forms import UserForm,UserProfileForm,UserFinderForm
from ehealth_project.medLine_search import run_queryMed
from ehealth_project.healthFinder_search import run_queryHF
from ehealth_project.bing_Search import run_query
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import random
from bs4 import BeautifulSoup
import requests
from textblob import TextBlob
from textstat.textstat import textstat



def saved_pages(request):
    return render(request,'ehealth_project/base.html', {})

def manage_account(request):
    return render(request,'ehealth_project/base.html', {})

def user_profile(request,username,current_folder=None):
    # Get the user with the specified username
    user = User.objects.all().get(username=username)
    user_prof = UserProfile.objects.all().get(user=user)

    # If the user submitted a new folder name then a new folder will be made if it doesnt exist
    if request.method == 'POST':
        if u'new_folder_name' in request.POST:
            folder_name = request.POST.get('new_folder_name')
            new_folder = Folder.objects.get_or_create(user=user_prof,name=folder_name)

    #user = authenticate(username=user.username, password=user.password)
    #login(request,user)
    current_users_profile = False
    print user==request.user
    if user==request.user:
        current_users_profile = True

    current_pages=None

    # gets all the public folders from the user, and if a current folder has been selected then the current_folder is set to
    # the current_folder passed to the view.  Gets all the pages in the current_folder.
    users_public_folders = Folder.objects.all().filter(user=user_prof, privacy=False)

    if current_folder:
        current_folder = Folder.objects.all().get(slug=current_folder)
        current_pages = Page.objects.all().filter(folder=current_folder)

    context_dict={'user_prof':user_prof,'users_public_folders':users_public_folders,'current_pages':current_pages, 'current_folder':current_folder, 'current_users_profile': current_users_profile}

    return render(request,'ehealth_project/user_profile.html', context_dict)
def user_profile_form(request):
    registered = True
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)

            profile.user = user

         
            if 'pic' in request.FILES:
                profile.pic = request.FILES['pic']

           
            profile.save()
        else:
            print user_form.errors, profile_form.errors
    user_form = UserForm()
    profile_form = UserProfileForm()
    return render(request,
            'ehealth_project/user_profile_form.html',
            {'user_form':user_form,'profile_form': profile_form, 'registered': registered} )
def user_finder(request):
    qd = request.GET #gets a query dictionary
    users = User.objects.all().order_by('username')
    query_string = None

    #if the user tried to search then get the query string and find a user with a username or email matching
    #the query string
    if u'search_bar' in qd:
        query_string = str(qd[u'search_bar']).strip()
        if query_string.__contains__("@"):
            users = users.filter(email = query_string)
        else:
            users = users.filter(username__contains = query_string)
    user_profs = UserProfile.objects.all().filter(user__in=users)

    return render(request,'ehealth_project/user_finder.html', {'users': users, 'user_profs':user_profs})

def getUserFolders(user_prof):
    folder_list = []

    if Folder.objects.all().filter(user= user_prof) != []:
        folder_list = Folder.objects.all().filter(user=user_prof)

    return folder_list;

def searchAll(request):
    result_list = []
    folder_list = []

    #Execute Search
    if request.method == 'GET':
    
        query = request.GET.get('searchTerms');
        source = request.GET.get('Source');
        
        if source is None:
            source = 'All'
        
        
        if query:
            if(source == 'All' or source == 'Bing'):
                results_Bing = run_query(query)
                result_list.extend(results_Bing)
            if(source == 'All' or source == 'Healthfinder'):
                results_HF = run_queryHF(query)
                result_list.extend(results_HF)
            if(source == 'All' or source == 'Medline'):
                results_Med = run_queryMed(query)
                result_list.extend(results_Med)
            
    random.shuffle(result_list,random.random)
    if request.user.is_authenticated():
        user = request.user
        #Get user's folders
        folder_list = getUserFolders(UserProfile.objects.all().get(user=user))

    return render(request,'ehealth_project/results.html',{'result_list':result_list,'folders':folder_list, 'searchTerms': query})

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
    return render(request,'ehealth_project/advanced.html', {})

def basic_search(request):
    context_dict = {}
    return render(request, 'ehealth_project/search.html',context_dict)

def about(request):
    context_dict = {}
    return render(request, 'ehealth_project/about.html',context_dict)

def how(request):
    context_dict = {}
    return render(request, 'ehealth_project/how.html',context_dict)
from django.contrib.auth import logout


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/ehealth/')
def user_login(request):


    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')


        user = authenticate(username=username, password=password)

        if user:

            if user.is_active:

                login(request, user)
                return HttpResponseRedirect('/ehealth/')
            else:

                return HttpResponse("Your ehealth account is disabled.")
        else:

            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    else:

        return render(request, 'ehealth_project/login.html', {})


#Adds page to folder
@login_required
def save_page(request):
    #Smash through the request and get the url, desc & folder
    url = request.GET.get('url')
    desc = request.GET.get('desc')
    title = request.GET.get('title')
    folder_name = request.GET.get('folder_name')

    #Score the page using APIs
    #TO DO: (Ruxandra apis)

    r = requests.get(url)  #Open the url, read the contents then score them. Seems to be slowing down the app quite a bit.
    myfile = BeautifulSoup(r.text,"html.parser").text
    blob = TextBlob(myfile)
    scr_polarity = "{:.2f}".format( blob.sentiment.polarity)
    scr_subjectivity = "{:.2f}".format( blob.sentiment.subjectivity)
    scr_readability ="{:.2f}".format(textstat.flesch_reading_ease(myfile))

    #Save page
    user_profile = UserProfile.objects.all().get(user=request.user)
    folder = Folder.objects.all().get(name=folder_name,user=user_profile)
    P = Page.objects.get_or_create(title=title,
    url=url,summary=desc,
    readability_score=scr_readability,
    objectivity_score=scr_subjectivity,
    sentimentality_score=scr_polarity,
    folder=folder)

    #Return success/fail
    return HttpResponse('Was a success')

@login_required
def delete_folder(request, id):
    #folder_id = request.GET.get('folder_id')
    #folder_curr = request.GET.get('folder_current')
    
    #Delete
    Folder.objects.get(pk=id).delete()

    return redirect('/ehealth/user_profile/'+str(request.user))

def delete_page(request, id, current_folder):
    #page_id = request.GET.get('page_id')
    #page_curr = request.GET.get('page_current')

    #Delete
    Page.objects.get(pk=id).delete()

    return redirect('/ehealth/user_profile/'+str(request.user)+"/"+str(current_folder))
