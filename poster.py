'''TMDb から映画のあらすじを取得して DALL·E がポスターを書くデモ。
'''
import openai

from settings import *
from tmdb import get_movie_overview

openai.api_key = OPENAI_SECRET_KEY

SIZE = '256x256'


def make_dalle_prmp(overview):
    '''映画の概要から ChatGPT が DALL·E のプロンプトを考える

    parameters
    ----------
    overview : str
        映画の概要

    returns
    -------
    str
        ChatGPT が考えた DALL·E のプロンプト
    '''
    prompt = '以下のプロットの映画があります。'
    prompt += 'この映画のポスターを DALL·E に描かせるプロンプトを'
    prompt += '英語で作ってください。\n'
    prompt += f'プロット:\n{overview}'

    try:
        response = openai.ChatCompletion.create(
            model=CHAT_MODEL,
            messages=[{"role": "user", "content": prompt}]
        )
        dalle_prmp = response["choices"][0]["message"]["content"]
        return dalle_prmp.strip()
    except:
        raise Exception('DALL·E のプロンプトを考えられませんでした。')


def main():
    title = input('映画のタイトル>> ')
    try:
        overview = get_movie_overview(title)
        print('ChatGPT が考えた DALL·E のプロンプト...')
        prompt = make_dalle_prmp(overview)
        print(prompt)
        print('ポスターを描画中...')
        response = openai.Image.create(
            prompt=prompt,
            size=SIZE,
        )
        print(response['data'][0]['url'])
    except Exception as err:
        print(err)
        return


if __name__ == '__main__':
    main()
