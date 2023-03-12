# @Time:2022/1/1311:42
# @Author:中意灬
# @File:斗破1.py
# @ps:tutu qqnum:2117472285
import time
import requests
from lxml import etree
from concurrent.futures import ThreadPoolExecutor

def download(url,title):
    resp=requests.get(url)
    resp.encoding='utf-8'
    html=resp.text
    tree=etree.HTML(html)
    body = tree.xpath("/html/body/div/div/div[4]/p/text()")
    body = '\n'.join(body)
    with open(f'斗破1/{title}.txt',mode='w',encoding='utf-8')as f:
        f.write(body)
        
def geturl(url):
    resp = requests.get(url)
    resp.encoding = 'utf-8'
    html = resp.text
    tree = etree.HTML(html)
    lis = tree.xpath("/html/body/div[1]/div[2]/div[1]/div[3]/div[2]/ul/li")
    return lis

if __name__ == '__main__':
    url="https://www.doupo321.com/doupocangqiong/"
    t1=time.time()
    lis=geturl(url)
    with ThreadPoolExecutor(1000)as t:#创建线程池，有1000个线程
        for li in lis:
            href = li.xpath("./a/@href")[0].strip('//')
            href = "http://" + href
            title = li.xpath("./a/text()")[0]
            t.submit(download,url=href,title=title)
    t2=time.time()
    print("耗时：",t2-t1)