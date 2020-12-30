import requests
import bs4
import sqlite3
import matplotlib.pyplot as plt

url = 'https://osu.ppy.sh/rankings/mania/country'
html = requests.get(url)
if html.status_code == 200:  # 查看请求状态码 200 表示正常运行
    html.encoding = html.apparent_encoding  # 设置编码格式
    # print(html.text)
    doc = bs4.BeautifulSoup(html.text, "html.parser")
    table = doc.find("tbody")
    ranks = list()
    areas = list()
    rankscores = list()
    avgscores = list()
    conn = sqlite3.connect('OSUdatabase.db')
    c = conn.cursor()
    c.execute("delete from FOSU")
    i = 0
    for tr in table.find_all("tr"):
        if i >= 10:
            break
        tds = tr.find_all("td");
        rank = int(tds[0].text.replace('\n', '').replace(' ', '').replace('#', ''))
        area = tds[1].text.replace('\n', '').replace(' ', '')
        rankscore = tds[4].text.replace('\n', '').replace(' ', '')
        avgscore = tds[5].text.replace('\n', '').replace(' ', '').replace('million', '')
        areas.append(area)
        ranks.append(rank)
        rankscores.append(rankscore)
        avgscores.append(float(avgscore))
        c.execute("INSERT INTO FOSU (RANK,COUNTRY,RANKSCORE,AVGSCORE) VALUES(?,?,?,?)",
                  (rank, area, rankscore, avgscore))
        i = i + 1
    conn.commit()
    conn.close()
    fig = plt.figure(figsize=(15, 8))
    # 解决中文乱码
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.bar(areas, avgscores, width=0.5)
    xlocs = plt.xticks()
    # xlabs = plt.xticks()
    xlocs = [i for i in range(0, 10)]
    # xlabs = [i / 2 for i in range(0, 10)]
    plt.xlabel("地区名称")
    plt.ylabel("玩家平均得分/million")
    plt.title("不同地区玩家平均得分图")
    plt.savefig("Average_Score.jpg")
    plt.xticks(xlocs)
    for i, v in enumerate(avgscores):
        plt.text(xlocs[i] - 0.15, v + 0.50, str(v))
    plt.show()
else:
    print("连接失败")
