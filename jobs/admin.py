from django.contrib import admin
from .models import Jobs
# Register your models here.

class JobsAdmin(admin.ModelAdmin):
    list_display = ('Employer','Title','Salary') 

admin.site.register(Jobs, JobsAdmin)