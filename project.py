import string
from attr import attrs
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from geopy.geocoders import Nominatim

# browser = webdriver.Chrome(ChromeDriverManager().install())  
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"}

# loc = Nominatim(user_agent="GetLoc")
# city = "montreal"
# country = "canada"
# getLoc = loc.geocode(f"{city}, {country}")
# latitude = getLoc.latitude
# longitude = getLoc.longitude

def create_soup(url):
  res = requests.get(url, headers=headers)
  res.raise_for_status()
  soup = BeautifulSoup(res.text, "lxml")
  return soup

def scrape_weather():
  print("[Today's Weather]")
  url = "https://weather.naver.com/today/WDCAN01283"
  soup = create_soup(url)

  max_temp = soup.find('dt', attrs={"class":"term"}, string="최고").find_next_sibling('dd').get_text()
  min_temp = soup.find('dt', attrs={"class":"term"}, string="최저").find_next_sibling('dd').get_text()
  feels_like = soup.find('dt', attrs={"class":"term"}, string="체감").find_next_sibling('dd').get_text()
  rainfall_prob = soup.find('dt', attrs={"class":"ttl"}, string="강수확률").find_next_sibling('dd').get_text()

  weather_summary = "Max : {} | Min : {} | Feels like : {} | Ranifall Probability : {}".format(max_temp, min_temp, feels_like, rainfall_prob)
  return weather_summary

def scrape_news():
  print("[News]")
  url = "https://www.theverge.com/tech"
  soup = create_soup(url)
  
  news_list = soup.find('div', attrs={"class":"c-compact-river"}).find_all('h2', limit=3)

  for index, news in enumerate(news_list):
    title = news_list[index].a.get_text()
    link = news_list[index].a["href"]

    print("{}. {}".format(index+1, title))
    print("   " + link)
print()

def scrape_quotes():
  print("[Carpe Diem]")
  url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%98%A4%EB%8A%98+%EB%AA%85%EC%96%B8&oquery=%EB%85%B8%EB%A0%A5+%EB%AA%85%EC%96%B8&tqi=hB0ildp0YihssPBek3KssssssA8-009031"
  soup = create_soup(url)
  
  quoteList = soup.find_all('p', attrs={"class":"lngeng"}, limit=2)
  for index, quote in enumerate(quoteList):
    sentence = quoteList[index].get_text()
    print("{}. {}".format(index+1, sentence))
  print()


if __name__ == "__main__":
  scrape_weather()
  scrape_news()
  scrape_quotes()

