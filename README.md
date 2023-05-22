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

## 動かし方


