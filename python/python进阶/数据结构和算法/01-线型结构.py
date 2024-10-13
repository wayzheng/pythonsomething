# 构建线型结构
class Array(object):
    # 初始化
    def __init__(self, size=32):
        self.__size = size # 记录容器的大小
        self.__item = [None] * size # 分配空间
        self.__length = 0
    # 设置值
    def __setitem__(self, key, value):
        self.__item[key] = value
        self.__length += 1
    # 获取数据
    def __getitem__(self, index):
        return self.__item[index]
    # 获取长度
    def __length__(self):
        return self.__length
    # 设置迭代
    def __iter__(self):
        for value in self.__item:
            yield value

if __name__ == "__main__":
    a1 = Array(10)
    a1[0] = "hello world"
    a1[1] = "孙悟空"
    print(a1[0])
    print(a1[1])
    print(a1.__length__())
    print("*" * 10)
    for i in a1:
        print(i)
