"""
1 在实际爬取百度热搜时发现存在不同的结果。程序中的热搜可能与百度显示出的热搜存在不同
2 热搜有时候打不开……不太清楚其中的奥妙
3 希望每个人都能在帮主页面得到帮助
4 最近发现一首歌很好听就加进来了
"""

import sqlite3
import os
from flask import Flask, send_file
import requests
import re

app = Flask(__name__)

header = {
    "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"
}
url = "https://www.baidu.com/"


@app.route('/ScoreChart')
def scoretable():
    conn = sqlite3.connect('OSUdatabase.db')
    c = conn.cursor()
    print("连接成功")
    result = c.execute("select * from FOSU")
    stra = '<html><head><title>OSU不同地区得分统计</title></head><body><center><a href="/">返回首页</a><br>' \
           '<table border="1" cellspacing="0" width="450px"><tbody><tr><th>排名</th><th>国家/地区</th><th>Rank得分</th><th' \
           '>平均得分</th><tr> '
    strb = str()
    for i in result:
        strb = strb + '<tr><td>'+str(i[0])+'</td><td>'+i[1]+'</td><td>'+i[2]+'</td><td>'+i[3]+'million'+'</td><tr>'
    strc='</tbody></center></body></html>'
    strtable = stra+strb+strc
    print("正在访问得分统计表")
    return strtable


@app.route('/AverageScorePicture')
def scorepic():
    PROJECT_ROOT = os.path.dirname(os.path.relpath(__file__))
    path = os.path.join(PROJECT_ROOT, "Average_Score.jpg").replace('\\', '/')
    print("当前正在访问平均得分图片")
    return send_file(path)
    
    
@app.route('/show')
def tables():

    conn = sqlite3.connect("mydate.db")
    c = conn.cursor()
    print("连接成功")
    result = c.execute("select * from FOSU")
    strf = '<html><head><title>FOSU数据统计</title></head><body><center><a href="/">返回首页</a><br>' \
           '<table border="1" cellspacing="0"><tbody><tr><th>国家/地区</th><th>玩家数量</th></tr>'
    strb = str()
    for i in result:
        strb = strb + '<tr><td>'+i[0]+'</td><td>'+str(i[1])+'</td><tr>'
    stre = '</tbody></center></body></html>'

    table = strf+strb+stre
    print("当前正在访问统计页面")
    return table


@app.route('/picture')
def show_picture():
    PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))  # 获取项目根目录
    path = os.path.join(PROJECT_ROOT, "OSU.jpg").replace('\\', '/')
    print("当前正在访问图片页面")
    return send_file(path)


@app.route('/heat')
def baidu_heat():
    request = requests.get(url, headers=header)
    if request.status_code == 200:
        print("running……")
        request.encoding = request.apparent_encoding
        html = request.text.replace("&quot", '\'')
        title = re.findall(r'\"pure_title\": \"(.*?)\"', html)
        heat_score = re.findall(r'\"heat_score\": \"(.*?)\"', html)
        start = '<html><head><title>百度热搜</title></head><body><center><a href="/">返回首页</a><br><br><br><br>' \
                '<table border="1" cellspacing="0"><tbody><tr><th>位次</th><th>标题</th><th>热度</th></tr>'
        mid = str()
        for i in range(15):
            mid = mid + '<tr><td>' + str(i+1) + '</td><td><a href="http://www.baidu.com/s?ie=utf-8&wd=' \
                  + title[i] + '"/>' + title[i] + '</td><td>' + str(heat_score[i])+'</td></tr>'
        ends = '</tbody></center></body></html>'
        table = start + mid + ends
        print("当前正在访问百度热搜界面")
        return table


@app.route('/')
def homepage():
    start = '<html><head><title>homepage</title></head<body><center><br><br>'
    url1 = '<a href="/picture">OSU玩家分布的图片</a><br>'
    url2 = '<a href="/show">OSU玩家分布的表格</a><br>'
    url3 = '<a href="/heat">现在的百度热搜</a><br>'
    url4 = '<a href="/ScoreChart">OSU得分前十统计表</a><br>'
    url5 = '<a href="/AverageScorePicture">OSU得分前十平均得分条形图</a><br>'
    url6 = '<iframe frameborder="1" marginwidth="0" marginheight="0" width=330 height=86 src="https://music.163.com/outchain/player?type=2&id=32958602&auto=1&height=66"></iframe><br>'
    url7 = '<a href="/help">帮助</a><br>'
    end = '</center></body></html>'
    print("当前正在访问主页")
    return start+url1+url2+url3+url4+url5+url6+url7+end


@app.route('/help')
def help_page():
    start = '<html><head><title>help</title></head<body><center><br><br>'
    url1 = '<a href="https://www.baidu.com">点击这里获得帮助</a><br>'
    url2 = '<b>很高兴你能点击这个页面，我们为寻求帮助的人提供了上方这个链接，请毫不犹豫的点下吧！</b>'
    end = '</center></body></html>'
    return start + url1 + url2 + end
