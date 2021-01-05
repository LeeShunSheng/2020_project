# 2020_project
2020年开源软件基础大作业

* 组长是个~~二次元~~，喜欢打音游。基于这些诞生了这个项目
* 主要功能为
  1.  访问 https://osu.ppy.sh/rankings/mania/country 获取表格中的数据
  2.  将取得的数据存入数据库并生成图片，保存
  3.  利用Flask将数据库中的数据以及图片进行展示
* 另外，由于头一眼看上去感觉东西有点少就又给加了几个小功能，目前有
  1.  实现查看实时百度热搜功能
  2.  在主页塞进去一首我很喜欢听的歌~~我不是车万人~~
  
## 运行方法
* 下载完成后，在F-work.py文件所在目录下打开cmd窗口运行如下命令
  1.  set FLASK_APP=F-work.py
  1.  flask run
* 然后按照提示在浏览器中输入网址即可

##  注:
  1.  由于种种原因爬取到的热搜结果可能与实际不符，详见F-work.py代码注释。
