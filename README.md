# SpotifyToJSON

Spotify の API を叩いて、返ってきた JSON データをファイルとして手元に保存します。

ふたつのコマンドラインツールからなっています。

1. spotipy_to_json.py
2. json_to_csv.py


## spotipy_to_json.py

依存ライブラリ:
spotipy という Spotify のSDKを使っています。

spotipy
https://spotipy.readthedocs.io/en/latest/

まず、実行する環境に spotipy をインストールしてから進めてください。


利用手順:

### 1.まず Spotify にアプリ登録します。

https://developer.spotify.com/dashboard/

Webサービスをつくるので、タイプは Website を指定します。

### 2.アプリのダッシュボードのトップページから、Client ID と Client Secret をコピーして手元にメモ島ます。


### 3.アプリのダッシュボードの EDIT SETTINGS から、Redirect URIs に認証後にリダイレクト表示するページのURLを記入します。

かつてはどんなURLでもよかったらしいのですが、今は、実在するページでないとエラーになります。
また localhost はダメで、Spotify 側からアクセスできるページである必要があるようです。
なんでもよいので、ダミーページを1枚用意してください。

### 4.spotipy_to_json.py をテキストエディタで開き、SPOTIPY_CLIENT_ID、SPOTIPY_CLIENT_SECRET、SPOTIPY_REDIRECT_URI を記入します。

### 5.続けて、username （SpotifyのユーザーID）も記入します。

### 6.spotipy_to_json.py を実行するディレクトリ直下に temp という名前でディレクトリをつくります。取得したデータはこのディレクトリ内に保存されます。

### 7.Spotify のアルバムIDを調べます。Spotify のアプリなどで、該当のアルバムでシェアする→リンクをコピーすると、IDがわかります。

例
https://open.spotify.com/album/6SHOYTaWp1ChOO4UhJquhA?si=FfBdBz7PS6eFTFCcRwyVWQ

この 6SHOYTaWp1ChOO4UhJquhA が Spotify のアルバムIDになります。

### 8.spotipy_to_json.py の urn のところに、アルバムIDを書き換えます。

```python
urn = 'spotify:album:6SHOYTaWp1ChOO4UhJquhA' # アルバムID
```

のところの spotify:album: の後ろを差し替えます。

### 9.spotipy_to_json.py を保存します。

### 10.spotipy_to_json.py を実行します。

```
python spotipy_to_json.py
```

### 11.途中、認証で「Enter the URL you were redirected to:」というメッセージが出て、ブラウザが開くので、ブラウザのURLを、そのままコピーして、コンソールに貼り付けてエンターキーで進みます。

http://examlpe.com/?code=... の「 http://examlpe.com/?code= 」部分も含めてコピーすること。

### 12.temp ディレクトリ配下に、曲ごとに JSON ファイルが保存されます。


## json_to_csv.py

spotipy_to_json.py でダウンロードした JSON ファイルを、ひとつに結合して、JSON ファイルと csv ファイルに吐き出します。

利用手順:

### 1.spotipy_to_json.py で、temp ディレクトリ内に JSON ファイルを保存します。

### 2.json_to_csv.py を実行します。

```
python json_to_csv.py
```
### 3.temp ディレクトリ内に "_.json" と "_.csv" という名前で、結合されたファイルが生成されます。



