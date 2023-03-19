# OpenAI の API を試すデモ

今のところ ChatGPT の API を試すデモだけです。

## 準備

1. 仮想環境を作って requirements.txt をインストールします。

## 設定

1. settings_sample.py を settings.py にリネームします。
1. `SECRET_KEY` に OpenAI アカウントで発行したシークレットを設定します。
1. モデルを変えたい場合は `CHAT_MODEL` を変えます。

## ask.py

- ChatGPT API で一問一答式の質問を繰り返すデモです。
- 前のやりとりの内容は憶えません。

## chat.py

- ChatGPT API で文脈を憶えて会話するデモです。
- 質問するたびにそれまでの会話履歴を送信するので、トークンの消費量が雪だるま式に増えます。

## 参考

- https://platform.openai.com/docs/guides/chat
