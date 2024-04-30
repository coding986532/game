from django.contrib import admin

# Register your models here.

class JoblistingAdmin(admin.ModelAdmin):
    list_display = ('Title')