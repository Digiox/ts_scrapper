from bs4 import BeautifulSoup
import requests


def get_page_content(session: requests.Session, product_url: str) -> BeautifulSoup:
    """Retrieve the webpage content using the session object and return the BeautifulSoup object."""
    response = session.get(product_url)

    if response.status_code != 200:
        raise Exception(f"Error while retrieving the webpage: {response.status_code}")

    return BeautifulSoup(response.content, 'html.parser')
