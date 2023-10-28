import json
import requests
from bs4 import BeautifulSoup

def scrape_github(url):
    print("Test 1")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    data_to_save = []
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        print("Repos1")
        repos1 = soup
        articles = soup.find_all('p', {'class': 'col-9 color-fg-muted my-1 pr-4'})
        print(articles)

        print("articles")
        for article in articles:
            try:
                repo_name_element = article.find('a')  
                repo_description_element = article.find('p', {'class': 'col-9 color-fg-muted my-1 pr-4'})

                print("Repo_data")
                repo_data = {
                    "name": repo_name_element.get_text(strip=True),
                    "description": repo_description_element.get_text(strip=True) if repo_description_element else "No description available."
                }
                data_to_save.append(repo_data)

                # 3. Printing Data
                print(f"Repository: {repo_data['name']}\nDescription: {repo_data['description']}\n{'-'*40}")

            except Exception as e:
                print(f"Error processing a repository: {e}")
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
