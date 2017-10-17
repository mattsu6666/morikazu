from db import threashold_settings
from guile import http, scraping
import mail
import configparser


def main():
    """
    python main.py で実行.
    GUILEサイトをクローリングしthreshold_settingsの設定値を超えた場合にメール通知をする.
    :return:
    """
    config = configparser.ConfigParser()
    config.read('common.ini')

    # GUILEのサイトにログイン
    settings = threashold_settings.find_all()
    session_id = http.get_SID(config['common']['guile_id'], config['common']['guile_pass'])

    # 有効な設定値すべてに関して閾値のチェック
    for s in settings:
        page = http.get_ad_page(session_id, s['campaign_id'], s['ad_id'])
        fetched_count = scraping.get_target_count(page, s['target_param'])
        # 閾値を超えた場合はメール通知とDBのステータスを更新
        if fetched_count >= int(s['threshold']):
            mail.send_over_threshold(s, fetched_count)
            threashold_settings.update_to_inactive(s['id'])

if __name__ == '__main__':
    main()
