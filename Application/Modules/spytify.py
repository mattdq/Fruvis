import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
import os


class Spot():
    def __init__(self, local, vol):
        self.local = local
        self.vol = vol
        os.environ['SPOTIPY_CLIENT_ID'] = "ac075cdbffc643c4a56f92d41f905e48"
        os.environ['SPOTIPY_CLIENT_SECRET'] = "04ddcaa7a0604b6ab82fbf918d68e882"
        os.environ['SPOTIPY_REDIRECT_URI'] = "http://127.0.0.1:5000"

        scope = "user-read-playback-state,user-modify-playback-state"

        self.sp = spotipy.Spotify(client_credentials_manager=SpotifyOAuth(scope=scope))

        if local.count('sala') == 0:
            self.sp.transfer_playback(device_id='7b5a7d48ffaba6b288b501acb512d719f18c1eb3', force_play=False)  # Pc
        else:
            self.sp.transfer_playback(device_id='c2bf4b8d90227381da907da452717d928a285054', force_play=False)  # Sala

        self.sp.volume(vol)

    def raiseVol(self):
        self.vol += 10
        self.sp.volume(self.vol)

    def lowerVol(self):
        self.vol -= 10
        self.sp.volume(self.vol)

    def searchtrack(self, searchStr):
        result = self.sp.search(searchStr)
        result['name'] = result['tracks']['items'][0]['name']
        result['artist'] = result['tracks']['items'][0]['artists'][0]['name']
        return result

    def playtrack(self, uri):
        self.sp.start_playback(uris=[uri])