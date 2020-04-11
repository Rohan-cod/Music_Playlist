from django.db import models
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse


class All_Playlist_Apple_Music(models.Model):
	pla_name = models.CharField(max_length=100)

class All_Playlist_Spotify(models.Model):
	pla_name = models.CharField(max_length=100)

class Playlist_Spotify(models.Model):
	playlist_name = models.CharField(max_length=100)

class Playlist_Apple_Music(models.Model):
	playlist_name = models.CharField(max_length=100)


class New_Playlist_Spotify(models.Model):
	
	description = models.CharField(max_length=200)
	playlist_name = models.CharField(max_length=100)

class New_Playlist_Apple_Music(models.Model):
	
	description = models.CharField(max_length=200)
	playlist_name = models.CharField(max_length=100)