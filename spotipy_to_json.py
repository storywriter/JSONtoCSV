#! /usr/local/bin/python2.7
# coding: utf-8

# SpotifyのAPIから返ってきたJSONをファイルにする 
# 2017年10月7日


# 途中、ブラウザが開くので、
# http://example.com/?code=...
# の「 http://example.com/?code= 」というURLも含めて Enter the URL you were redirected to: に入力すること。


import os
import json
import spotipy
import spotipy.util as util


os.environ[ 'SPOTIPY_CLIENT_ID' ] = '' # your-spotify-client-id
os.environ[ 'SPOTIPY_CLIENT_SECRET' ] = '' # your-spotify-client-secret
os.environ[ 'SPOTIPY_REDIRECT_URI' ] = '' # your-app-redirect-url

username = '' # Spotify のユーザーID
scope = 'user-library-read'

token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify( auth = token )

    # ここを書き換える
    urn = 'spotify:album:6SHOYTaWp1ChOO4UhJquhA' # アルバムID 例 spotify:album:6SHOYTaWp1ChOO4UhJquhA

    album = sp.album( urn ) # アルバム情報を取得

    for track in album[ 'tracks' ][ 'items' ]:

      # print( json.dumps( track, indent = 4 ) ) # アルバム情報

      track_number = track[ 'track_number' ]
      tids = track[ 'id' ]
      name = track[ 'name' ]
      artists = track[ 'artists' ][ 0 ][ 'name' ]
      d = { 'name': name, 'artists': artists, 'track_number': track_number }

      features = sp.audio_features( tids ) # 曲情報を取得

      features[ 0 ].update( d )

      with open( 'temp/' + str( track_number ) + '.json', 'w' ) as f:
        print( json.dumps( features[ 0 ], indent = 4 ), file = f )

else:
    print( "Can't get token for", username )