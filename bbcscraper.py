import requests
from bs4 import BeautifulSoup

def get_top_headlines():
    # Make a request to the website
    r = requests.get('https://www.bbc.co.uk/news')

    # Create an object of BeautifulSoup and specify the parser
    soup = BeautifulSoup(r.text, 'html.parser')

    # Get the top headlines
    headlines = soup.select('.gs-c-promo-heading__title')

    # Print the top headlines
    for headline in headlines:
        print(headline.get_text())

if __name__ == "__main__":
    get_top_headlines()
