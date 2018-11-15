# encoding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import requests
import time
from bs4 import BeautifulSoup
import json
import csv

print (sys.getdefaultencoding())

with open(r'data.csv',"w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['网站名','类别','商家名称','地址','人均消费','缩略图','评分'])
        target = 'http://km.meituan.com/meishi/'
        head={}
        head['authorization']='your ClientID'
        head['User-Agent'] = ''
        req = requests.get(url=target,headers=head)
        html=req.text
        bf=BeautifulSoup(html,'lxml')
        texts=bf.find_all('script')
        text=texts[14].get_text().strip()
        text=text[19:-1]
        result=json.loads(text)
        result=result['filters']
        result=result['areas']
        list=[]
        for item in result:
            for i in item['subAreas']:
                if i['name']=='全部':
                    continue
                list.append(i['id'])
        print(list)
        for item in list:
            for i in range(50):
                if i==0:
                    continue
                target='http://km.meituan.com/meishi/'+'b'+str(item)+'/'+'pn'+str(i)+'/'
                head={}
                head['authorization']='your ClientID'
                head['User-Agent'] = ''
                req = requests.get(url=target,headers=head)
                html=req.text
                bf=BeautifulSoup(html,'lxml')
                texts=bf.find_all('script')
                text=texts[14].get_text().strip()
                text=text[19:-1]
                result=json.loads(text)
                result=result['poiLists']
                result=result['poiInfos']
                print result
                if result:
                    print(target)
                    for it in result:
                        Info_list=[]
                        Info_list.append('美团')
                        Info_list.append('美食')
                        Info_list.append(it['title'])
                        Info_list.append(it['address'])
                        Info_list.append(it['avgPrice'])
                        Info_list.append(it['frontImg'])
                        Info_list.append(it['avgScore'])

                        
                        writer.writerow(Info_list)
                    # time.sleep(3)
                else:
                    break
print('Done')

