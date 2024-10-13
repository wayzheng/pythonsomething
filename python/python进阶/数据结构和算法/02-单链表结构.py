# -*- encoding: utf-8 -*-
"""

PyCharm 02-单链表结构.py
2024年10月13日17时21分
by wenyang

"""
# 定义一个单链表的类
# 首先要创建一个节点的类
# 链表就是由一个一个的节点组成的
class Node(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
class LinkedList(object):
    def __init__(self):
        # 首先要定义链表的一个根节点
        self.root = Node()
        # 通过self.size来记录链表的长度
        self.size = 0
        self.next = None # 增加新的数据 就是将新的数据的索引或者地址与上一个数据的地址来进行关联
    # 默认就是在尾部进行增加数据
    def append(self, value):
        # 首先实例化一个节点
        node = Node(value)
        # 判断是否根节点的后面是否已经有数据了
        # 如果没有数据 就是将传入的数据作为一个根节点后的第一个来进行传入
        if not self.next:
            self.root.next = node # 就是将新的节点挂在root的后面
        else:
            self.next.next = node # 就是将新节点挂到最后的一个节点的后面
        self.next = node
        self.size += 1

    def append_first(self, value):
        # 初始化节点
        node = Node(value)
        # 将新的节点挂到整个的链表的前面
        if not self.next:
            self.root.next = node
            self.next = node
        else:
            temp = self.root.next # 获取原来的root后面的那个节点
            self.root.next = node # 将新的节点挂到root后面
            node.next = temp # 就是将新的节点的下一个节点指向原来root后面的节点
        self.size += 1
    # 遍历一个链表
    def __iter__(self):
        current = self.root.next


def main():
    ...


if __name__ == "__main__":
    main()
