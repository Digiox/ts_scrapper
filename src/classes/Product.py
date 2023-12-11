from typing import Dict, List, Union

from src.classes.Variant import Variant

class Product:
    def __init__(self, title: str, description: str, prices_and_variants: List[Variant], image_urls: List[str], manufacturer: str):
        self.title: str = title
        self.description: str = description
        self.prices_and_variants: List[Variant] = prices_and_variants
        self.image_urls: List[str] = image_urls
        self.manufacturer: str = manufacturer