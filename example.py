import spotipy
spotify = spotipy.Spotify()
results = spotify.search(q='artist:' + 'Yo Gotti', type='artist')
print results