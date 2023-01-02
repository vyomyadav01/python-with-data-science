from bs4 import BeautifulSoup
import requests
url = 'http://www.google.com/search?q=css'
response = requests.get(url)
if not response.status_code == 200:
    print('An error occurred')
    exit()
else:
    print('Successfully')
    soup = BeautifulSoup(response.text,'html5lib')
    print(soup.prettify())
    #get all headings
    headings_2 = soup.find_all('h2')
    print(headings_2)
    for i in headings_2:
        print(i.text)
        
    # get all links
    links = soup.find_all('a')
    print("links")
    for i in links:
        print(f'{i.text} -> {i.get("href")}')        
    