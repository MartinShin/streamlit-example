

import altair as alt
import pandas as pd
import streamlit as st
from bs4 import BeautifulSoup as bs
import requests

"""
# NPR 기사 목록입니다.

"""





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
            st.write(x,link['href'])
            article_urls.append(link['href'])
            x=x+1


# requests를 사용하여 웹 페이지의 HTML을 가져옵니다.
article=article_urls[1]
response = requests.get(article)

html = response.content

# BeautifulSoup 객체를 생성하여 HTML을 파싱합니다.
soup = bs(html, 'html.parser')

# 기사 본문을 추출합니다. 실제 클래스 이름은 페이지에 따라 다를 수 있습니다.
#article_body = soup.find('p')
#paragraphs = article_body.find_all('p')
paragraphs = soup.find_all('p')

# 기사 본문을 텍스트로 합칩니다.

article_content = '\n'.join(paragraph.text for paragraph in paragraphs)
article_content ="아래 기사는 미국 언론 NPR이 보도한 것이다.\n"+article_content 
#print(article_content)
st.write(article_content)
