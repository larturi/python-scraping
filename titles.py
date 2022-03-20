from bs4 import BeautifulSoup;
import requests;

def get_titles(page_id):
    url = f'https://subslikescript.com/movies?page={page_id}'
    result = requests.get(url)
    content = result.text
    soup = BeautifulSoup(content, 'lxml')
    box = soup.find('article', class_='main-article')
    
    links = []
    
    for link in box.find_all('a', href=True):
        links.append('https://subslikescript.com/' + link['href'])  
        
    return links
