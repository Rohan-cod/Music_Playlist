from django.urls import path

from .views import HomePageView, Spotify, Apple_Music, New_Spotify, New_Apple_Music, search_spotify_view, search_apple_view, All_Spotify_Playlist, All_Apple_Music_Playlist


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('spotify/', Spotify.as_view(), name='spotify'),
    path('apple_music/', Apple_Music.as_view(), name='apple_music'),
    path('new_spotify/', New_Spotify.as_view(), name='new_spotify'),
    path('new_apple_music/', New_Apple_Music.as_view(), name='new_apple_music'),
    path('spotify_playlist/', All_Spotify_Playlist.as_view(), name='spotify_playlist'),
    path('apple_music_playlist/', All_Apple_Music_Playlist.as_view(), name='apple_music_playlist'),
    path('search_spotify/', search_spotify_view, name='search_spotify'),
    path('search_apple_music/', search_apple_view, name='search_apple_music'),
]