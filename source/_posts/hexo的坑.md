---
title: hexo的坑
date: 2020-03-20 02:21:39
tags:
---

主要记录了利用hexo搭建博客遇到的各种问题，尝试给出解决办法，但是往往因为没法复现搁置了。挖坑以后再补。

<!-- more -->
## Github同步
hexo自带的`hexo d`能将本地文件上传到github上，然后实现网页更新。但是上传的其实是输入`hexo d`后生成的 **/.deploy_git**文件夹，整个源文件并没有上传到github。这就导致未来多设备更新网页的不便。一个常见的解决办法是新建分支，利用git将源文件保存到新分支上（将整个项目当成普通工程用git来管理）。不过这就意味着每次`hexo d`后都要再做一遍`git push`的操作，才能达到备份的效果，有点不够直接。知乎上的[这个回答](https://www.zhihu.com/question/21193762/answer/172097576)非常简单的解决了同步的功能。

不过这个回答的细节没有写得很清楚，还是让silly me折腾了一会儿。关键在于：按照他的方法上传后，其实从我们新建的那个库就可以直接重现网页。

首先在github上设置新增的分支为默认分支。然后假设我们在一台新电脑上，想要修改网页。那么在工作文件夹目录下输入

    git clone yourRepositoryURL 

然后输入

    npm install (大概是这个吧)
（不要使用`hexo init`，那样会生成新的config_yml文件。）然后再试试`hexo d`，现在应该能成功上传了。这就说明我们已经可以在这台新设备上开始干活了！

如果上传报错的话，玄学的办法是删除deploy_git文件夹以及改一改comfig_yml文件里面deploy的参数，不知道为什么突然就好了，有待进一步研究。~~其实是不想再花时间研究这个劳什子玩意儿了。~~



## 免密登录
这个其实很简单，网上方法也写得很多。生成ssh公钥填到github网站上，config.yml文件里deploy设置里的repo用ssh URL。其他就没啥问题了。


## 插入图片
这是使用绝对路径插入的图片。

    ![](hexo的坑/kyaru.png)

![](hexo的坑/kyaru.png)

这是使用标签语法插入的图片。

    {% asset_img hexo的坑/kyaru.png This is an image %}

{% asset_img hexo的坑/kyaru.png This is an image %}

这是使用图床插入的图片。

    ![](https://s1.ax1x.com/2020/03/22/8ITfIO.png)

![](https://s1.ax1x.com/2020/03/22/8ITfIO.png)

图床链接：
https://imgchr.com/i/8ITfIO

插入图片试验了base64（太长；不显示），本地图片插入（不显示），最后还是屈服于网络图床。关于本地图片直接插入，这里有个写的[挺好的博客](https://myfavs.win/2019/08/08/%E8%AE%B0%E5%BD%95-Hexo-%E5%9B%BE%E7%89%87%E7%9A%84%E5%9D%91/)，可惜我按它说的做还是没效果。