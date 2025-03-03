# 先导课程

***

## 自问自答

### 我们用什么工具？📏

#### 如何分布式协作？
* **Git**：Git是一个分布式版本控制系统，用于跟踪代码的更改，并允许多个开发者在单个项目中进行协作。    
下载链接：https://git-scm.com/downloads
* **GitHub**：GitHub是一个托管代码的网站，用于存储和分享代码，并允许开发者进行版本控制。
仓库地址：https://github.com/WFCT-Share/Code-Pipeline-Train  
注册并加入仓库成为协作者吧
* **GitHub Issues**：GitHub Issues是一个用于跟踪项目问题的平台，可以创建、查看和评论问题。  
仓库Issues：https://github.com/WFCT-Share/Code-Pipeline-Train/issues

#### 如何进行高效沟通？
* **diagrams**：diagrams是一个用于创建 diagrams 的在线网页，支持将GitHub仓库作为协作的云存储，可以轻松地创建流程图、 UML 类图、时序图、状态图、ER 图等。  
链接：https://app.diagrams.net/
* **Markdown**：Markdown是一种轻量级的标记语言，用于创建格式化文本，并支持多种格式，如标题、列表、链接等，可以快速创建README.md文件，方便快速记录信息。  
官方学习文档（中文版）：https://markdown.com.cn/

#### 使用什么编程工具？
```python
"""本项目基本使用纯python语言进行开发，方便大家进行协作。虽然会遇到一些困难，但是方法总比困难多。😉"""
```

* **Visual Studio Code**：Visual Studio Code是一个开源的代码编辑器，支持多种编程语言，并具有丰富的扩展功能。  
下载链接：https://code.visualstudio.com/download
* **Pycharm Professional**：Pycharm Professional是一个用于 Python 开发的集成开发环境，具有丰富的扩展功能和调试功能。  
下载链接：https://www.jetbrains.com/pycharm/download/#section=windows
* **Anaconda**：Anaconda是一个开源的 Python 的容器管理器，用于管理依赖和维护开发环境。  
下载链接：https://www.anaconda.com/products/individual
* **通义灵码**：通义灵码是一个阿里推出的代码补全大模型，可以作为扩展安装在 VS code和pycharm中，可以快速补全代码，提高开发效率，最适合中文宝宝的代码补全大模型。😇  
下载方式请查看链接：https://lingma.aliyun.com/lingma/download

### 如何快速开始？🚀
* 第一步：先注册一个GitHub账号，然后加入仓库成为协作者。
* 第二步：下载并安装git，并配置好用户名和邮箱。  
大模型提示词：
```text
如何在git中配置好用户名和邮箱，并且无需每次都配置，以及设置全部目录为安全目录
```
终端代码：
```shell
git config --global user.name "你的用户名"
git config --global user.email "你的邮箱"
git config --global --add safe.directory '*'
git config --global --list
```
* 第三步：下载并安装anaconda，创建一个python3.11的容器
大模型提示词：
```text
如何使用anaconda创建一个python3.11的容器，并且设置每次默认打开此容器
```
终端代码：
```shell
conda create -n <容器名字> python=3.11 -y
conda activate <容器名字>
conda config --set auto_activate_base False  # 先禁用 base 环境的自动激活（可选）
conda config --set default_env <容器名字>
```
* 第四步：下载并安装IDE：Visual Studio Code或者Pycharm Professional，并安装通义灵码插件

* 第五步：配置好IDE的python解释器，运行你的`Hello World`
* 大模型提示词：
```text
如何在python中创建一个hello world程序
```
```python
print("Hello World")
```

### 如何开始分布式协作？😀
* 第一步：使用git clone下本仓库
大模型提示词
```text
如何用git clone下这个仓库https://github.com/WFCT-Share/Code-Pipeline-Train.git
```
终端代码：
```shell
git clone https://github.com/WFCT-Share/Code-Pipeline-Train.git
cd Code-Pipeline-Train
```
* 第二步：使用git branch 创建你的分支
大模型提示词：
```text
如何使用git branch 创建分支
```
终端代码：
```shell
git branch <你的分支名>
git checkout <分支名>
```
* 第二步：使用git add 添加你的文件（可选）
大模型提示词：
```text
如何使用git add 添加你的文件
```
终端代码：
```shell
git add <你的文件路径>
```
* 第三步：使用git commit 提交你修改过的文件:
大模型提示词：
```text
如何使用git commit 提交你修改过的文件
```
终端代码：
```shell
git commit -m "你的提交信息"
```
* 第四步：使用git push 推送你的修改到远程仓库
提示词：
```text
如何使用git push 推送你的分支到远程仓库
```
终端代码：
```shell
git push origin <当前分支名>
```

* 第五步：发起一个pull request，等待审核，完成你的开始
在以下网页发起PR：https://github.com/WFCT-Share/Code-Pipeline-Train/compare
* 更多：询问AI：为我介绍使用GitHub和git进行分布式协作的全流程