import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# 저는 streamlit을 모릅니다.

"""
st.write("Hello World")
from bs4 import BeautifulSoup 


"""
import requests





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
            print(x,link['href'])
            article_urls.append(link['href'])
            x=x+1

import os
from openai import OpenAI

client = OpenAI(
   api_key=os.environ.get('OPEN_API_KEY')
) 
def ask_chatgpt(messages):
    response = client.chat.completions.create(
    model="gpt-4-0125-preview", messages=messages
  )
    return response.choices[0].message.content

prompt_role = "너는 한국의 신문 기자이다. \
      FACT의 내용을 바탕으로 새로 기사를 써줘.    \
        한국인 독자가 이해하기 쉽도록, 너가 다시 읽어보고 잘 해설해서 써줘.    \
          이 사건에 대한 너의 견해와 분석도 넣어줘.    \
        이 기사의 출처가 NPR이라는 걸 꼭 밝혀줘.\
        이 기사의 출처가 NPR이라는 걸 정말 꼭 밝혀줘.\
           제발 이 기사의 출처가 NPR이라는 걸 결과물에 정말 꼭 밝혀줘.\
            TONE 과  LENGTH, STYLE 등의 instructions 를 지켜줘.\
            넌 잘 할 수 있어.  "
        
from typing import List
def assist_journalist(
  facts: List[str], tone: str, length_words: int, style: str
):
    facts = ", ".join(facts)
    #prompt_role = "너는 한국의 신문 기자다."
    prompt = f"{prompt_role} \
    FACTS: {facts} \
    TONE: {tone} \
    LENGTH: {length_words} words \
    STYLE: {style} "
    return ask_chatgpt([{"role": "user", "content": prompt}])





#article_url = 'https://www.npr.org/2024/02/06/1228720142/michael-mann-climate-scientist-in-court-suing-for-defamation'


# requests를 사용하여 웹 페이지의 HTML을 가져옵니다.
article=article_urls[9]
response = requests.get(article)

html = response.content

# BeautifulSoup 객체를 생성하여 HTML을 파싱합니다.
soup = BeautifulSoup(html, 'html.parser')

# 기사 본문을 추출합니다. 실제 클래스 이름은 페이지에 따라 다를 수 있습니다.
#article_body = soup.find('p')
#paragraphs = article_body.find_all('p')
paragraphs = soup.find_all('p')

# 기사 본문을 텍스트로 합칩니다.

article_content = '\n'.join(paragraph.text for paragraph in paragraphs)
article_content ="아래 기사는 미국 언론 NPR이 보도한 것이다.\n"+article_content 
#print(article_content)
print(
  assist_journalist(
 [article_content], "formal", 400, "신문 기사"
  )
)
"""
