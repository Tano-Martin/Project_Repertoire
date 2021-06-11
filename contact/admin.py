from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe

# Register your models here.

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
	list_display = ('view_photo', 'nom', 'prenom', 'email', 'telephone', 'date_add', 'date_update', 'status')
	date_hierarchy = 'date_add'
	list_per_page = 10
	list_editable = ['email', 'telephone', 'status']

	def view_photo(self, obj):
		return mark_safe(f'<img src="{obj.photo.url}" style="height:80px; width:130px">')
	view_photo.short_description = 'Apercu des images view_photo'
