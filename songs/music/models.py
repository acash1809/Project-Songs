from django.db import models

from django.urls import reverse #importing reverse
# Create your models here.

###############for genre in admin#############

class Genre(models.Model):
	name=models.CharField(max_length=200, db_index=True) #db_index is used for faster processing but uniqueness of a value is must.
	slug=models.SlugField(max_length=200, db_index=True, unique=True)


	class Meta:
		ordering = ('name',)
		verbose_name='Genre'
		verbose_name_plural='Genres'

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('genre_list_by_category',args=[self.slug])


########################FOR music In admin########################

class Musics(models.Model):
	genre=models.ForeignKey(Genre,related_name='music',on_delete=models.CASCADE)
	name=models.CharField(max_length=200, db_index=True)
	slug=models.SlugField(max_length=200, db_index=True, unique=True)
	image=models.ImageField(upload_to='songs', blank=True)
	description = models.TextField(blank=True)
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)
	audiofile= models.FileField(upload_to='static',blank=True)
	

	class Meta:
		ordering=('-created',)
		index_together=(('id','slug'),)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('music_detail',args=[self.id,self.slug])