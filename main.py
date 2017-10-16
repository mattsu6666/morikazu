from db import threashold_settings
from guile import http, scraping
import configparser

def main():
    config = configparser.ConfigParser()
    config.read('common.ini')

    settings = threashold_settings.find_all()
    session_id = http.get_SID(config['common']['guile_id'], config['common']['guile_pass'])

    for s in settings:
        page = http.get_ad_page(session_id, s['campaign_id'], s['ad_id'])
        # 値をプリントするとこまでできたので
        # enumとclass名のマッピング
        print(scraping.get_target_count(page, s['target_param']))

if __name__ == '__main__':
    main()