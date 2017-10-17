# morikazu
もりかずの依頼のやつ

## セットアップ方法 (for Mac)
- Python3をダウンロード & インストール
```
https://www.python.org/downloads/
```

- git clone
```
$ git clone https://github.com/mattsu6/morikazu.git
$ cd morikazu
```

- Pythonモジュールをインストール
```
$ pip3 install -r requirements.txt
```

- MySQLをインストール
```
$ brew install mysql
```

- DBとテーブル作成
```
$ mysql -uroot
> create database guile_master_db;
> source sql/threshold_settings.sql
> exit()
```

- 設定ファイルを書く
```
$ cp common.ini.sample common.ini
$ vim common.ini
```

- 以下のように編集する
```
[common]
guile_id=ログインユーザ名
guile_pass=ログインパスワード

mail_address=通知メールの送信先

[guile_master_db]
host=localhost
db=guile_master_db
port=3306
user=root
pass=
```

- 閾値を設定する
```
$ mysql -uroot guile_master_db
> insert into threshold_settings(........
```

- 実行(1回だけ)
```
$ python3 main.py
```

- 定期実行
```
cd ~/Library/LaunchAgents/
vim test.plist
```
```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>test</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/bin/ruby</string>
        <string>-Ku</string>
        <string>スクリプトのある場所/main.py</string>
    </array>
    <key>StartInterval</key>
    <integer>180</integer>
    <key>StandardOutPath</key>
    <string>スクリプトのある場所に変更</string>
    <key>StandardErrorPath</key>
    <string>スクリプトのある場所に変更</string>
</dict>
</plist>
```

- 保存したら以下を実行して定期実行開始
```
$ launchctl load ~/Library/LaunchAgents/test.plist
```

- 停止
```
$ launchctl unload ~/Library/LaunchAgents/test.plist
```
