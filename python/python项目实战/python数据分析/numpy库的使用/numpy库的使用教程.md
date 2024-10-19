# numpy使用库的教程
## 目录
* [简单的介绍](#简单的介绍)
* [基础的使用](#基础的使用)

## 简单的介绍
* numpy是一个开源的python数据科学的计算的库 
* 提供了一个多维数组对象以及多种派生对象 可以进行快速的创建和计算数组的操作
* numpy是一个基于C语言的库 速度非常快
* numpy的核心就是ndarray对象 用于存储多维数组的对象 以及一系列的操作数组的函数
* 如何安装?
    * 通过官网来查看方法 [numpy官方网站](https://numpy.org/)
    * 通过使用命令行来安装 `pip install numpy` 或者 `conda install numpy`

## 基础的使用
### 目录
* [创建数组](#创建数组)
* [数组的属性](#数组的属性)
* [数组的运算](#数组的运算)
* [数组的索引](#数组的索引)
* ...
### 创建数组
* [通过具体的数据来创建数组](#通过具体的数据来创建数组)
* [通过使用numpy的函数来创建数组](#通过使用numpy的函数来创建数组)
#### 通过具体的数据来创建数组 
* 方式一 通过具体的数据来创建数组 通过使用 numpy.array(列表 或者 元祖)创建数组
* 比如 `a = numpy.array([1, 3, 4, 5])`或者`a = numpy.array((1, 3, 4, 5))`
#### 通过使用numpy的函数来创建数组
* 函数一 使用zeros和ones和full创建数组
    * zeros函数就是创建一个全是0的数组
    * ones函数就是创建一个全是1的数组
    * full函数就是创建一个全是指定值的一个数组
    * 比如 `a = numpy.zeros(5)` 或者 `a = numpy.ones(5)`
    * 括号内容就是数组的维度
* 函数二 使用arange和linspace和logspace创建数组
    * arange函数就是创建一个等差数列的数组
    * linspace函数就是创建一个等差数列的数组
    * logspace函数就是创建一个对数等差数列的数组 通过使用base指定底数
    * 比如 `a = numpy.arange(5)` 或者 `a = numpy.linspace(0, 10, 5)`
    * 括号内容就是数组的维度
* 函数三 使用random函数创建随机数数组
    * 使用numpy.random.randint(low, high, size)创建一个随机数数组
    * 使用numpy.random.random(size)创建一个0-1之间的随机数数组
    * 使用numpy.random.randn(size)创建一个正态分布的随机数数组
    * 现在还有一种可以通过使用生成器的方式来创建随机数组 
    * 首先通过使用 `numpy.random.default_rng(随机数种子)`来创建一个生成器
* 将创建的数组保存到文件中 文件的后缀名称就是.npy
  * 使用numpy.save('文件名', 数组)来保存数组到文件中
  * 使用numpy.load('文件名')来加载文件中的数组
