import requests
from bs4 import BeautifulSoup

query=input("What news u need?: ")

# Step 1: Fetch the page
url = "https://timesofindia.indiatimes.com/"
r = requests.get(url)

# Step 2: Parse the content
soup = BeautifulSoup(r.text, 'html.parser')

# Step 3: Find all headline elements
# Headlines are often in <h2>, <h3>, or inside <a> tags with specific classes
for heading in soup.find_all(["figcaption", "h2",]):
    text = heading.get_text(strip=True)
    if text:
        print(text)
for headline in soup.find_all('a', class_='ga-headlines'):
    print(headline.get_text(strip=True))



