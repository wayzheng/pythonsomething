# -*- encoding: utf-8 -*-
"""

PyCharm 生成器模式来创建迭代器.py
2024年10月13日23时56分
by wenyang

"""
import re
import reprlib

RE_WORD = re.compile(r"\w+")

class Sentence(object):

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(self.text)

    def __repr__(self):
        return "Sentence(%s)" % reprlib.repr(self.text)

    def __iter__(self):
        for word in self.words: # 迭代self.words
            yield word # 产出当前的单词
        return  # 这个return语句不是必须的 不管有没有return 语句 生成器函数都不会抛出 StopIteration

def main():
    ...


if __name__ == "__main__":
    main()
