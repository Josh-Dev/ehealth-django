from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	# user that the profile belongs to
	user = models.OneToOneField(User)
	# date of birth of User
	dob = models.DateField()
	age = models.IntegerField()
	# address of the user
	address_1 = models.CharField(max_length=128)
	address_2 = models.CharField(max_length=128, blank=True)
	city = models.CharField(max_length=64, default="")
	post_code = models.CharField(max_length=8)
	# Gender of the user
	gender = models.CharField(max_length=128)
	def __unicode__(self):
		return self.user.username
		
class Folder(models.Model):
	# User folder belongs to
	user = models.ForeignKey(UserProfile)
	# name of the folder
	name = models.CharField(max_length=128)
	# status of the privacy of the folder
	privacy = models.BooleanField(default=False)
	def __unicode__(self):
		return self.name

class Page(models.Model):
	# title of the Page
	title = models.CharField(max_length=128)
	# the parent folder of this page
	folder = models.ForeignKey(Folder)
	# url of the page
	url = models.URLField()
	# source used to get the page
	source = models.CharField(max_length=128)
	# short summary of the page contents
	summary = models.TextField()
	# scores used to determine how good the page is
	readability_score = models.IntegerField(default=0)
	objectivity_score = models.IntegerField(default=0)
	sentimentality_score = models.IntegerField(default=0)
	def __unicode__(self):
		return self.title

