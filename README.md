# emoji.py 
[![PyPI version](https://badge.fury.io/py/emoji.py.svg)](https://badge.fury.io/py/emoji.py) 

emoji 表情命令行搜索工具，灵感来自 [emoji-cli](https://github.com/watilde/emoji-cli)。

### 安装

**安装依赖包**

依赖需要用到两个 wheel 包，地址在这里，根据自己对应的 Python 版本下载安装即可。
```http
https://www.lfd.uci.edu/~gohlke/pythonlibs/#python-levenshtein
https://www.lfd.uci.edu/~gohlke/pythonlibs/#curses
```

**安装 emoji.py**

```bash
$ pip install emoji.py
```

### 使用

```bash
$ emoji -h
usage: emoji [-h] [-v] [KEYWORD [KEYWORD ...]]

Search emoji via command-line

positional arguments:
  KEYWORD        emoji keyword

optional arguments:
  -h, --help     show this help message and exit
  -v, --version  displays the current version of emoji
```

### 示例

<div align="center">
    <img width="90%" src="https://user-images.githubusercontent.com/19553554/50540626-34e47000-0bd0-11e9-98b7-6888cfbe58df.gif">
</div>


### License

MIT [©chenjiandongx](https://github.com/chenjiandongx)
