import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = 'http://quotes.toscrape.com/'  # Changed URL

response = requests.get(base_url)
soup = BeautifulSoup(response.text, 'html.parser')

quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')
tags = soup.find_all('div', class_='tags')

# List to store the data
data = []

for quote, author, tag in zip(quotes, authors, tags):
    quote_text = quote.text.strip()
    author_name = author.text.strip()
    tag_list = [t.text for t in tag.find_all('a', class_='tag')]

    # Add the data to the list
    data.append({
        'Quote': quote_text,
        'Author': author_name,
        'Tags': ', '.join(tag_list)
    })

# Convert the list of data into a pandas DataFrame
df = pd.DataFrame(data)

# Save the DataFrame as a CSV file
df.to_csv('quotes.csv', index=False)

print("Data has been saved to 'quotes.csv'")