import requests
from bs4 import BeautifulSoup

links = ['https://www.imdb.com/title/tt0325980/?ref_=nm_knf_i2', 'https://www.imdb.com/title/tt0367594/?ref_=rvi_tt',
         'https://www.imdb.com/title/tt6450804/?ref_=rvi_tt']


def slice(title):
    start = title.find('>') + 1
    end = title[1:].find('<') + 1
    return title[start:end]


for i in links:
    r = requests.get(i)
    soup = BeautifulSoup(r.text, 'html.parser')
    title = soup.find('h1')
    print("Hello", title)
    title = str(title)
    title = slice(title)
    about = soup.find_all('div', {'class': 'credit_summary_item'})
    print("ABOUT", about)
    director, writers, stars = [i.find_all('a') for i in about]
    print("+-+-", director)
    writers = [slice(str(i)) for i in writers]
    stars = [slice(str(i)) for i in stars]
    del stars[-1]
    director = str(director)
    director = slice(director[1:])
    print(title)
    print(*director)
    print(*writers)
    print(*stars)
