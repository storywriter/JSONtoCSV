#! /usr/local/bin/python2.7
# coding: utf-8

# SpotifyのJSONをCSVファイルにする 
# 2017年10月7日


import os
import json
import pandas as pd

path = 'temp' # JSONファイルが入っているディレクトリ
csv_name = '_.csv' # 出力するcsvファイルの名前
json_name = '_.json' # 出力するcsvファイルの名前

jsonfiles = os.listdir( path ) # path フォルダ内のファイル一覧を取得

df = pd.DataFrame( index = [], columns = [ 'track_number','name','artists','uri','duration_ms', 'tempo', 'mode', 'loudness', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'speechiness', 'valence' ] )


# JSON の読み込み
for jsonfile in jsonfiles:

  if ( jsonfile != csv_name ) and ( jsonfile != json_name ) and ( jsonfile != '.DS_Store' ): # csv_name と json_name と .DS_Store は除く

    with open( path + '/' + jsonfile, 'r' ) as f:

      j = json.load( f )
      s = pd.Series( [ j[ 'track_number' ], j[ 'name' ], j[ 'artists' ], j[ 'uri' ], j[ 'duration_ms' ], j[ 'tempo' ], j[ 'mode' ], j[ 'loudness' ], j[ 'acousticness' ], j[ 'danceability' ], j[ 'energy' ], j[ 'instrumentalness' ], j[ 'liveness' ], j[ 'speechiness' ], j[ 'valence' ] ], index = df.columns )
      df = df.append( s, ignore_index=True )


# 値を 0-1 の間に正規化する（分散が同じあたりに集まっている場合、正しく正規化できないので注意。どれかが必ず0と1になってしまう）
df[ 'duration_ms' ] = ( df[ 'duration_ms' ] - df[ 'duration_ms' ].min() ) / ( df[ 'duration_ms' ].max() - df[ 'duration_ms' ].min() )
# df[ 'duration_ms' ] = ( df[ 'duration_ms' ] - 0 ) / ( 2000000 - 0 )
df[ 'tempo' ] = ( df[ 'tempo' ] - df[ 'tempo' ].min() ) / ( df[ 'tempo' ].max() - df[ 'tempo' ].min() )
# df[ 'tempo' ] = ( df[ 'tempo' ] - 60 ) / ( 200 - 60 )
df[ 'loudness' ] = ( df[ 'loudness' ] - df[ 'loudness' ].min() ) / ( df[ 'loudness' ].max() - df[ 'loudness' ].min() )
# df[ 'loudness' ] = ( ( df[ 'loudness' ] - 0 ) / ( 60 - 0 ) ) * -1




# ファイルに出力
df.to_csv( path + '/' + csv_name, encoding = 'shift-jis' )
df.to_json( path + '/' + json_name, orient = 'index' )