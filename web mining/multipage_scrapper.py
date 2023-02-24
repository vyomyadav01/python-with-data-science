from bs4 import BeautifulSoup
import requests
import pandas as pd


# get the data from website as soup a soup object
def get_soup(url) -> BeautifulSoup:
    try:
        page = requests.get(url)
        if page.status_code == 200:
            return BeautifulSoup(page.content, 'html5lib')
        else:
            print('Error getting', page.status_code)
    except Exception as e:
        print('Error:',e)
def collect_items(soup) -> list:
    try:
        items = soup.find_all('div',class_="_1xHGtK _373qXS")
        if len(items) > 0:
            return items
    except Exception as e:
        print('Error:',e)

# extract the data and return a dictionary
def extract_data(item) -> dict:
    brand  = item.find('div',class_='_2WkVRV').text
    product = item.find('div',class_='IRpwTa _2-ICcC')
          
    
# main function to run the program
def main():
    s = 'bags'
    url = f"https://www.flipkart.com/search?q={s}"
    print("URL =>",url)
    soup = get_soup(url)
    items = collect_items(soup)
    if isinstance(items, list):
        print(f'Total items found: {len(items)}')
        
main()


