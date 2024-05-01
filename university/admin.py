from django.contrib import admin
from . models import Programs

class Uni_ListingAdmin(admin.ModelAdmin):
    list_display = ('University', 'Program', 'tuition', )
# Register your models here.
admin.site.register(Programs, Uni_ListingAdmin)