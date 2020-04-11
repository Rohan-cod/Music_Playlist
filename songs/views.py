from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, TemplateView, DetailView
from .models import Playlist_Spotify, Playlist_Apple_Music, New_Playlist_Spotify, New_Playlist_Apple_Music, All_Playlist_Spotify, All_Playlist_Apple_Music
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.shortcuts import render
from .spotify import ToPlaylist
from .apple_music import A_ToPlaylist






class HomePageView(TemplateView):
	template_name = 'index.html'

class Spotify(LoginRequiredMixin, CreateView):
	model = Playlist_Spotify
	template_name = 'spotify.html'
	login_url = 'login'
	fields = {'playlist_name',}
	def submit(request):
		if request.method == 'POST':
			pl_name = request.POST['playlist_name']
			cp = ToPlaylist()
			cp.add_song_to_playlist(pl_name)

class Apple_Music(LoginRequiredMixin, CreateView):
	model = Playlist_Apple_Music
	template_name = 'apple_music.html'
	login_url = 'login'
	fields = {'playlist_name',}
	def submit(request):
		if request.method == 'POST':
			pl_name = request.POST['playlist_name']
			cp = A_ToPlaylist()
			cp.add_song_to_playlist(pl_name)

class All_Spotify_Playlist(LoginRequiredMixin, ListView):
	template_name = 'all_spotify.html'
	model = All_Playlist_Spotify
	paginate_by = 5
	login_url = 'login'
	
class All_Apple_Music_Playlist(LoginRequiredMixin, ListView):
	template_name = 'all_apple_music.html'
	model = All_Playlist_Apple_Music
	paginate_by = 5
	login_url = 'login'

class New_Spotify(LoginRequiredMixin, CreateView):
	model = New_Playlist_Spotify
	template_name = 'new_spotify.html'
	login_url = 'login'
	fields = {'description', 'playlist_name',}
	def submit(request):
		if request.method == 'POST':
			pl_name = request.POST['playlist_name']
			des = request.POST['description']
			cp = ToPlaylist()
			cp.create_playlist(pl_name, des)

class New_Apple_Music(LoginRequiredMixin, CreateView):
	model = New_Playlist_Apple_Music
	template_name = 'new_apple_music.html'
	login_url = 'login'
	fields = {'description', 'playlist_name',}
	def submit(request):
		if request.method == 'POST':
			pl_name=request.POST['playlist_name']
			des = request.POST['description']
			cp = A_ToPlaylist()
			cp.create_playlist(pl_name, des)


def search_apple_view(request):
	ctx = {}
	url_parameter = request.GET.get("q")

	if url_parameter:
		all_apple_music_playlist = All_Playlist_Apple_Music.objects.filter(pla_name__icontains=url_parameter)
	else:
		all_apple_music_playlist = All_Playlist_Apple_Music.objects.all()

	ctx["all_apple_music_playlist"] = all_apple_music_playlist

	if request.is_ajax():
		html = render_to_string(
			template_name="all_apple_music_playlist-results-partial.html", 
			context={"all_apple_music_playlist": all_apple_music_playlist}
		)

		data_dict = {"html_from_view": html}

		return JsonResponse(data=data_dict, safe=False)

	return render(request, "all_apple_music_playlist_search.html", context=ctx)


def search_spotify_view(request):
	ctx = {}
	url_parameter = request.GET.get("q")

	if url_parameter:
		all_spotify_playlist = All_Playlist_Spotify.objects.filter(pla_name__icontains=url_parameter)
	else:
		all_spotify_playlist = All_Playlist_Spotify.objects.all()

	ctx["all_spotify_playlist"] = all_spotify_playlist

	if request.is_ajax():
		html = render_to_string(
			template_name="all_spotify_playlist-results-partial.html", 
			context={"all_spotify_playlist": all_spotify_playlist}
		)

		data_dict = {"html_from_view": html}

		return JsonResponse(data=data_dict, safe=False)

	return render(request, "all_spotify_playlist_search.html", context=ctx)




