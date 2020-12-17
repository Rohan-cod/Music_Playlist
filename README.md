# Music Playlist App
A **Django** app to automatically add songs liked by you on **YouTube** to a **Spotify** **|** **Apple Music** playlist. 🎧 

## Configuration Required

  * Go to `songs/spotify.py`. Add your **Spotify Oauth Token** to the `spotify_token` variable and **Spotify user_id** to the `spotify_user_id` variable. To get **user_id** click [here](https://www.spotify.com/us/account/overview/). To get **Oauth Token** click [here](https://developer.spotify.com/console/post-playlists/).
  * Go to `songs/apple_music.py`. Add your **Apple music token** to the `apple_music_token` variable.
  * Go to `songs/client_secret.json`. Replace the complete contents of the file with the contents of your `client_secret.json` file that you can download after enabling **Oauth for YouTube** from [here](https://developers.google.com/youtube/v3/getting-started/).

## Steps to get the Oauth Token from Spotify
  * Login to your [Spotify account](https://www.spotify.com/us/account/overview/) and get your username.
  * The username will be your Spotify user_id.
  * Now, get the [Oauth token](https://developer.spotify.com/console/post-playlists/) by entering your user_id and then click Get Token.
  * In the scope options, select the required scopes.
  * It will generate a Spotify token and note that this **token expires** every once in a while. So, if you face any issue with accessing your Spotify Playlist, it may be because
  your token might have expired. In that case, create a new token by repeating the above process.
 

## Steps to get the Oauth for Youtube
  * Login to the [Google Cloud Platform](https://console.developers.google.com/)
  * Create a new project by entering your project name.
  * Now enable the the api (**YouTube Data API v3**) by selecting the "ENABLE APIS AND SERVICES" option.
  * After enabling the api, crete your credentials by clicking the "Credentials" in the sidebar.
  * Now press the "+ CREATE CREDENTIALS" option and then **select the OAuth Client ID**
  * Click on "CONFIGURE CONSENT SCREEN" and it redirect to OAuth consent screen.
  * Select the External option in the User type and then proceed.
  * Now, fill out the required fields and proceed forward. (Note: In the scopes section go through all the options and select the ones you think will be necessary)
  * In the Test Users section, add your email address and then save and continue.
  * Now, head back to the Credentials section in the sidebar and create the OAuth client ID.
  * Select the application type to be "**Web application**".
  * Now, in the "Authorized redirect URIs" add your local url of the django app. (It may look like "http://127.0.0.1:8000/")
  * After entering all the details, save it and then an OAuth client ID will be created.
  * Now download the **json file** by clicking on the download symbol next to your client ID.
  * Copy the contents of the json file and paste it inside the client_secret.json file in your projects folder.

**Note that in the above method, it is mentioned that the app is a web application, so for it work the app needs to deployed first. So, use heroku to deploy the app in the web.**

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
## Code of Conduct
Check code of conduct [here](https://github.com/shubhdeeprajput/Music_Playlist/blob/master/CODE_OF_CONDUCT.md)


## Communities for extenxive bussiness
Artists
Developers
Advertising
Investors
Vendors

## User Interface
Available in many different languages

## Resources
For deploying app using Heroku : [Heroku Tutorial](https://youtu.be/6DI_7Zja8Zc)
