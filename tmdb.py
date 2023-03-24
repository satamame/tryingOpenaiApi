'''TMDb API を使う関数等のモジュール

TMDb の API についてのページ
https://www.themoviedb.org/documentation/api?language=ja
'''
import urllib

import requests

from settings import TMDB_API_KEY

genres = {
    28: 'Action',
    12: 'Adventure',
    16: 'Animation',
    35: 'Comedy',
    80: 'Crime',
    99: 'Documentary',
    18: 'Drama',
    10751: 'Family',
    14: 'Fantasy',
    36: 'History',
    27: 'Horror',
    10402: 'Music',
    9648: 'Mystery',
    10749: 'Romance',
    878: 'Science Fiction',
    10770: 'TV Movie',
    53: 'Thriller',
    10752: 'War',
    37: 'Western',
}


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
            raise

        # 公開日順にソートする
        movies.sort(key=lambda m: m['release_date'])

        m_i = 0  # 複数あった場合の選択するインデックス
        if cnt > 1:
            for i, m in enumerate(movies):
                y = m['release_date'].split('-')[0]
                print(f'{i + 1}: {m["title"]} ({y})')
            while True:
                sel = input(f'どれにしますか？ (1～{cnt})>> ')
                if sel in [str(x + 1) for x in range(cnt)]:
                    m_i = int(sel) - 1
                    break
                if not sel:
                    break
        return movies[m_i]['overview']
    except:
        raise Exception('映画の情報が見つかりませんでした。')
