# れあｄめ.md
## What's this?
gym を使って、強化学習の実装の練習をしたものをここに残します。セミナーでも使うかもしれないので、以下に環境構築手順を示します。

## download this repository (20/9/25現在)
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
