# sketch

## サーバー起動方法

以下のコマンドを実行し，コンテナを起動する。

```
$ docker-compose up -d
```

初回起動時は`python`コンテナで Django のコマンドを実行しなければならない。

```
$ bash shellscripts/enter_into_container.sh python
```

のように実行をしてコンテナにアクセスした後，以下のコマンドを実行する。

```
$ bash shellscripts/lazy_db_migrate.sh
```

実行後、http://localhost:8000 にアクセスすると利用できる。

## 終了時

コンテナ内にいる場合は、まず、`exit`コマンドでコンテナから抜ける必要がある。  
ローカルに戻った後に，以下のコマンドを実行するとコンテナが停止する。

```
$ docker-compose stop
```

## その他

### 管理者の登録

以下のコマンドを実行すると管理者登録用のプロンプトが表示される。

```
$ python manage.py createsuperuser
```

### コンテナ変更時

`docker-compose.yml`、`Dockerfile`、`requirements.txt`のいずれかを編集した場合，コンテナ内部に反映させるために以下のコマンドを実行する必要がある。

```
$ docker-compose up -d --build
```

## 参考サイト

- [Django+MySQL の開発環境を docker-compose で構築する](https://qiita.com/bakupen/items/f23ce3d2325b4491a2dd)
- [Docker 内で MySQL に Python で接続する](https://qiita.com/kenjiSpecial@github/items/63d682274ad993d69c10)
- [docker-compose で Django + MySQL の環境を作る](https://medium.com/@hokan_dev/docker-compose%E3%81%A7django-mysql%E3%81%AE%E7%92%B0%E5%A2%83%E3%82%92%E4%BD%9C%E3%82%8B-bd99cef7df0c)
