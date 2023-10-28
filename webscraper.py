import json
import requests
from bs4 import BeautifulSoup

def scrape_github(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    data_to_save = []
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        repos1 = soup
        articles = soup.find_all('p', {'class': 'col-9 color-fg-muted my-1 pr-4'})
        print(articles)
       
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
    
    return data_to_save

def save_to_json(data):
    with open('scraped_data.json', 'w') as file:
        json.dump(data, file, indent=4)

def main():
    url = 'https://github.com/trending'
 
    scraped_data = scrape_github(url)
    save_to_json(scraped_data)

if __name__ == "__main__":
    main()
