# -*- encoding: utf-8 -*-
"""

PyCharm 单词序列.py
2024年10月13日21时22分
by wenyang

"""
# 单词序列
class Sentence(object):

    def __init__(self, text):
        self.text = text
        self.words = self.text.split(" ")

    def __len__(self):
        return len(self.words)

    def __getitem__(self, position):
        return self.words[position]

    def __repr__(self):
        return f"Sentence({self.text})"
import re
import reprlib

RE_WORD = re.compile(r"\w+")

class Sentence(object):

    def __init__(self, text):
        self.text = text
        self.words = ER_WORD.findall(text)

    def __len__(self):
        return len(self.words)

    def __getitem__(self, position):
        return self.words[position]

    def __repr__(self):
        return f"Sentence({reprlib.repr(self.text)})"
def main():
    s = Sentence("hello world javascript python 3.12 what up")
    for word in s.words:
        print(word)
    print(s)
    print(list(s))


if __name__ == "__main__":
    main()
