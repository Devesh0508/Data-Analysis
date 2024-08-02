# Webscraping from wikipedia

pip install requests beautifulsoup4
import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_and_convert_to_dataframe(url):
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the table in the HTML
        table = soup.find('table')

        # Extract table data into a list of lists
        data = []
        for row in table.find_all('tr'):
            row_data = [cell.text.strip() for cell in row.find_all(['td', 'th'])]
            data.append(row_data)

        # Convert the list of lists to a DataFrame
        df = pd.DataFrame(data[1:], columns=data[0])

        # Save DataFrame to CSV file
        df.to_csv('World_Population_Data.csv', index=False)

        return df
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return None


url_to_scrape = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population'
result_dataframe = scrape_and_convert_to_dataframe(url_to_scrape) #function call


if result_dataframe is not None:
    print(result_dataframe)
