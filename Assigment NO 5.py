import requests
from bs4 import BeautifulSoup
import pandas as pd

url="https://islamqa.info/en/answers/145520/difference-between-hadith-and-sunnah"

Page=requests.get(url)
#print (Page)

soup=BeautifulSoup (Page.content,'html.parser')
#print(soup)

title=soup.find(class_="title is-4 is-size-5-touch").text.replace("\n","")
#print(title)

questionNo=soup.find(class_="level-item has-separator").text.replace("\n","")
#print(questionNo)

Question=soup.find(class_="single_fatwa__question text-justified").text.replace("\n","")
#print(Question)

Answer=soup.find(class_="single_fatwa__answer__body text-justified _pa--0").text.replace("\n","")
#print(Answer)

data=[[url,title,questionNo,Question,Answer]]
#print(data)

df=pd.DataFrame(data,columns=['Url','Title','QuestionNo','Question','Answer'])
#df
df.to_csv("coding.csv")
