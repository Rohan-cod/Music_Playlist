# Music Playlist App
A **Django** app to automatically add songs liked by you on **YouTube** to a **Spotify** **|** **Apple Music** playlist. 🎧 

## Configuration Required

  * Go to `songs/spotify.py`. Add your **Spotify Oauth Token** to the `spotify_token` variable and **Spotify user_id** to the `spotify_user_id` variable. To get **user_id** click [here](https://www.spotify.com/us/account/overview/). To get **Oauth Token** click [here](https://developer.spotify.com/console/post-playlists/).
  * Go to `songs/apple_music.py`. Add your **Apple music token** to the `apple_music_token` variable.
  * Go to `songs/client_secret.json`. Replace the complete contents of the file with the contents of your `client_secret.json` file that you can download after enabling **Oauth for YouTube** from [here](https://developers.google.com/youtube/v3/getting-started/).


## Requirements

  * Python 3.7  
  * Django 2.2.10
  * [Youtube Data API v3](https://developers.google.com/youtube/v3)
  * [Spotify Web API](https://developer.spotify.com/documentation/web-api/)
  * [Apple Music API](https://developer.apple.com/documentation/applemusicapi)
  * [Requests Library v 2.22.0](https://requests.readthedocs.io/en/master/)
  * [Youtube_dl v 2020.01.24](https://github.com/ytdl-org/youtube-dl/)
  * Additional requirements are in **Pipfile**.

## Setting up the Project

  * Download and install Python 3.7
  * Download and install Git.
  * Fork the Repository.
  * Clone the repository to your local machine `$ git clone https://github.com/<your-github-username>/Music_Playlist.git`
  * Change directory to Music_Playlist `$ cd Music_Playlist`
  * Install pipenv `$ pip3 install pipenv`  
  * Create a virtual environment and install all requirements from Pipfile `$ pipenv install`  
  * Activate the env: `$ pipenv shell`
  * Make migrations `$ python manage.py makemigrations`
  * Migrate the changes to the database `$ python manage.py migrate`
  * Create superuser `$ python manage.py createsuperuser`
  * Run the server `$ python manage.py runserver`

## Contributing

Feel free to raise a issue or make a pull request to fix a bug or add a new feature. If you are new to open source you can first read about git by [clicking here](https://www.codecademy.com/learn/learn-git).

## Communtiy Slack Channel

To get started, the first step is to meet the community. We use slack to communicate, and there the helpful community will guide you. Slack is an instant messaging service used by developers and users of GitHub. It uses chatrooms, where developers can join in and can talk about a particular topic. [Click here](https://join.slack.com/t/codingninjas-talk/shared_invite/enQtODI1ODM0NTIzNzMwLTk3ZjMwMDExNWFlMTMyZDdjMjYzOWMzNjFmYzY5YjYyYjYzMmJiNDEyZmZlM2ExMDU0MGUzYzRiMTMyZGFiNDI) to join our Slack Workspace.
