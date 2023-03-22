'''TMDb から映画のあらすじを取得して ChatGPT が結末を考えるコード例。
'''
import openai

from settings import *
from tmdb import get_movie_overview

openai.api_key = OPENAI_SECRET_KEY


def predict_ending(overview):
    '''映画の概要から ChatGPT が結末を考える

    parameters
    ----------
    overview : str
        映画の概要

    returns
    -------
    str
        ChatGPT が考えた結末
    '''
    prompt = '以下のプロットの映画を作ろうとしています。'
    prompt += f'結末を考えて1文で答えてください。\nプロット:\n{overview}'

    try:
        response = openai.ChatCompletion.create(
            model=CHAT_MODEL,
            messages=[{"role": "user", "content": prompt}]
        )
        ending = response["choices"][0]["message"]["content"]
        return ending.strip()
    except:
        raise Exception('結末を考えられませんでした。')


def main():
    title = input('映画のタイトル>> ')
    try:
        overview = get_movie_overview(title)
        print('ChatGPT が考えた結末...')
        ending = predict_ending(overview)
        print(ending)
    except Exception as err:
        print(err)
        return


if __name__ == '__main__':
    main()
