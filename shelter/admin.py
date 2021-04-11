from django.contrib import admin
from .models import *
# Register your models here.
class AnimalAdmin(admin.ModelAdmin):
	list_display = ('name', 'breed', 'found', 'photo', 'description', 'atype',)
admin.site.register(Animal, AnimalAdmin)