import smtplib
import configparser
from email.mime.text import MIMEText


def send_over_threshold(settings, current):
    """
    ローカルホストから閾値を超えた際のメールを送信する.

    :param settings: DBから取得した設定値データ
    :param current: クローリングして取得した数値
    """
    config = configparser.ConfigParser()
    config.read('common.ini')

    # メール本文
    msg = MIMEText(f"campaign_id: {settings['campaign_id']}\n"
                   f"ad_id: {settings['ad_id']}\n"
                   f"type: {settings['target_param']}\n"
                   f"現在/設定値: {current} / {settings['threshold']}")

    # 送信先・送信元
    msg['Subject'] = f"campaign: {settings['campaign_id']}, ad: {settings['ad_id']} is over threshold"
    msg['From'] = "ma-guile-info@microad.co.jp"
    msg['To'] = config['common']['mail_address']

    server = smtplib.SMTP('localhost')
    server.sendmail("ma-guile-info@microad.co.jp", [config['common']['mail_address']], msg.as_string())
    server.quit()
