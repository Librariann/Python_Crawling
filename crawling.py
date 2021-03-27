#!/usr/bin/env python
# coding: utf-8

# In[53]:


from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import pandas as pd
import urllib.parse


#  PC Version

# 네이버 검색 후 검색 결과 URL
baseUrl = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=view&query='
plusUrl = []  # 입력한 키워드 담아두는 list
plusUrl = input('검색어를 입력하세요 : ').split()  # 키워드를 띄어쓰기로 구분하여 배열에 저장한다
dataset = []  # 엑셀 데이터 담아두는 list

# 키워드 갯수로 for문 돌림
for a in plusUrl:
    # 현재 키워드
    print("--------------"+a+"--------------")  # 구분선
    url = baseUrl + urllib.parse.quote_plus(a)  # 키워드로 검색한 url
    print(url)  # url 출력
    html = urlopen(url)
    bsObject = bs(html, "html.parser")

    # 키워드로 검색한 리스트에서 view section list
    wrap = bsObject.select('._svp_item')

    for i in wrap:
        if len(i.select('.source_inner > .link_ad')) != 0:
            total_tit = i.select('.total_tit')
            company_name = i.select('span.name')
            for j in total_tit:
                print()
                for c in company_name:
                    print("제목 : " + j.get_text())
                    print("업체명 : " + c.get_text())
                    print("URL : " + j['href'])
                    dataset.append([a, j.get_text(), c.get_text(), j['href']])
                print()
    # 엑셀변환
    df = pd.DataFrame(dataset, columns=['키워드', '제목', '업체명', 'URL'])
    writer = pd.ExcelWriter('excel_test.xlsx', engine='xlsxwriter')  # 엑셀파일명
    df.to_excel(writer, sheet_name='sheet1')  # 시트명
    writer.save()


# In[12]:


plusUrl = []
plusUrl = input('검색어를 입력하세요 : ').split()
print(plusUrl)

for a in plusUrl:
    print(a)


# In[39]:



#  Mobile Version

# 네이버 검색 후 검색 결과 URL
baseUrl = 'https://m.search.naver.com/search.naver?where=m_view&sm=mtb_jum&query='
plusUrl = []  # 입력한 키워드 담아두는 list
plusUrl = input('검색어를 입력하세요 : ').split()  # 키워드를 띄어쓰기로 구분하여 배열에 저장한다


# 키워드 갯수로 for문 돌림
for a in plusUrl:
    # 현재 키워드
    print("--------------"+a+"--------------")  # 구분선
    url = baseUrl + urllib.parse.quote_plus(a)  # 키워드로 검색한 url
    print(url)  # url 출력
    html = urlopen(url)
    bsObject = bs(html, "html.parser")

    # 키워드로 검색한 리스트에서 view section list
    wrap = bsObject.select('._svp_item')

    for i in wrap:
        if len(i.select('.total_source > .ico_ad')) != 0:
            total_tit = i.select('.total_tit')
            company_name = i.select('span.name')
            for j in total_tit:
                print()
                for c in company_name:
                    print("업체명 : " + c.get_text())
                print("타이틀 : " + j.get_text())
                #print("링크 : " + j['href'])
                print()
