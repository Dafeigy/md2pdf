<p align="center">
    <img src="https://raw.githubusercontent.com/dafeigy/image/master/20210216161025.jpeg" alt="logo"  />
</p>
<h1 align="center">Md2pdF</h1>
<p align="center">
    <em>Typroa什么时候才更新命令行啊</em>
</p>
<p align="center">
    <a>
        <img src="https://img.shields.io/badge/Platform-python-blue.svg" alt="Platform">
    </a>
    <a>
        <img src="https://img.shields.io/badge/Version-0.6.15-red.svg" alt="Version">
    </a>
    <a href="https://github.com/Dafeigy/md2pdf/blob/main/README.md">
        <img src="https://img.shields.io/badge/Readme-Clickhere-yellow.svg" alt="README">
    </a>
    <a href="http://cybercolyce.cn/">
        <img src="https://img.shields.io/badge/Contact-Homepage-brightgreen.svg" alt="Contact">
    </a><p align="center">
    <a href="https://github.com/me-shaon/GLWTPL/blob/master/LICENSE">
        <img src="https://img.shields.io/badge/Build-Cando-purple.svg" alt="Build">
    </a>
    <a href="https://github.com/Dafeigy">
        <img src="https://img.shields.io/badge/Contribution-Wel♂cum-blue.svg" alt="contribution">
    </a>
    <a href="https://github.com/me-shaon/GLWTPL/blob/master/LICENSE">
        <img src="https://img.shields.io/badge/License-GLWT-critical.svg" alt="License">
    </a>
</p>



# ❓这是个什么玩意儿？

这是个将`Markdown`文件转换为PDF的小脚本

# 💡但是我的Typora本来就有导出PDF的功能啊？

是的，但是我们的`Typora`没有把这个功能集成到命令行里，如果你**遇到这种情况**：

<img src="https://raw.githubusercontent.com/dafeigy/image/master/20210216155519.png" style="zoom:67%;" />

你就会很晕对吧？所以这个小脚本支持批量转换`Markdown`为`PDF`。

# 📚那这个是怎么实现的

直接采用Pandoc转PDF的方法不太好使，所以采取了折中的方案：先将`Markdown`用[Pandoc](https://github.com/jgm/pandoc)转换为`HTML`,然后再用[wkhtmltopdf](https://github.com/wkhtmltopdf/wkhtmltopdf)完成PDF转换。

Pandoc转换为HTML~~几乎完美~~，但是需要补充HTML头部以及CSS样式等。所以前端大佬可以直接修改`html_head.txt`中的文件完善。：

## Emoji渲染

emoji方面尝试了三种方式，分别是SegoeUI的字体扩展、jQueryEmoj以及最终确定的twemoji.min.js的方法。

第一种方式得到的是黑白的**Emoji**，第二种和第三中都是用**js**更换**Emoji**为图片，区别是第二种的图片更全面一点。



## 数学公式渲染

采用Mathjax渲染，目前没有更好的方案，转换成pdf时会出现一些神秘的位置小错误，无伤大雅,这里以同样无伤大雅的欧拉公式举例：


$$
e^{\pi i}=-1
$$


## 代码块渲染

没啥好说的,原始代码块，可以自己改CSS，我就摸了

```python
print('摸了')
```

# 🤺说了这么多那我要怎么用

* 安装好Pandoc 和 wkhtmltopdf 环境
* 拷贝需要转换的md文件到该项目文件夹根目录
* python环境下运行

# 🐟Todolist

- [ ] ~~丰富CSS样式~~
- [ ] ~~样式修复~~
- [ ] ~~公式的居中问题~~
- [ ] ~~Emoji的正文自动换行问题~~
- [x] 督促Typora更新



