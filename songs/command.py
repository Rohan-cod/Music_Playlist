import schedule
import time
from .models import All_Playlist_Apple_Music, All_Playlist_Spotify
from .spotify import ToPlaylist
from .apple_music import A_ToPlaylist

cp = ToPlaylist()
cp_ = A_ToPlaylist()


def comm():
	li = cp.get_all_playlist()
	for i in li:
		All_Playlist_Spotify.objects.update_or_create(
			    pla_name = i
			)

	li_ = cp.get_all_playlist()
	for i_ in li_:
		All_Playlist_Apple_Music.objects.update_or_create(
			pla_name = i_
			)

schedule.every(10).minutes.do(comm)

while True:
	schedule.run_pending()
	time.sleep(1)


