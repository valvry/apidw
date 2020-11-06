from django.http import HttpResponse
from  django.shortcuts import render
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions

#method view
def index(request):
    return render(request,'index.html')


def lastEpisode(request):
    options = FirefoxOptions()
    options.add_argument("--headless")
    browser = webdriver.Firefox(options=options)
    browser.get('https://www.animeindo.cc/anime-terbaru')
    html = browser.page_source
    # print(html)

    page = BeautifulSoup(html, 'html.parser')

    listAnime = page.find_all('div', class_='post-show')

    return HttpResponse(listAnime)