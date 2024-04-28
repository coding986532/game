from django.contrib import admin

# Register your models here.

from .models import Listing, Transaction
class ListingAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'Owner', 'property_type','city','territory', 'zip']

admin.site.register(Listing, ListingAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ['Property', 'Buyer', 'Method', 'price', 'Complete']

admin.site.register(Transaction, TransactionAdmin)