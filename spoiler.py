'''TMDb から映画のあらすじを取得して ChatGPT が結末を考えるデモ。

TMDb の API についてのページ
https://www.themoviedb.org/documentation/api?language=ja
'''
import urllib

import requests
import openai

from settings import *

openai.api_key = OPENAI_SECRET_KEY


def search_tmdb(query):
    '''TMDb を検索して結果を返す

    parameters
    ----------
    query : str
        検索に使う文字列 (映画の邦題)

    returns
    -------
    list
        API から取得した映画情報 (辞書) のリスト
    '''
    params = urllib.parse.urlencode({
        'api_key': TMDB_API_KEY,
        'query': query,
        'language': 'ja',
    })
    url = f'https://api.themoviedb.org/3/search/movie?{params}'
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    res = requests.get(url, headers=headers)

    results = res.json()['results']
    return results


def get_movie_overview(title):
    '''TMDb から映画の概要を取得する

    parameters
    ----------
    title : str
        検索する映画の邦題

    returns
    -------
    str
        TMDb から取得した映画の概要
    '''
    try:
        movies = search_tmdb(title)
        cnt = len(movies)
        if cnt == 0:
            raise()
        if cnt > 1:
            for i, m in enumerate(movies):
                y = m['release_date'].split('-')[0]
                print(f'{i + 1}: {m["title"]} ({y})')
            while True:
                sel = input(f'どれにしますか？ (1～{cnt})>> ')
                sel = int(sel)
                if 1 <= sel <= cnt:
                    break
            return movies[sel - 1]['overview']
        else:
            return movies[0]['overview']
    except:
        raise Exception('映画の情報が見つかりませんでした。')


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
            messages=[
                {"role": "user", "content": prompt},
            ]
        )
        ending = response["choices"][0]["message"]["content"]
        return ending.strip()
    except:
        raise Exception('結末を考えられませんでした。')


def main():
    title = input('映画のタイトル>> ')
    try:
        overview = get_movie_overview(title)
        ending = predict_ending(overview)
        print(f'ChatGPT が考えた結末:\n{ending}')
    except Exception as err:
        print(err)
        return


if __name__ == '__main__':
    main()
