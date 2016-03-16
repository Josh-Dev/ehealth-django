from django.shortcuts import render
from ehealth_project.models import UserProfile
from ehealth_project.forms import UserForm,UserProfileForm

def saved_pages(request):
    return render(request,'ehealth_projects/base.html', {})

def manage_account(request):
    return render(request,'ehealth_projects/base.html', {})

def user_finder(request):

    all_users = UserProfile.objects.all()
    context_dict={'users':all_users}

    if request.method == 'POST':

        user_finder_form = UserFinderForm(data=request.POST)
        if user_finder_form.is_valid():
            #The username input to search through current users
            search_username = user_finder_form.save()

        else:
            print user_finder_form.errors

    else:
        user_finder_form = UserFinderForm()

    return render(request,'ehealth_project/user_finder.html',context_dict)

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
    return render(request,'ehealth_projects/base.html', {})

def basic_search(request):
    context_dict = {}
    return render(request, 'ehealth_project/search.html',context_dict)

def about(request):
    context_dict = {}
    return render(request, 'ehealth_project/search.html',context_dict)

def how(request):
    context_dict = {}
    return render(request, 'ehealth_project/search.html',context_dict)