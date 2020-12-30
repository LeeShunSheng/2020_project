'''
实现 1 从指定网站获得数据
    2 将获得的数据保存至数据库
    3 将获得的数据通过统计以图片的形式展示

怎么说呢……request.get(url)特别慢。但是运行几次就不慢了，不知道为啥。
建议与数据库文件一起下载。当初建立数据库的人已经忘了自己是怎么写的create table了。
'''
import requests
import bs4
import matplotlib.pyplot as plt
import sqlite3

header = {
    "cookie": "_ga=GA1.2.680209622.1582863761; XSRF-TOKEN=uZqvhz3hXAlt82NBqDY9gNYGVfZh8BaDCK0OAvh0; __cfduid=dc148c4d4bdae2ce8a681d968476794141607134484; osu_session=eyJpdiI6InJnNFV3SllMbTdvNFVjeDVtUnlLa0E9PSIsInZhbHVlIjoibkhcL0x2b2dueWJFbVgxcXdmY2lUMlg0Z0FvNzRScTR1MHhlNHdZblwvTmJVbjNsaXpNWjFBMURlckNXMCt6aDNCUkd6OE8wdDNmbDNWak15T1NSeVhiUT09IiwibWFjIjoiYzA3NTgzNmJhNGU3ZmEwN2Q1ZDY2MDljMTcyNGU4NDZmZjVkZTc2NzhmMDljYjQ2NDI5OWZmMTQwMTFiZTI0MCJ9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}

url = "https://osu.ppy.sh/rankings/mania/country"
print("在运行了，在运行了。")
res = requests.get(url, headers = header)
if res.status_code == 200:
    res.encoding = res.apparent_encoding
    doc = bs4.BeautifulSoup(res.text, features="html.parser")
    table = doc.find("tbody")
    lables = list()
    dates = list()
    conn = sqlite3.connect("mydate.db")
    c = conn.cursor()
    conn.execute("delete from FOSU")
    for tr in table.find_all("tr"):
        tds = tr.find_all("td")
        countries = tds[1].text.replace('\n', '').replace(' ', '')
        users = int(tds[2].text.replace('\n', '').replace(' ', '').replace(',', ''))
        lables.append(countries)
        dates.append(users)
        c.execute("INSERT INTO FOSU (COUNTRY,NUMS) VALUES (?, ?)", (countries, users))
    conn.commit()
    fig = plt.figure(figsize=(20, 20))
    plt.pie(dates, labels= lables, autopct='%1.2f%%')#
    plt.title("OSU players")
    plt.savefig("OSU.jpg")
    print("已完成,感谢您的耐心等待")
else:
    print("连接失败")
