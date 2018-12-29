# coding=utf-8

import argparse
import json
import os

import pyperclip
from fuzzywuzzy import fuzz
from pick import pick


THRESHOLD = 80
VERSION = "0.1.0"

TITLE = "Emojis: Use arrow keys"

HERE = os.path.join(
    os.path.abspath(os.path.dirname(__file__)), "emojilib")
#
with open(os.path.join(HERE, "emojis.json"), "r", encoding="utf-8") as f:
    emojis = json.load(f)


def get_parser():
    """
    解析命令行参数
    """
    parser = argparse.ArgumentParser(description="Search emoji via command-line")
    parser.add_argument(
        "keyword", metavar="KEYWORD", type=str, nargs="*", help="emoji keyword"
    )
    parser.add_argument(
        "-v",
        "--version",
        action="store_true",
        help="displays the current version of youdao",
    )
    return parser


def command_line_runner():
    """
    执行命令行操作
    """
    parser = get_parser()
    args = vars(parser.parse_args())

    if args["version"]:
        print("emoji", VERSION)
        return

    if len(args["keyword"]) == 0:
        parser.print_help()
        return

    keyword = args["keyword"][0]
    if not keyword:
        parser.print_help()
        return

    query_emoji(keyword)


def query_emoji(keyword):
    """
    查询 emoji 表情
    """
    opts = list()

    for key, value in emojis.items():
        for v in value.get("keywords"):
            if fuzz.ratio(v, keyword) > THRESHOLD:
                opts.append(value.get("char"))

    if len(opts) == 0:
        print("Sorry, nothing found!")
        return

    opt, index = pick(opts, TITLE, indicator="=>")
    pyperclip.copy(opt)
    print("Copied", opt)


if __name__ == "__main__":
    command_line_runner()
