'''TMDb から映画のあらすじを取得して DALL·E がポスターを書くコード例。
'''
import openai
from openai import InvalidRequestError

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
        ChatGPT が考えた DALL·E へのプロンプト
    '''
    sys_prmp = '''
今後は OpenAI の safety system に反しないよう、安全な表現だけを使ってください。
性、残酷、暴力を思わせる言葉や、倫理に反する言葉は絶対に使わないでください。
'''

    user_prmp = '''
以下のプロットで映画を作っています。この映画のポスターを描くための指示が欲しい。
たとえば描かれている人物、背景、時代、土地、雰囲気、題名ロゴ、デザイン、画風など。
英語で40語以内に収めること。
実在する有名な映画の題名、キャラクター、俳優の名前は使わないこと。
'''
    user_prmp += f'\nプロット:\n{overview}'

    try:
        response = openai.ChatCompletion.create(
            model=CHAT_MODEL,
            messages=[
                {"role": "system", "content": sys_prmp},
                {"role": "user", "content": user_prmp}
            ]
        )
        dalle_prmp = response["choices"][0]["message"]["content"]
        return dalle_prmp.strip().strip('"\'')
    except:
        raise Exception('DALL·E へのプロンプトを考えられませんでした。')


def main():
    title = input('映画のタイトル>> ')
    try:
        overview = get_movie_overview(title)
        print('ChatGPT が考えた DALL·E へのプロンプト...')
        prompt = make_dalle_prmp(overview)
        print(prompt)
        print('ポスターを描画中...')
        response = openai.Image.create(
            prompt=prompt,
            size=SIZE,
        )
        print(response['data'][0]['url'])
    except InvalidRequestError as err:
        print(f'Invalid Request: {err}')
        return
    except Exception as err:
        print(f'Error: {err}')
        return


if __name__ == '__main__':
    main()
