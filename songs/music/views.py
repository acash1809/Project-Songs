from django.shortcuts import render,get_object_or_404

from .models import Musics,Genre
from django.contrib.auth.decorators import login_required

@login_required
def genre_list(request,genre_slug=None):
	genre=None
	genres=Genre.objects.all()
	musics=Musics.objects.all()
	if genre_slug:
		genre=get_object_or_404(Genre,slug=genre_slug)
		musics=musics.filter(genre=genre)
	context={
		'genre':genre,
		'genres':genres,
		'musics':musics
		}
	return render(request,'home.html',context)



def music_detail(request,id,slug):
	music = get_object_or_404(Musics,id=id,slug=slug)
	

	return render(request,
		'home.html',
		{'music':music})


	