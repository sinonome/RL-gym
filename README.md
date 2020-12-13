# れあｄめ.md
## What's this?
gym を使って、強化学習の実装の練習をしたものをここに残します。セミナーでも使うかもしれないので、以下に環境構築手順を示します。

## download this repository (20/10/15現在)
追記します。

```bash
$ git clone https://github.com/sinonome/RL-gym.git
```

## env
### poetry
こちらの環境構築は初心者なので間違っていたら教えてください。

#### install by pip

```bash
$ pip install poetry
```

#### settings
windows ではデフォルトでプロジェクト直下に `.venv` フォルダが生成されないみたいだ。
その結果、何か支障があるわけではないが、vs code が仮想環境を感知してくれないので以下のように設定する。
なお、[ここ](https://medium.com/music-and-technology/poetry%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%A8%E4%BB%AE%E6%83%B3%E7%92%B0%E5%A2%83%E4%BD%9C%E6%88%90%E5%85%88%E3%81%AE%E5%A4%89%E6%9B%B4-96e1bab83725) を参考にさせていただいた。

```shell
$ poetry config --list
# 一部省略
#=> virtualenvs.in-project = null
$ poetry config virtualenvs.in-project true
```

#### make venv

```bash
# dev ver
$ poetry install
# non-dev ver
$ poetry install non-dev
```

#### activate
```bash
$ poetry shell
```

#### deactivate
`deactivate` でできるらしいですが、これは罠なのでしてはいけません。`exit` しましょう。


### venv (廃止)
以下による環境構築をやめ、poetry による環境構築に移行しました。

```bash
$ python -m venv venv
```

#### for windows

```bash
$ venv/Scripts/activate
```

#### for mac

```bash
$ source venv/bin/activate
```

### install library
#### upgrade pip

```bash
# for windows
$ python -m pip install --upgrade pip
# for mac
$ pip install --upgrade pip
```

#### install requirements.txt

```bash
$ pip install -r requirements.txt
```

### deactivate
venv を無効化する場合は次のコマンドを入力

```
$ deactivate
```

もしくはターミナルそのまま閉じても OK な場合があります。
