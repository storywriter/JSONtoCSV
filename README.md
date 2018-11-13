# SpotifyToJSON

Spotify の API を叩いて、返ってきた JSON データをファイルとして手元に保存します。

ふたつのコマンドラインツールからなっています。

1. spotipy_to_json.py
2. json_to_csv.py


## spotipy_to_json.py

依存ライブラリ:
spotipy という Spotify のSDKを使っています。

利用手順:

### まず Spotify にアプリ登録します。

https://developer.spotify.com/dashboard/

Webサービスをつくるので、タイプは Website を指定します。

### アプリのダッシュボードのトップページから、Client ID と Client Secret をコピーして手元にメモ島ます。


### アプリのダッシュボードの EDIT SETTINGS から、Redirect URIs に認証後にリダイレクト表示するページのURLほ記入します。

かつてはどんなURLでもよかったらしいのですが、今は、実在するページでないとエラーになります。
また localhost はダメで、Spotify 側からアクセスできるページである必要があるようです。
なんでもよいので、ダミーページを1枚用意してください。

### spotipy_to_json.py をテキストエディタで開き、SPOTIPY_CLIENT_ID、SPOTIPY_CLIENT_SECRET、SPOTIPY_REDIRECT_URI を記入します。

### 続けて、username （SpotifyのユーザーID）も記入します。

### spotipy_to_json.py を実行するディレクトリ直下に temp という名前でディレクトリをつくります。取得したデータはこのディレクトリ内に保存されます。

### Spotify のアルバムIDを調べます。Spotify のアプリなどで、該当のアルバムでシェアする→リンクをコピーすると、IDがわかります。

例
https://open.spotify.com/album/6SHOYTaWp1ChOO4UhJquhA?si=FfBdBz7PS6eFTFCcRwyVWQ

この 6SHOYTaWp1ChOO4UhJquhA が Spotify のアルバムIDになります。

### spotipy_to_json.py の urn のところに、アルバムIDを書き換えます。

```python
urn = 'spotify:album:6SHOYTaWp1ChOO4UhJquhA' # アルバムID
```

のところの spotify:album: の後ろを差し替えます。

### spotipy_to_json.py を保存します。

### spotipy_to_json.py を実行します。

```
python spotipy_to_json.py
```

### 途中、認証で「Enter the URL you were redirected to:」というメッセージが出て、ブラウザが開くので、ブラウザのURLを、そのままコピーして、コンソールに貼り付けてエンターキーで進みます。

http://examlpe.com/?code=... の「 http://examlpe.com/?code= 」部分も含めてコピーすること。

### temp ディレクトリ配下に、曲ごとに JSON ファイルが保存されます。


## json_to_csv.py

spotipy_to_json.py でダウンロードした JSON ファイルを、ひとつに結合して、JSON ファイルと csv ファイルに吐き出します。

利用手順:

### spotipy_to_json.py で、temp ディレクトリ内に JSON ファイルを保存します。

### json_to_csv.py を実行します。

```
python json_to_csv.py
```
### temp ディレクトリ内に "_.json" と "_.csv" という名前で、結合されたファイルが生成されます。



