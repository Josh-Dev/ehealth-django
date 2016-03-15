import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ehealth.settings')

import django
django.setup()

from ehealth_project.models import Folder, Page, UserProfile
from django.contrib.auth.models import User

generic_user = User.objects.get_or_create(username="John", password="1234", email="Gdgsadfa@fdafds.com",is_superuser=False, is_staff=False)[0]
generic_user_profile = UserProfile.objects.get_or_create(user=generic_user,dob="2012-03-09", address_1 = "123 fakestreet",address_2="", city="City", post_code= "GR8 M8", gender="human")[0]

def populate():

	test_cat_1 = add_cat(user= generic_user_profile,name="TEST_CAT_1",privacy=True)
	
	add_page(folder=test_cat_1,title="page_1",url="www.google.com",source="bing.com",summary="blahblahblah",readability_score=57,objectivity_score=45,sentimentality_score=65)
	
	add_page(folder=test_cat_1,title="page_2",url="www.google.com",source="bing.com",summary="blahblahblah",readability_score=14,objectivity_score=24,sentimentality_score=13)
	
	add_page(folder=test_cat_1,title="page_3",url="www.google.com",source="bing.com",summary="blahblahblah",readability_score=15,objectivity_score=54,sentimentality_score=87)
	
	test_cat_2 = add_cat(generic_user_profile,"TEST_CAT_2",False)
	
	add_page(folder=test_cat_2,title="page_1",url="www.google.com",source="bing.com",summary="blahblahblah",readability_score=43,objectivity_score=54,sentimentality_score=76)
	
	add_page(folder=test_cat_2,title="page_2",url="www.google.com",source="bing.com",summary="blahblahblah",readability_score=54,objectivity_score=23,sentimentality_score=42)
	
	add_page(folder=test_cat_2,title="page_3",url="www.google.com",source="bing.com",summary="blahblahblah",readability_score=42,objectivity_score=54,sentimentality_score=24)
	
	test_cat_3 = add_cat(generic_user_profile,"TEST_CAT_3",False)
	
	add_page(folder=test_cat_2,title="page_1",url="www.google.com",source="bing.com",summary="blahblahblah",readability_score=34,objectivity_score=25,sentimentality_score=78)
	
	add_page(folder=test_cat_2,title="page_2",url="www.google.com",source="bing.com",summary="blahblahblah",readability_score=87,objectivity_score=78,sentimentality_score=98)
	
    # Print out what we have added to the user.
	for f in Folder.objects.all():
		for p in Page.objects.filter(folder=f):
			print "- {0} - {1}".format(str(f), str(p))

def add_page(folder, title, url, source, summary, readability_score, objectivity_score,sentimentality_score):
	p = Page.objects.get_or_create(title=title,folder=folder, url=url,source=source,summary=summary,readability_score=readability_score,objectivity_score=objectivity_score,sentimentality_score=sentimentality_score)[0]
	p.save()
	return p

def add_cat(user,name,privacy):
	print user, name
	f = Folder.objects.get_or_create(user = user,name=name)[0]
	f.privacy = privacy
	f.save()
	return f

# Start execution here!
if __name__ == '__main__':
	print "Starting Rango population script..."
	populate()