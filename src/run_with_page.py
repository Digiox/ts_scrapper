import http
import time
from bs4 import BeautifulSoup
import requests
from src.classes.Product_csv import Product_csv
from src.extract_product_data import extract_product_data
from src.generate_product_import_csv import generate_product_import_csv
from src.get_page_content import get_page_content


def run_with_page(url: str, product_import_file_name: str, session: requests.Session, product_csv: Product_csv) -> Product_csv:
    """Run the script using the product URL."""
    # Téléchargement du contenu de la page
    http.client._MAXHEADERS = 1000
    response = requests.get(url)
    html_content = response.text

    # Analyse du contenu HTML avec BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extraction des URL des articles et stockage dans une liste
    article_links = [a['href'] for a in soup.find_all('a', class_='product-name')]

    print(f"{len(article_links)} product URLs found.")
    time.sleep(5)

    for article_link in article_links:
        
        soup = get_page_content(session, article_link)
        product_data = extract_product_data(soup)
        product_csv: Product_csv = generate_product_import_csv(product_data, product_import_file_name, product_csv)
    
    return product_csv