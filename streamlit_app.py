

import altair as alt
import pandas as pd
import streamlit as st
from bs4 import BeautifulSoup as bs
import requests

"""
# 저는 streamlit을 모릅니다.

"""
st.write("Hello World")




# step3. 입력받은 query가 포함된 url 주소(네이버 뉴스 검색 결과 페이지) 저장

url = 'https://www.npr.org'


# step4. requests 패키지를 이용해 'url'의 html 문서 가져오기

response = requests.get(url)

html_text = response.text


# step5. beautifulsoup 패키지로 파싱 후, 'soup' 변수에 저장

soup = bs(response.text, 'html.parser')

# 모든 'a' 태그 찾기
links = soup.find_all('a')

# 각 링크의 href 속성 출력
article_urls = []
x=0
for link in links:
    if link.has_attr('href'):
        if 'npr.org/2024' in link['href']:
            st.write("Hello World")
            print(x,link['href'])
            article_urls.append(link['href'])
            x=x+1


