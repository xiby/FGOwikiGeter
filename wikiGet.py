import urllib.request
import urllib.parse
import requests
import json
import re
from bs4 import BeautifulSoup

import MySQLdb

import getpass

def getHTML(url):
    ret=requests.get(url).content
    ret=ret.decode('utf-8')
    return ret

def findans(html):
    info=BeautifulSoup(html,'html.parser')
    ans=info.findAll("script")
    for ans_part in ans:
        ansString=str(ans_part.string)
        ansList=ansString.split('\n')
        for item in ansList:
            pattern=re.compile(u'var datadetail = (.*?);$')
            ret=pattern.findall(item)
            if ret!=[]:
                infoJSON=json.loads(ret[0])
                return infoJSON[0]
    
    return None

if __name__=='__main__':
    baseurl='https://fgowiki.com/guide/petdetail/'
    psw=getpass.getpass('输入您的数据库密码：')
    db=MySQLdb.connect('localhost','root',psw,'servent',charset='utf8')
    cursor=db.cursor()
    for i in range(1,209):
        newurl=baseurl+str(i)
        html=getHTML(newurl)
        ansdict=findans(html)
        print(ansdict['ID'],ansdict['NAME'],ansdict['CLASS'],ansdict['STAR'])
        sql="insert into servent(ID,SNAME,SCLASS,STAR) values("+"'"+ansdict['ID']+"'"+','+"'"+ansdict['NAME']+"'"+','+"'"+ansdict['CLASS']+"',"+ansdict['STAR']+')'
        try:
            cursor.execute(sql)
            db.commit()
        except:
            print('开始回滚')
            db.rollback()
    db.close()


