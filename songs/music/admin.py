from django.contrib import admin

# Register your models here.

from .models import Musics,Genre


class GenreAdmin(admin.ModelAdmin):
	list_display=['name','slug']
	prepopulated_fields={'slug':('name',)}#   ------------->  to automatically fill the field slug



class MusicAdmin(admin.ModelAdmin):
	list_display=['name','slug','genre','created','updated']
	list_filter=['created','updated','genre']
	list_editable=['genre']
	prepopulated_fields={'slug':('name',)}


admin.site.register(Genre,GenreAdmin)
admin.site.register(Musics,MusicAdmin)
