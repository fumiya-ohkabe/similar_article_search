## 概要
キュレーションサイトから記事をスクレイピングしwebアプリから入力したテキストと類似する記事を検索する

## 環境構築
- requirements.txt
    - pythonモジュール
- sql/table_structure.sql
    - DB作成

なお本番環境などでDBの接続先を変えたい場合は環境変数の

- ENVIROMENT
- DB_HOSTNAME
- DB_PASSWORD

を設定する。


## クローラー
- url_crawler.py
    - 記事urlをDBに保存
- html_crawler.py
    - DB上のurlからhtmlを取得してDBに保存
- html_parser.py
    - DB上のhtmlをパースしてDBに保存

## 類似度計算
- create_tfidf_vectorizer.py
    - DB上の記事をtf-idfでベクトル化する。後の類似度計算に必要な物をバイナリ化してdocsに保存している。
- show_similarities.py
    - bottleから呼び出される。渡されたテキストと類似度の高い記事を返す。

## アプリ起動
```
python app.py
```
