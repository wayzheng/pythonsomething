# -*- encoding: utf-8 -*-
"""

PyCharm 多态.py
2024年10月17日19时59分
by wenyang

"""
# 多态就是调用方法的时候 要看这个对象是父类创建的对象还是子类创建的对象 而不一定非得调用是子类或者是父类
# 创建一个父类
class MiniOS(object):
    def __init__(self, name):
        self.name = name
        self.apps = []

    def __str__(self):
        return f"{self.name}上安装的软件有{self.apps}"
    def install_app(self, app):
        if app.name in self.apps:
            print(f"{app.name}已经安装了")
        else:
            # 首先会判断这个app是不是App的实例  如果子类有这个install方法就会使用子类的方法 如果子类没有就是会调用父类的install方法
            app.install()
            self.apps.append(app.name)
            print(f"{app.name}安装成功")
class App(object):
    def __init__(self, name, version, desc):
        self.name = name
        self.version = version
        self.desc = desc

    def __str__(self):
        return f"{self.name}的当前版本就是{self.version}, {self.desc}"

    def install(self):
        print(f"将{self.name}[{self.name}]的执行程序复制到程序目录中...")

class Pycharm(App):
    # 此时就是会重写父类的install方法
    def install(self):
        print(f"正在解压安装程序")
        super().install()
# 此时就是继承了App类的所有的属性和方法
class Chrome(App):
    pass
def main():
    pycharm = Pycharm("pycharm", "1.0", "python的IDE")
    chrome = Chrome("chrome", "1.0", "浏览器")
    linux = MiniOS("linux")
    linux.install_app(pycharm)
    linux.install_app(chrome)
    print(linux)



if __name__ == "__main__":
    main()
