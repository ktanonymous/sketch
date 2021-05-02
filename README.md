# sketch

## 開発手順

まずは動作確認をします。以下の手順でコマンドを入力してみてください。  
* コンテナの起動

    ```
    docker-compose up -d
    ```

この状態で、ブラウザで[ローカルホスト](http://localhost:8000)に接続できない場合は「上手くいかない場合」を試してみて下さい。


<details>
 <summary>上手くいかない場合</summary>
  <div>

   `db`の起動が遅くて`python`コンテナが停止してしまっている可能性があります。試しに、次のコマンドを入力してみて下さい。

   ```
   docker restart python
   ```

   恐らくこれで[ローカルホスト](http://localhost:8000)に接続できると思います。  
   それでも解決しない場合には、管理者にご連絡下さい。

  </div>
</details>

<br>

* 開発環境に入る
このアプリには、`db`コンテナと`python`コンテナの2つがあります。  
実際の開発は後者で行うので、次のコマンドで`python`コンテナに入ります。  
これで、bashが開けるので、開発が始められます。

    ```
    docker exec -it python /bin/bash
    ```

<br>

* 開発作業の反映
    * `docker-compose.yml`、`Dockerfile`、`requirements.txt`のいずれかを編集した場合

        ```
        docker-compose up -d --build
        ```
    
    * それ以外
        ホストのカレントディレクトリとコンテナの`/code/`をマウントしているので、特に何もしなくても反映されます。  

<br>

* コンテナの停止
コンテナ内のbashを開いている場合は、まず、`exit`コマンドでコンテナから抜けます。  
ホストのコマンドラインで以下のコマンドを実行して下さい。

    ```
    docker-compose stop
    ```

## 参考サイト
* [Django+MySQLの開発環境をdocker-composeで構築する](https://qiita.com/bakupen/items/f23ce3d2325b4491a2dd)
* [Docker内でMySQLにPythonで接続する](https://qiita.com/kenjiSpecial@github/items/63d682274ad993d69c10)
* [docker-composeでDjango + MySQLの環境を作る](https://medium.com/@hokan_dev/docker-compose%E3%81%A7django-mysql%E3%81%AE%E7%92%B0%E5%A2%83%E3%82%92%E4%BD%9C%E3%82%8B-bd99cef7df0c)