# ai beginning
## 目录
* [软件的安装和基本的配置](#软件的安装和基本的配置)
* [数学基础](#数学基础)
* [python基础](#python基础)
## 软件的安装和基本的配置
* [Anaconda的安装](#Anaconda的安装)
* [python的安装](#python的安装)
* [pytorch的发展和安装](#pytorch的发展和安装)
* [python的包的介绍](#python的包的介绍)
* [相关的基础配置](#相关的基础配置)
* [根据使用的gpu来选择对应的pytorch版本进行安装](#根据使用的gpu来选择对应的pytorch版本进行安装)
* [tensorflow的安装和配置](#tensorflow的安装和配置)
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
* 会生成一个配置文件![jupyter配置文件](./static/img/jupyter_config_file.png)，然后找到配置文件中的#c.NotebookApp.notebook_dir = '' 这一行，然后修改路径即可 之后还要将#给删除
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
### python的包的介绍
* 工具包也称为依赖包、模块、库、包等，是一组可重用的代码，用于解决特定问题或执行特定任务
* python的工具包有很多，比如说numpy、pandas、matplotlib、scikit-learn等
* 主要就是分为内置包和第三方包两种
* 内置包就是python自带的包，比如说os、sys、math等
* 第三方包就是需要我们自己安装的包，比如说numpy、pandas、matplotlib等
* 但是如果想要查看已经安装的库的话，可以使用以下的命令
```shell
pip list
```
* 就可以查看已经安装的库了
### 相关的基础配置
* 虚拟环境
  * 简介
    * 虚拟环境是一个独立的、隔离的、安全的python运行环境
    * 可以在不同的项目中使用不同的python版本和不同的包
  * **通过使用anaconda来创建虚拟环境**
    * 创建虚拟环境
      * 创建一个新的虚拟环境
      ```shell
      conda create -n 虚拟环境的名字 python=版本号
      ```
      * 激活虚拟环境
      ```shell
      conda activate 虚拟环境的名字
      ```
      * 退出虚拟环境
      ```shell
      conda deactivate
      ```
      * 删除虚拟环境
      ```shell
      conda remove -n 虚拟环境的名字 --all
      ```
      * **通过使用virtualenv来创建虚拟环境**
      * 安装virtualenv
      ```shell
      pip install virtualenv
      ```
        * 创建虚拟环境
        ```shell
        virtualenv 虚拟环境的名字
        ```
        * 激活虚拟环境
        ```shell
        source 虚拟环境的名字/bin/activate
        ```
        * 退出虚拟环境
        ```shell
        deactivate
        ```
        * 删除虚拟环境
        ```shell
        rm -rf 虚拟环境的名字
        ```
        * **通过使用venv来创建虚拟环境**
        * 创建虚拟环境
        ```shell
        python -m venv 虚拟环境的名字
        ```
        * 激活虚拟环境
        ```shell
        source 虚拟环境的名字/bin/activate
        ```
        * 退出虚拟环境
        ```shell
        deactivate
        ```
        * 删除虚拟环境
        ```shell
        rm -rf 虚拟环境的名字
        ```
    * 比较常用的方式就是使用anaconda来创建虚拟环境
### 根据使用的gpu来选择对应的pytorch版本进行安装
  * cuda的安装
  * 可以先通过pytorch来查看对应的cuda版本
  * [查看pytorch对应的cuda版本](https://pytorch.org/get-started/locally/)
  * [cuda过往版本下载的链接](https://developer.nvidia.com/cuda-toolkit-archive)
  * pytorch的安装
    * [pytorch](https://pytorch.org/)
    * 下载whl文件 [whl文件](https://download.pytorch.org/whl/torch_stable.html)
    * 也可以通过使用网站下载[pytorch网站的下载链接](https://download.pytorch.org/whl/torch_stable.html)
    * 我的下载版本就是 ![下载版本图片选择](./static/img/cuda_torch_python_system.png) cu对应的版本就是cuda的版本 torch对应的就是torch版本 cp对应的是python版本 win_amd64对应的是系统的版本 还有 ![另外一个版本](./static/img/cuda_torchversion.png)
    * 命名方式 torch-1.7.1+cu110-cp38-cp38-win_amd64.whl
    * cu92/torch-1.7.1+cu92-cp38-cp38-win_amd64.whl 名字的意思就是 pytorch的版本是1.7.1，cuda的版本是9.2，python的版本是3.8，系统是win_amd64
  * 下载cuDNN软件
    * 可以通过使用`nvidia-smi`来查看当前使用的cuda版本
    * 其中CUDA Version表示就是最高支持的cuda版本
    * 需要登录才能进行下载，下载地址 [cuDNN](https://developer.nvidia.com/rdp/cudnn-archive)
  * 当以上的软件都安装完成之后
    1. 首先要将下载的cuda的软件的进行安装 安装完成之后 可以来到安装目录中 打开命令行窗口 之后输入`nvcc --version` 如果显示出版本号 说明安装成功
    2. 然后就是将下载的cuDNN的软件进行解压，然后将解压的文件夹中的bin、include、lib文件夹中的内容复制到cuda的安装目录中
    3. 之后来到extras\demo_suite\文件夹目录中 打开命令行窗口 输入 `bandwidthTest.ext` 如果最后的结果是PASS 就是说明安装成功 通过使用`deviceQuery.exe`来查看gpu的信息
    4. 之后就是可以创建一个项目 比如说是在pycharm中先创建一个项目 然后在项目中创建一个虚拟环境
    5. 创建一个虚拟环境
        * 首先通过 windows + R 打开运行的窗口 然后输入cmd 然后输入以下的命令
        * 创建一个虚拟环境
        ```shell
        conda create -n 虚拟环境的名字 python=版本号
       # 比如 conda create -n pytorch_gpu python=3.12
        ```
        * 然后就是激活虚拟环境
         ```shell
          conda activate 虚拟环境的名字
          # 比如 conda activate pytorch_gpu
         ```
        * 之后就是安装pytorch
        * 首先通过使用`cd 下载torch文件的目录`来进入下载torch软件的目录
        * 然后通过使用以下的命令来安装torch
        ```shell
        pip install torch-1.7.1+cu110-cp38-cp38-win_amd64.whl
       # 输入路径的时候其实只要输入tor之后再输入tab键之后就是可以自动将路径补全了
        ```
       * 安装完成之后 终端的界面就是会显示出先这样的样子![安装成功](./static/img/successful_install_torch.png)
    6. 完成虚拟环境的创建之后 即时可以通过撇孩子pycharm环境解释器来设置虚拟环境的解释器
        * 可以直接通过下面的方式来进行配置![配置解释器](./static/img/config_python_interpreter.png)
    7. 之后进行等待就是可以了 
    8. 然后可以通过使用code文件夹中的check文件夹中的torch_test.py文件来测试是否安装成功
> 创建虚拟环境的一些tips 
> 1. 安装anaconda的时候要都选添加环境变量
> 2. 创建虚拟环境的时候要注意python的版本号
> 3. 为了使得后续的python第三方库安装的速度更快 可以使用国内的镜像源 比如清华的镜像源和中科大的镜像源等
> 4. 配置中科大的源可以使用以下的命令
```shell
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/free/
conda config --set show_channel_urls yes
```
> 5. 配置清华的源可以使用一下的命令 推荐使用清华的镜像源 更加稳定
```shell
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --set show_channel_urls yes
```
> 6. 如果之后创建的虚拟环境一直失败 就是可以使用清除配置的命令将配置清除 来重新设置
```shell
conda config --remove-key channels
```
> 7. 如果想要查看当前的配置的话 可以使用以下的命令
```shell
conda config --show
```
> 8. 如果要删除虚拟环境 就是可以使用下面的命令
```shell
conda remove --name 虚拟环境名字 --all
```
> 9. 如果要查看所有的创建的虚拟环境 就是可以使用一下的命令
```shell
conda info --envs
```
> 10. 如果要跳出当前的虚拟环境 就是可以是会用以下的命令
```shell
conda deactivate
```
> 11. 安装特定版本的cpu版本的pytorch可以使用一下的命令
```shell
pip install torch==1.7.1+cpu -f https://download.pytorch.org/whl/torch_stable.html
```
### tensorflow的安装和配置
* windows安装和下载
* 首先就是简单的CPU版本的安装 但是注意不要在gpu环境下来实现一大非常大的模型项目 可能会导致cpu出现不可挽回的错误
* [tensorflow的官网](https://www.tensorflow.org/install/source_windows?hl=zh-cn)
* 通过使用命令行方式来就进行安装
  * 首先可以通过使用conda来创建一个虚拟的环境
    * ```shell
        conda create -n tensorflow_cpu python=3.8
        ```
    * 之后激活这个虚拟环境
    * ```shell
        conda activate tensorflow_cpu
        ```
    * 然后就是来安装tensorflow 比如安装的就是cpu版本的tensorflow2.0.0
    * ```shell
        # 通过使用清华源来进行安装
        pip install tensorflow==2.0.0 -i https://pypi.tuna.tsinghua.edu.cn/simple
        ```
  * 然后就是来安装gpu版本的tensorflow
  * 首先就是来安装cuda的软件
  * 然后就是来安装cuDNN的软件
  * 然后就是来安装tensorflow
  * ```shell
    # 通过使用清华源来进行安装
    pip install tensorflow-gpu==2.0.0 -i https://pypi.tuna.tsinghua.edu.cn/simple
    ```
  * 个人的设置
  * ```shell
    # 通过使用清华源来进行安装
    pip install tensorflow-gpu==2.2.0 -i https://pypi.tuna.tsinghua.edu.cn/simple
    ```
  * 之后还要安装一个东西 这样就是不会报错了
  * ```shell
    conda install cudatoolkit=10.1.243
    ```
  * 通过使用python来导入库
  * 出现这样的画面就是表示安装成功了 ![安装成功](./static/img/successful_install_tensorflow_gpu.png)
    
