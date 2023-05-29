# trash-bot-kun
ゴミ収集をSlackに通知するアプリケーション
## 環境構築

- pyenvとpyenv-virtualenvを使用します

```shell!
cd　/path/to/trash-bot-kun
pyenv virtualenv 3.9.9 trash-bot-kun
pyenv local trash-bot-kun

pip install -U pip setuptools wheel poetry
```

- poetryを使用して依存ライブラリをインストールします

```shell
poetry install
```

- 環境変数にSlackのAPIを設定します
```shell
export TRASH_BOT_KUN_SLACK_API = "☓☓☓☓☓☓☓☓"
```

## 動かし方

- 以下のコマンドを実行します

```shell
# 大文字の曜日部分には登録するゴミの種類を入力
# MONDAY:可燃ごみ,TUESDAY:不燃語ごみ...など

poetry run python main.py --monday 'MONDAY' --tuesday 'TUESDAY' --wednesday 'WEDNESDAY' --thursday 'THURSDAY' --friday 'FRIDAY'　--saturday 'SATURDAY' --sunday 'SUNDAY'

# 土曜日と日曜日は未入力でも実行される

poetry run python main.py --monday 'MONDAY' --tuesday 'TUESDAY' --wednesday 'WEDNESDAY' --thursday 'THURSDAY' --friday 'FRIDAY'

```
- Slackへ通知が届く
