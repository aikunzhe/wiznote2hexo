# wiznote2hexo
**为知笔记转hexo**
最近把为知笔记同步到hexo博客中，今天写了一个非常简单的脚本帮助我完成迁移任务。


## 依赖环境
- Python3
- bs4库：安装方式 `pip install beautifulsoup4`
- hashlib库：安装方式 `pip install hashlib`



## 使用方式：
把笔记另存为 htm格式：
![](index_files/a7cc71bb-ee2c-4004-83e8-4483120a511a.png)
![](index_files/6e49ea83-1ef6-44f4-b823-8d437ee89e6c.png)
此时会有2个文件夹：
![](index_files/0092d583-c7e6-4106-9d1e-686495fc6deb.jpg)




## 运行脚本
**修改file_path的路径**
![](index_files/8b92cca7-051e-42c1-8c30-51c5b21551cf.png)
**运行脚本：**
![](index_files/2b89c06e-690c-4ed6-9725-84f1737408cb.png)
得到一个同名的md文件，把md文件、文件夹一起复制到hexo的source文件夹中，就可以了。
![](index_files/c26721b4-9ed4-48b5-837c-767fd3c83b42.jpg)

