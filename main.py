import time
from urllib.request import urlopen, Request
from urllib import parse
import requests
from bs4 import BeautifulSoup
import json
import math
# url1 = "https://m.land.naver.com/complex/getComplexArticleList?hscpNo=107513&cortarNo=1168010300&page=1"
# url1 = "https://m.land.naver.com/complex/getComplexArticleList?hscpNo="
# hscpNo = "107513"
# cortarNo = "1168010300"
# url = url1 + hscpNo + "&cortarNo=" + cortarNo + "&page="

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
limit = 20
page = 0
for i in range(1,10):
    url1 = "https://m.land.naver.com/complex/getComplexArticleList?hscpNo="
    hscpNo = "144187"
    cortarNo = "4311311400" #청주더샵
    # hscpNo = "107513"
    # cortarNo = "1168010300" #개포상지리츠빌
    hscpNo = "818"
    cortarNo = "1168010300"  # 개포우성8차
    url = url1 + hscpNo + "&cortarNo=" + cortarNo + "&page="
    url+=str(i)
    res = requests.get(url, headers=header)
    # time.sleep(3)
    res.raise_for_status()
    bsObject = BeautifulSoup(res.text, "html.parser")
    jsonObject = json.loads(bsObject.text)
    total = int(jsonObject['result']['totAtclCnt']) #전체 매물 수
    page = math.ceil(total/limit) # 페이지 수
    cnt = 0 # 한 페이지당 매물 수
    if i > page or len(jsonObject['result']['list']) == 0: break    # 매물 페이지가 넘어가거나 list에 아무 매물이 없으면 멈춤

    print("총 매물 수:", total)
    if page > 1 :
        if i != page: cnt = limit
        else: cnt = total % limit
    else: cnt = total
    for j in range(cnt) :
        print(f"매물",limit*(i-1)+j+1)
        name = jsonObject['result']['list'][j]['atclNm']
        tradeType = jsonObject['result']['list'][j]['tradTpNm']
        spc1 = float(jsonObject['result']['list'][j]['spc1'])
        spc1_p = round(spc1 * 0.3025, 1)
        spc2 = float(jsonObject['result']['list'][j]['spc2'])
        spc2_p = round(spc2 * 0.3025, 1)
        price_str = jsonObject['result']['list'][j]['prcInfo']

        print(name)
        print(tradeType)
        print(price_str)
        print("평형: ", spc1_p, "평")
        print("전용평형: ", spc2_p,"평")

        price = 0
        for k in range(len(price_str)) :
            if price_str[k] == "억" :
                price = int(price_str[0:k])*100000000
            elif price_str[k] == "/"  :
                print(price_str[k+1:len(price_str)])
            elif price_str[k] == " ":
                print(price_str[k + 1:len(price_str)])
                break





        print(("\n"))


# bsObject = BeautifulSoup(res.text, "html.parser")
# print(bsObject.text)  # 웹 문서 전체가 출력됩니다.



