# OpenAI の API を試すコード例

## 準備

1. 仮想環境を作って requirements.txt をインストールします。

## 設定

1. settings_sample.py を settings.py にリネームします。
1. `SECRET_KEY` に OpenAI アカウントで発行したシークレットを設定します。
1. モデルを変えたい場合は `CHAT_MODEL` を変えます。
1. spoiler.py または poster.py を使う場合は、`TMDB_API_KEY` に TMDb で発行した API キーを設定します。

## ask.py

- ChatGPT API で一問一答式の質問を繰り返すコード例です。
- 前のやりとりの内容は憶えません。

## chat.py

- ChatGPT API で文脈を憶えて会話するコード例です。
- 質問するたびにそれまでの会話履歴を送信するので、トークンの消費量が雪だるま式に増えます。

## spoiler.py

- ChatGPT が映画の概要をもとに結末を考えるコード例です。
- タイトルを入力すると映画の概要を TMDb から取得して ChatGPT API に渡します。
- ※タイトルは ChatGPT API には渡していません。

## poster.py

- ChatGPT が映画の概要をもとにそのポスターを描くためのプロンプトを考えるコード例です。
- タイトルを入力すると映画の概要を TMDb から取得して ChatGPT API に渡します。
- ※タイトルは ChatGPT API には渡していません。
- ChatGPT が考えたプロンプトを使って DALL·E に描画させ、画像の URL を出力します。

## 参考

- https://platform.openai.com/docs/guides/chat
- https://platform.openai.com/docs/guides/images
- https://www.themoviedb.org/documentation/api?language=ja
