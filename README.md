# ai beginning
## 目录
* [软件的安装](#软件的安装)
* [数学基础](#数学基础)
* [python基础](#python基础)
## 软件的安装
* [Anaconda的安装](#Anaconda的安装)
* [python的安装](#python的安装)
### Anaconda的安装
* 首先就是人工智能的必备的软件 Anaconda 的安装
* 安装的地址 [Anaconda](https://www.anaconda.com/products/individual)
* 安装的过程中需要注意的是，安装的时候需要勾选上添加到环境变量中
* 安装完成后，需要打开Anaconda的命令行，输入以下命令
```shell
conda --version
```
* 如果显示出版本号，说明安装成功
* 如果没有显示出版本号，需要重新安装
* 安装成功之后 就是可以使用Anaconda中的一些功能了 比如说是notebook 等 
* 但是notebook的默认的路径一般是在C盘，如果想要修改路径的话，可以使用以下的命令
```shell
jupyter notebook --generate-config
```
* 会生成一个配置文件，然后找到配置文件中的#c.NotebookApp.notebook_dir = '' 这一行，然后修改路径即可 之后还要将#给删除
* 但是如果没有找到这一行的话, 可以在查看是否有# c.ServerApp.root_dir = '' 将'' 的内容修改成为你想要的路径即可
* 之后就可以使用jupyter notebook 来打开notebook了
### python的安装
* python的安装就比较简单了，直接去官网下载安装即可
* 安装的地址 [python](https://www.python.org/)
* 安装完成之后，需要打开命令行，输入以下命令
```shell
python --version
```
* 如果显示出版本号，说明安装成功
* 如果没有显示出版本号，需要重新安装
* 安装成功之后，就可以使用python的一些功能了
* 但是需要注意的是，python的版本最好是3.7以上的版本
* 之后就可以使用python的一些功能了
* 但是如果想要使用一些第三方的库的话，可以使用pip来安装
* 比如说安装numpy库的话，可以使用以下的命令
```shell
pip install numpy
```
* 安装完成之后，就可以使用numpy了
* 但是如果想要卸载的话，可以使用以下的命令
```shell
pip uninstall numpy
```
* 就可以卸载了
* 但是如果想要查看已经安装的库的话，可以使用以下的命令
```shell
pip list
```
* 就可以查看已经安装的库了
* 但是如果想要查看某一个库的版本的话，可以使用以下的命令
```shell
pip show numpy
```
* 就可以查看numpy的版本了
* 但是如果想要升级的话，可以使用以下的命令
```shell
pip install --upgrade numpy
```
* 就可以升级了
* 但是如果想要安装指定的版本的话，可以使用以下的命令
```shell
pip install numpy==1.18.5
```
* 就可以安装指定的版本了
* 但是如果想要安装的时候不显示过程的话，可以使用以下的命令
```shell
pip install numpy -q
```
* 就可以安装的时候不显示过程了
### pytorch的发展和安装
* pytorch是一个开源的深度学习框架，是一个非常强大的框架
* 它的发展是非常迅速的，现在已经是一个非常强大的框架了
* 它的安装也是非常简单的，可以直接去官网下载安装即可
* 安装的地址 [pytorch](https://pytorch.org/)
* 安装完成之后，可以使用以下的命令来测试是否安装成功
```shell
import torch
print(torch.__version__)
```
* 如果显示出版本号，说明安装成功
* 如果没有显示出版本号，需要重新安装
* 之后就可以使用pytorch的一些功能了
* 可以可以直接通过命令行的方式来安装
```shell
pip install torch
```
* 但是如果想要安装指定的版本的话，可以使用以下的命令
```shell
pip install torch==1.7.1
```
* 就可以安装指定的版本了
* pytorch的优点
  1. 上手快
  2. 代码简介灵活
  3. debug方便
  4. 文档规范 [pytorch中文文档](https://pytorch.apachecn.org/docs/1.0/) [pytorch英文文档](https://pytorch.org/docs/stable/index.html)
  5. 开发者多
  6. 由facebook维护和开发
