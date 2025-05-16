import json
from requests_html import HTMLSession
from urllib.parse import urljoin

session = HTMLSession()
url = 'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFZxYUdjU0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen'

r = session.get(url)
r.html.render(sleep=1, scrolldown=5)

articles = r.html.find('article')
base_url = 'https://news.google.com'

news_data = []

for article in articles:
    link_tag = article.find('a.gPFEn', first=True)
    if link_tag:
        title = link_tag.text
        relative_link = link_tag.attrs.get('href')
        full_link = urljoin(base_url, relative_link)
        news_data.append({
            "title": title,
            "url": full_link
        })

# Save to JSON file
with open("news_headlines.json", "w") as f:
    json.dump(news_data, f, indent=2)

print("Exported headlines to news_headlines.json successfully")

#There are a few dependencies that must be installed for this script to run properly 
#lxml_html_clean
#requests_html
