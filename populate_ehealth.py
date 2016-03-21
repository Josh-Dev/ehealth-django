import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ehealth.settings')

import django
django.setup()

from ehealth_project.models import Folder, Page, UserProfile
from django.contrib.auth.models import User

def populate():

	generic_user = User.objects.get_or_create(username="John", password="1234", email="john@email.com",is_superuser=False, is_staff=False)[0]
	generic_user_profile = UserProfile.objects.get_or_create(user=generic_user,dob="2012-03-09", address_1 = "123 fakestreet",address_2="", city="City", post_code= "GR8 M8", gender="human")[0]

	test_cat_1 = add_cat(generic_user_profile,"diabetes",True)
	
	add_page(folder=test_cat_1,title="American Diabetes Association",url="http://www.diabetes.org/",source="Bing",summary="Our Mission:  To prevent and cure diabetes and to improve the lives of all people affected by diabetes."
			 ,readability_score=57,objectivity_score=45,sentimentality_score=65)
	
	add_page(folder=test_cat_1,title="Webmd diabetes",url="http://www.webmd.com/diabetes/",source="Medline",summary="blahblahblah",
			 readability_score=14,objectivity_score=24,sentimentality_score=13)
	
	add_page(folder=test_cat_1,title="Medical news today",url="http://www.medicalnewstoday.com/info/diabetes/",source="Bing",summary="blahblahblah",
			 readability_score=15,objectivity_score=54,sentimentality_score=87)
	
	test_cat_2 = add_cat(generic_user_profile,"cancer",False)
	
	add_page(folder=test_cat_2,title="Comprehensive Cancer Information - National Cancer Institute",url="http://www.cancer.gov/",source="HealthFinder",summary="blahblahblah",
			 readability_score=43,objectivity_score=54,sentimentality_score=76)
	
	add_page(folder=test_cat_2,title="American Cancer Society",url="http://www.cancer.org/",source="Bing",summary="blahblahblah",
			 readability_score=54,objectivity_score=23,sentimentality_score=42)
	
	add_page(folder=test_cat_2,title="Webmd cancer",url="http://www.webmd.com/cancer/",source="Medline",summary="blahblahblah",
			 readability_score=42,objectivity_score=54,sentimentality_score=24)
	
	test_cat_3 = add_cat(generic_user_profile,"Heart Disease",False)
	
	add_page(folder=test_cat_3,title="Mayo Clinic",url="http://www.mayoclinic.org/diseases-conditions/heart-disease/basics/definition/con-20034056",source="HealthFinder",
			 summary="blahblahblah",readability_score=34,objectivity_score=25,sentimentality_score=78)
	
	add_page(folder=test_cat_3,title="American Heart Association",url="http://www.heart.org/HEARTORG/Caregiver/Resources/WhatisCardiovascularDisease/What-is-Cardiovascular-Disease_UCM_301852_Article.jsp",source="Bing",summary="blahblahblah",
			 readability_score=87,objectivity_score=78,sentimentality_score=98)
	
    # Print out what we have added to the user.
	for f in Folder.objects.all():
		for p in Page.objects.filter(folder=f):
			print "- {0} - {1}".format(str(f), str(p))

	add_user(username="Jeffery", password="4321", email="jj@email.com",dob="1980-05-12", add_1 = "123 Fake Avenue",add_2="Fakeshire", city="Fakeville", post_code= "G14 2FH", gender="Female")

	add_user(username="Geoff", password="4235", email="gg@email.com",dob="1987-05-12", add_1 = "123 Fake Lane",add_2="Fakeshire", city="Fakeville", post_code= "G16 2FD", gender="Male")

	add_user(username="Sam", password="4321", email="sam@email.com",dob="1980-05-12", add_1 = "123 Fake Road",add_2="Fakeshire", city="Fakeshire", post_code= "G11 2ER", gender="Male")

	add_user(username="Fred", password="7455", email="fred@email.com",dob="1987-11-02", add_1 = "123 Fake Street",add_2="Fakeshire", city="Faketown", post_code= "G12 2FJ", gender="Female")

	for u in UserProfile.objects.all():
		print "-{0}".format(str(u))

def add_user(username, password, email, dob, add_1, add_2, city, post_code, gender):
	u = User.objects.get_or_create(username=username,password=password, email=email, is_superuser=False, is_staff=False)[0]
	up = UserProfile.objects.get_or_create(user=u,dob=dob,address_1=add_1,address_2=add_2,city=city,post_code=post_code, gender=gender)[0]
	up.save()
	return up

def add_page(folder, title, url, source, summary, readability_score, objectivity_score,sentimentality_score):
	p = Page.objects.get_or_create(title=title,folder=folder, url=url,source=source,summary=summary,readability_score=readability_score,objectivity_score=objectivity_score,sentimentality_score=sentimentality_score)[0]
	p.save()
	return p

def add_cat(user,name,privacy):
	f = Folder.objects.get_or_create(user = user,name=name)[0]
	f.privacy = privacy
	f.save()
	return f

# Start execution here!
if __name__ == '__main__':
	print "Starting Rango population script..."
	populate()