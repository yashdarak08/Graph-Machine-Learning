import requests
from bs4 import BeautifulSoup
import os
import json

def scrape_financial_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Dummy extraction logic: Find table rows with id "financial-data"
        data = []
        table = soup.find('table', {'id': 'financial-data'})
        if table:
            rows = table.find_all('tr')
            for row in rows:
                cols = row.find_all('td')
                if cols and len(cols) >= 3:
                    record = {
                        'company': cols[0].text.strip(),
                        'value': cols[1].text.strip(),
                        'date': cols[2].text.strip()
                    }
                    data.append(record)
        else:
            # Simulate dummy data if no table is found
            data = [
                {'company': 'Company A', 'value': '1000', 'date': '2023-01-01'},
                {'company': 'Company B', 'value': '2000', 'date': '2023-01-01'},
                {'company': 'Company C', 'value': '1500', 'date': '2023-01-02'}
            ]
        return data
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return []

def save_raw_data(data, filename='data/raw/financial_data.json'):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Data saved to {filename}")

def main():
    url = "http://example.com/financial_data" 
    data = scrape_financial_data(url)
    if data:
        save_raw_data(data)
    else:
        print("No data scraped.")

if __name__ == '__main__':
    main()
