
import pprint
from typing import Optional
import pandas as pd

from src.classes.Product import Product
from src.classes.Product_csv import Product_csv
from src.classes.Variant import Variant


def generate_product_import_csv(data: Product, filename: str, product_csv: Product_csv) -> Product_csv:
    """Create a CSV file from extracted data."""
    try:
        handle = data.title.lower().replace(" ", "-")
        csv_data = product_csv

        # Add main product row
        csv_data.handle.append(handle)
        csv_data.title.append(data.title)
        csv_data.body.append(data.description)
        csv_data.vendor.append(data.manufacturer)
        csv_data.status.append("draft")
        csv_data.option1_name.append("" if len(data.prices_and_variants) > 1 else "Title")
        csv_data.option1_value.append("" if len(data.prices_and_variants) > 1 else "Default Title")
        csv_data.variant_sku.append("" if len(data.prices_and_variants) > 1 else data.prices_and_variants[0]["sku"])
        csv_data.variant_price.append("" if len(data.prices_and_variants) > 1 else data.prices_and_variants[0]["variant_price"])
        csv_data.cost_per_item.append("" if len(data.prices_and_variants) > 1 else data.prices_and_variants[0]["cost_per_item"])
        csv_data.image_src.append(data.image_urls[0])
        csv_data.image_index.append("")
        csv_data.variant_fulfillment_service.append("manual")

        # Add variant rows
        if len(data.prices_and_variants) > 1:
            for index, variant in enumerate(data.prices_and_variants):
                variant_element: Variant = Variant(**variant)
                csv_data.handle.append(handle)
                csv_data.title.append("")
                csv_data.body.append("")
                csv_data.status.append("")
                csv_data.vendor.append("")
                csv_data.option1_name.append("Taille" if index == 0 else "")
                csv_data.option1_value.append(variant_element.variant)
                csv_data.variant_sku.append(variant_element.sku)
                csv_data.variant_price.append(variant_element.variant_price)
                csv_data.cost_per_item.append(variant_element.cost_per_item)
                csv_data.image_src.append("")
                csv_data.image_index.append("")
                csv_data.variant_fulfillment_service.append("")

        # Add image rows
        for index, image_url in enumerate(data.image_urls):
            if index == 0:
                continue
            csv_data.handle.append(handle)
            csv_data.title.append("")
            csv_data.body.append("")
            csv_data.vendor.append("")
            csv_data.status.append("")
            csv_data.option1_name.append("")
            csv_data.option1_value.append("")
            csv_data.variant_sku.append("")
            csv_data.variant_price.append("")
            csv_data.cost_per_item.append("")
            csv_data.image_src.append(image_url)
            csv_data.image_index.append(index + 1)
            csv_data.variant_fulfillment_service.append("")

        # Print length of each row in Product_csv
        for name, row in csv_data.__dict__.items():
            print(f"Length of {name}: {len(row)}")

    except Exception as e:
        print(f"Can't generate product import CSV: {e}")
        return None

    return product_csv
    

    