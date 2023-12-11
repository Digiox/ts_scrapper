from typing import Dict
from bs4 import BeautifulSoup
import requests


def login(url_login: str, credentials: Dict[str, str]) -> requests.Session:
    """Login to the website and return the session object."""
    session = requests.Session()
    response = session.post(url_login, data=credentials)
    soup = BeautifulSoup(response.content, 'html.parser')

    if not soup.find("a", class_="account"):
        raise Exception("Login failed")

    print("Login successful")
    return session