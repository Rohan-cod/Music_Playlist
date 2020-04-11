import json
import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import requests
import youtube_dl

apple_music_token = ""
apple_music_user_id = ""

class A_ToPlaylist():
    def __init__(self):
        self.youtube_client = self.get_youtube_client()
        self.all_song_info = {}

    def get_youtube_client(self):
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
        api_service_name = "youtube"
        api_version = "v3"
        client_secrets_file = "client_secret.json"
        scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            client_secrets_file, scopes)
        credentials = flow.run_console()
        youtube_client = googleapiclient.discovery.build(
            api_service_name, api_version, credentials=credentials)

        return youtube_client

    def get_liked_videos(self):
        request = self.youtube_client.videos().list(
            part="snippet,contentDetails,statistics",
            myRating="like"
        )
        response = request.execute()
        for item in response["items"]:
            video_title = item["snippet"]["title"]
            youtube_url = f'https://www.youtube.com/watch?v={item["id"]}'
            video = youtube_dl.YoutubeDL({}).extract_info(
                youtube_url, download=False)
            song_name = video["track"]
            artist = video["artist"]

            if song_name is not None and artist is not None:
                self.all_song_info[video_title] = {
                    "youtube_url": youtube_url,
                    "song_name": song_name,
                    "artist": artist,
                    "apple_music_uri": self.get_apple_music_uri(song_name, artist)

                }

    def get_playlist(self):
        query = f'https://api.music.apple.com/v1/me/library/playlists'
        response = requests.get(
            query,
            headers={
                "Content-Type": "application/json",
                "Authorization": f'Bearer {apple_music_token}'
            }
        )
        response_json = response.json()
        for playlist in response_json["data"]:
            if playlist["attributes"]["name"] == playlist_name:
                result = playlist["id"]

        return result

    def create_playlist(self, playlist_name, description):
        request_body = json.dumps({
            "name": playlist_name,
            "description": description,
            "public": True
        })

        query = f''
        response = requests.post(
            query,
            data=request_body,
            headers={
                "Content-Type": "application/json",
                "Authorization": f'Bearer {apple_music_token}'
            }
        )
        response_json = response.json()
        return response_json["id"]

    def get_all_playlist(self):
        query = f''
        response = requests.get(
            query,
            headers={
                "Content-Type": "application/json",
                "Authorization": f'Bearer {apple_music_token}'
            }
        )
        all_playlists = []
        response_json = response.json()
        for playlist in response_json["items"]:
            all_playlists.append(playlist["name"])

        return all_playlists

    def get_apple_music_uri(self, song_name, artist):
        query = f''
        response = requests.get(
            query,
            headers={
                "Content-Type": "application/json",
                "Authorization": f'Bearer {apple_music_token}'
            }
        )
        response_json = response.json()
        songs = response_json["tracks"]["items"]
        uri = songs[0]["uri"]

        return uri

    def add_song_to_playlist(self, playlist_name):
        self.get_liked_videos()
        uris = [info["spotify_uri"]
                for song, info in self.all_song_info.items()]
        playlist_id = self.get_playlist(playlist_name)
        q = f''
        res = requests.get(
            q,
            headers={
                "Content-Type": "application/json",
                "Authorization": f'Bearer {apple_music_token}'
            })
        res_json = res.json()
        tracks = res_json["tracks"]
        for track in tracks:
            t = track["track"]
            urri = t["uri"]
            if urri in uris:
                uris.remove(urri)


        request_data = json.dumps(uris)

        query = f''

        response = requests.post(
            query,
            data=request_data,
            headers={
                "Content-Type": "application/json",
                "Authorization": f'Bearer {apple_music_token}'
            }
        )

        response_json = response.json()
        return response_json

