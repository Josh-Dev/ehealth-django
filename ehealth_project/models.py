from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class UserProfile(models.Model):
	# user that the profile belongs to
	user = models.OneToOneField(User)
	# date of birth of User
	
	age = models.IntegerField(default=18)
	# Gender of the user
	gender = models.CharField(max_length=128)
	#Image for the profile ( avatar )
	pic = models.ImageField(upload_to='/static/',default='/static/images/blank.jpg')
	def __unicode__(self):
		return self.user.username
		
class Folder(models.Model):
	# User folder belongs to
	user = models.ForeignKey(UserProfile)
	# name of the folder
	name = models.CharField(max_length=128)
	#slug of the folder
	slug = models.SlugField()
	# status of the privacy of the folder
	privacy = models.BooleanField(default=False)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Folder, self).save(*args, **kwargs)

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
	readability_score = models.FloatField(default=0)
	objectivity_score = models.FloatField(default=0)
	sentimentality_score = models.FloatField(default=0)
	def __unicode__(self):
		return self.title

