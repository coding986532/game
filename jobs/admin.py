from django.contrib import admin
from .models import Joblisting
# Register your models here.

class JoblistingAdmin(admin.ModelAdmin):
    list_display = ('Title') 

admin.site.register(Joblisting, JoblistingAdmin)