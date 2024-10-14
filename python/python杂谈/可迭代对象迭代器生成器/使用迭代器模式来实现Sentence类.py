# -*- encoding: utf-8 -*-
"""

PyCharm 使用迭代器模式来实现Sentence类.py
2024年10月13日23时33分
by wenyang

"""

import re
import reprlib

from IPython.core.ultratb import text_repr

RE_WORD = re.compile(r"\w+")

class Sentence(object):

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(self.text)

    def __repr__(self):
        return "Sentence(%s)" % reprlib.repr(self.text)

    def __iter__(self): # 可以迭代
        return SentenceIterator(self.words) # 返回一个迭代器

class SentenceIterator(object):
    # 初始化属性
    def __init__(self, words):
        self.words = words
        self.index = 0

    # 实现迭代器的__next__方法
    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word

    # 实现迭代器的__iter__方法
    def __iter__(self):
        return self
def main():



if __name__ == "__main__":
    main()
