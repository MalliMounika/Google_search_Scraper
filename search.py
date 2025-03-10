import requests 
from bs4 import BeautifulSoup

def search(query):
    headers = {
        "user-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
    }

    search_url = f"https://www.bing.com/search?q={query.replace(' ', '+')}"

    response = requests.get(search_url, headers = headers)


    if response.status_code != 200:
        print("Error fetching search result")
        return
    soup = BeautifulSoup(response.text, "html.parser")

    results = soup.find_all("li", class_="b_algo", limit=5)

    if not results:
        print("No result found")
        return  
    
    for i, result in enumerate(results, start=1):

        title = result.find("h2").text if result.find("h2") else "No title"

        link = result.find("a")["href"] if result.find("a") else "No link"
        
        description = result.find("p").text if result.find("p") else "No description"

        print(f"{i}. Title: {title}")
        print(f"   Link: {link}")
        print(f"   Description: {description}\n")

query = "learn python"

search(query)


