import requests
from bs4 import BeautifulSoup
import pandas as pd

class NasEarthDataScraper:
    def __init__(self):
        self.base_url = "https://www.earthdata.nasa.gov/engage/open-data-services-and-software/api"

    def scrape_data(self):
        response = requests.get(self.base_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            data_links = soup.find_all('a', class_='view-full-dataset')

            data_list = []
            for link in data_links:
                data_name = link.text.strip()
                data_url = link['href']
                data_list.append({'Data Name': data_name, 'Data URL': data_url})

            df = pd.DataFrame(data_list)
            df.to_csv('nasa_earth_data.csv', index=False)
            print("Data has been scraped and saved to 'nasa_earth_data.csv'")
        else:
            print("Failed to retrieve data.")

if __name__ == "__main__":
    scraper = NasEarthDataScraper()
    scraper.scrape_data()
