import json
import requests
from bs4 import BeautifulSoup

def scrape_github(URL):
    data_to_save = []
    response = requests.get(URL)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Assuming for now that 'repo-list-item' is the correct class
        repos = soup.find_all('li', class_='repo-list-item')
        
        for repo in repos:
            repo_name = repo.find('a').get_text(strip=True)
            repo_link = 'https://github.com' + repo.find('a')['href']
            data_to_save.append({"Repository Name": repo_name, "Link": repo_link})
            print(f"Completed...")
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
    
    return data_to_save

def save_to_json(data):
    with open('scraped_data.json', 'w') as file:
        json.dump(data, file, indent=4)

def main():
    URL = 'https://github.com'
 
    scraped_data = scrape_github(URL)
    save_to_json(scraped_data)

if __name__ == "__main__":
    main()
