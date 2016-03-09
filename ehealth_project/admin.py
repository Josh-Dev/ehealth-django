from django.contrib import admin
from ehealth_project.models import Folder, UserProfile, Page

# Register your models here.
admin.site.register(Folder)
admin.site.register(Page)
admin.site.register(UserProfile)