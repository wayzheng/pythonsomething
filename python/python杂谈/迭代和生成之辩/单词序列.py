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

class SentenceOne(object):

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

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

    s1 = SentenceOne("hello world javascript")
    it = iter(s1)
    print("iter迭代器:", it)
    print(next(it))
    print(next(it))
    print(next(it))
    # print(next(it)) 此时就是会发生报错 这是因为迭代器已经迭代完毕了 但是继续爹地啊的话就是会爆出StopIteration的异常
    print("将s1变成一个序列", list(it)) # 此时就是会的到一个空的序列列表 这是因为迭代器已经迭代完成了 所以内部就是一个空的一个序列
    print("将s1重新变成一个序列", list(iter(s1)))

if __name__ == "__main__":
    main()
