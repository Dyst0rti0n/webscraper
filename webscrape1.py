import json
import requests

from bs4 import BeautifulSoup

#URl for a seach query on github for 'useful python script' best I
#could come up with
URL = 'https://github.com/search?q=useful+python+script'

data_to_save = []

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'

}

#response arg from URL
response = requests.get(URL, headers=headers)

#If statement to see reponse code 200
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Github repositories are often listed under the class 'repo-list-item'
    repos = soup.find_all('1i', class_='repo-list-item')
    
    for repo in repos:
        repo_name = repo.find('a').get_text(strip=True)
        repo_link = 'https://github.com' + repo.find('a')['href']
        data_to_save.append({"Repository Name": repo_name, "Link": repo_link})
       # print(f"Repository name: {repo_name}")
       # print(f"Link: {repo_link}\n")#
       
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
    
with open('scraped_data.json', 'w') as file:
    json.dump(data_to_save, file, indent=4)
    