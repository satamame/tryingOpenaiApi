'''文脈を憶えて会話するコード例。トークンの消費量に注意。
'''
import openai

from settings import *

FIRST_SYS_PROMPT = 'あなたは戯曲のプロットを考える手伝いをしてください。'
openai.api_key = OPENAI_SECRET_KEY


def gen_res(new_prmp, msg_hist):
    '''レスポンス生成

    paramters
    ---------
    new_prmp : str
        新しく入力されたプロンプト
    msg_hist : list
        メッセージ履歴

    returns
    -------
    msg : str
        生成したメッセージ
    tokens : int
        消費したトークン数
    '''
    new_msg = {'role': 'user', 'content': new_prmp}
    msg_hist.append(new_msg)

    res = openai.ChatCompletion.create(
        model=CHAT_MODEL,
        messages=msg_hist,
    )

    res_msg = res['choices'][0]['message']
    msg_hist.append(res_msg)

    tokens = res['usage']['total_tokens']
    return res_msg['content'], tokens


def main():
    sys_prmp = FIRST_SYS_PROMPT
    history = [{'role': 'system', 'content': sys_prmp}]
    turn = 0
    total_tokens = 0

    print('終了するには exit と入力してください。')

    while True:
        input_ = input(f'{turn}>> ').strip()

        # 'exit' を入力されたら終了
        if input_.lower() == 'exit': break

        # 履歴の長さを憶えておく
        hist_cnt = len(history)

        try:
            msg, tokens = gen_res(input_, history)
            print('<< ' + msg.strip())
            total_tokens += tokens
            print(f'(tokens: {tokens}/{total_tokens})')
            turn += 1
        except:
            print('*** エラーが起きました。もういちど入力してください。')
            history = history[:hist_cnt]

    print('チャットを終了します。')


if __name__ == '__main__':
    main()
