'''TMDb から映画のあらすじを取得して DALL·E がポスターを書くコード例。
'''
import openai

from settings import *
from tmdb import get_movie_overview

openai.api_key = OPENAI_SECRET_KEY

SIZE = '512x512'


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
    prompt = 'Create a DALL·E prompt to draw a movie poster '
    prompt += 'for the following plot, within 400 characters '
    prompt += 'without including unnecessary words like "prompt:". '
    prompt += "Don't use inproper words or phrases for DALL·E.\n"
    prompt += f'Prot:\n{overview}'

    try:
        response = openai.ChatCompletion.create(
            model=CHAT_MODEL,
            messages=[{"role": "user", "content": prompt}]
        )
        dalle_prmp = response["choices"][0]["message"]["content"]
        return dalle_prmp.strip().strip('"\'')
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
