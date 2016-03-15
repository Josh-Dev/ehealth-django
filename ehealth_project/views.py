from django.shortcuts import render


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print user_form.errors
    else:
        user_form = UserForm()
    return render(request,
            'ehealth/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )

def advanced_search(request):
    return render(request,'ehealth_projects/base.html', {})

def search(request):
    context_dict = {}
    return render(request, 'ehealth_project/search.html',context_dict)

