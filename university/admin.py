from django.contrib import admin
from . models import Uni_Listing

class Uni_ListingAdmin(admin.ModelAdmin):
    list_display = ('University', 'Program', 'tuition', )
# Register your models here.
admin.site.register(Uni_Listing, Uni_ListingAdmin)
