# Spotify User Playlists

Look up any Spotify user and list their public playlists — then pick one and see
every track in it.

```
$ python main.py
Enter the username of the Spotify user you would like to look up: <username>

Available playlists for viewing:
  Late Night
  Driving Somewhere
  Winter

Enter the playlist you would like have tracks listed for: Winter

   1              Sufjan Stevens  Should Have Known Better
   2                Nick Drake    Northern Sky
   ...
```

## Files

| File | Purpose |
|---|---|
| `main.py` | The prompt loop — list playlists, then list one playlist's tracks |
| `fetch_spotify.py` | Auth + the API calls, via [spotipy](https://github.com/plamere/spotipy) |

## Running it

```bash
pip install spotipy
```

Register an app at the [Spotify developer dashboard](https://developer.spotify.com/dashboard)
and put the client ID, client secret and redirect URI at the top of
`fetch_spotify.py`. Then:

```bash
python main.py
```

The first run opens a browser to authorize. The token is cached locally after
that, so it only happens once.

## Why it stops where it does

This was meant to be half of something bigger: read a user's Spotify playlists,
then recreate them note for note in Apple Music. The reading half works, which is
what's here.

The writing half never got built — the Apple Music API requires an Apple Developer
account at $99/year, which is a lot to pay to move a playlist. So the project got
cut back to the part that was free, and shipped as that.

## Status

**Archival, and it mostly still works** — spotipy is alive and the endpoints it
uses (`user_playlists`, `user_playlist`) are current. Two caveats from 2019 that
have since changed:

- The `user-library-read` scope it requests is broader than this needs; public
  playlists don't require an authorized scope at all now.
- `util.prompt_for_user_token()` is deprecated in current spotipy. Use
  `SpotifyOAuth` — a couple of lines in `fetch_spotify.py`.
