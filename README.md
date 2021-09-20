# tweepy

PythonでTweepy（TwitterAPI用Pythonライブラリ）を用いたコードをおいています。

## twpic

Twitterでフォローしている人の投稿画像を新着順で自動保存するツールです。

1 . twipicディレクトリに[config.py]で自分のTwitterディベロッパーアカウントのユーザー情報を入れてください。

  Linux 例）/home/[ユーザー名]/tweepy/twpic/config.py

  Win 例）C:\\tweepy\\twpic\\config.py

```python:config.py
consumer_key = 'ココ'
consumer_secret = 'ココ'
access_token = 'ココ'
access_token_secret = 'ココ'
```

2 . processing導入環境であれば、twpic_show.pdeを実行

processingにより、保存した画像をリアルタイムで表示しています。

比較的簡単に導入できるため、余裕があればインストールしてください。

3 . twpic.pyを実行

win勢はtwpic_win.pyをどうぞ。

4 . skip?>>[ココ]

[no]か[yes]でスキップ機能を切り替えます。

5 . How?>>[ココ]

自然数を入力して、一人あたりの探索するツイート数を指定します。

※10を入力した場合、[最新10ツイートを検索]という意味です。保存する画像数ではありません。

6 . Processingに画像が表示される

7 . tweepy/savepicに画像が保存される

詳しくは、こちらの記事をご覧ください。


License : 
- 商用利用は、禁止です
- 非商用利用は、著作権表示を行えば自由に利用できます
