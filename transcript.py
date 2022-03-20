from bs4 import BeautifulSoup;
import requests;

def get_transcript(url):
    result = requests.get(url)
    content = result.text
    soup = BeautifulSoup(content, 'lxml')
    box = soup.find('article', class_='main-article')
    title = box.find('h1').get_text()
    transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')
    
    clean_title = title.split(' - ')[0]
    
    with open(f'transcripts/{clean_title.capitalize()}.txt', 'w') as file:
        file.write(title + '\n')
        file.write(transcript)
        
        

