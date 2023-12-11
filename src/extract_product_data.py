from typing import Dict, Union
from bs4 import BeautifulSoup
from typing import Dict, List

from src.classes.Product import Product



def extract_product_data(soup: BeautifulSoup) -> Product:
    """Extract product data from BeautifulSoup object and return it as a dictionary."""
    try:
        title: str = soup.find("h1", itemprop="name").get_text()
        description: str = soup.find("div", ["std"]).get_text()

        prices_and_variants: List[Dict[str, str]] = []
        form_quantities = soup.find_all("div", ["quantities-block"])
        manufacturer: str = soup.find("a", class_="manufacturer").text
        for block in form_quantities:
            variant: str = block.find("span").text
            price: str = block.find("div", ["quantities-product-select-quantity"]).find("span").text.replace(" ", "").replace("€", "").replace(",", ".")
            price_with_taxes: float = round(float(price) * 1.5, 2)
            print(f'price * 1.5 = {price} * 1.5 = {price_with_taxes}')
            price_with_margin: float = round(float(price_with_taxes) * 1.5, 2)
            print(f'price_with_taxes * 1.5 = {price_with_taxes} * 1.5 = {price_with_margin}')
            sku: str = block.find("div", ["quantities-product-reference"]).text
            quantity: str = "0"  # Default value
            if block.find("li", ["product-quantity-ok"]):
                quantity = block.find("li", ["product-quantity-ok"]).text
            elif block.find("li", ["product-quantity-warning"]):
                quantity = block.find("li", ["product-quantity-warning"]).text
            


            prices_and_variants.append({
                "variant": variant,
                "variant_price": price_with_margin,
                "cost_per_item": price_with_taxes,
                "sku": sku,
                "quantity": quantity
            })

        image_urls: List[str] = []
        thumbnails = soup.find_all("li", {"id": lambda L: L and L.startswith('thumbnail_')})
        for thumbnail in thumbnails:
            img_url: str = thumbnail.find("a")["href"]
            image_urls.append(img_url)
    except Exception as e:
        print(f"Can't extract product data on product: {e}")
        return None
    
    return Product(title=title, description=description, prices_and_variants=prices_and_variants, image_urls=image_urls, manufacturer=manufacturer)
       
    