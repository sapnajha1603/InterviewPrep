'''
Question: Web Scraping with Python

Task: Write a Python script to scrape the titles and URLs of the latest articles from a news website (e.g., BBC, CNN, or any other site of your choice) and save them to a CSV file.
Requirements:

    Use the requests library to fetch the webpage's HTML.
    Use the BeautifulSoup library to parse the HTML and extract data.
    Save the extracted titles and URLs into a CSV file.

Would you like to attempt this or need a step-by-step explanation? 😊'''


import requests
from bs4 import BeautifulSoup
import csv

def scrape_news_and_save_to_csv(url, output_file):
    try:
        # Fetch the webpage content
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find article titles and URLs
        articles = soup.find_all('h3')  # Adjust the tag based on the website
        data = []
        for article in articles:
            title = article.get_text(strip=True)
            link_tag = article.find('a')
            link = link_tag['href'] if link_tag else None

            # Add data to the list (ignore items without a valid link)
            if title and link:
                # Handle relative URLs
                if link.startswith('/'):
                    link = f"{url}{link}"
                data.append([title, link])

        # Save the data to a CSV file
        with open(output_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Title', 'URL'])  # Write header
            writer.writerows(data)  # Write rows

        print(f"Scraped {len(data)} articles and saved to {output_file}.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
news_url = "https://www.bbc.com/news"  # Replace with your target URL
output_csv = "news_articles.csv"
scrape_news_and_save_to_csv(news_url, output_csv)
