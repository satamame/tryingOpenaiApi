'''ステートレスな一問一答式のコード例。
'''
import openai

from settings import *

openai.api_key = OPENAI_SECRET_KEY


def ask(prompt: str) -> str:
    response = openai.ChatCompletion.create(
        model=CHAT_MODEL,
        messages=[
            {"role": "user", "content": prompt},
        ]
    )
    msg = response["choices"][0]["message"]["content"]
    return msg


def main():
    print('終了するには exit と入力してください。')

    while True:
        input_ = input('>> ')

        # 'exit' を入力されたら終了
        if input_.lower() == 'exit': break

        msg = ask(input_)
        print('<< ' + msg.strip())
    print('終了します。')


if __name__ == '__main__':
    main()
