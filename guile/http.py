import requests
from datetime import datetime as dt


def get_SID(user_id, password):
    """
    GUILEサイトにログインし, セッションを取得し返す
    :param user_id:
    :param password:
    :return: セッション
    """
    url = 'https://mypage.guile.jp/login'
    payload = f'login_id={user_id}&' \
              f'login_pass={password}'
    headers = {
        'Content-Type' : 'application/x-www-form-urlencoded',
        'Accept-Encoding' : 'gzip, deflate, br',
        'Accept-Language' : 'ja,en-US;q=0.8,en;q=0.6'
    }

    session = requests.Session()
    session.post(url, data=payload, headers=headers)

    return session.cookies


def get_ad_page(sid, campaign_id, ad_id):
    """
    campaign_id x ad_idのHTMLページを取得し返す
    :param sid:
    :param campaign_id:
    :param ad_id:
    :return: HTMLページ
    """
    today = dt.now().strftime('%Y-%m-%d')
    url = f'https://mypage.guile.jp/report/detail/{ad_id}?' \
          f'period_start={today}&' \
          f'period_end={today}&' \
          f'group_by={campaign_id}'

    headers = {
        'Content-Type' : 'application/x-www-form-urlencoded',
        'Accept-Encoding' : 'gzip, deflate, br',
        'Accept-Language' : 'ja,en-US;q=0.8,en;q=0.6'
    }

    response = requests.get(url, headers=headers, cookies=sid)
    response.encoding = response.apparent_encoding
    return response.text
