import pandas as pd
from src.classes.Product_csv import Product_csv


def save_import_file(product_csv: Product_csv, filename: str) -> None:

    df = pd.DataFrame({
        'Handle': product_csv.handle,
        'Title': product_csv.title,
        'Body (HTML)': product_csv.body,
        'Vendor': product_csv.vendor,
        'Status': product_csv.status,
        'Option1 Name': product_csv.option1_name,
        'Option1 Value': product_csv.option1_value,
        'Variant SKU': product_csv.variant_sku,
        'Variant Price': product_csv.variant_price,
        'Cost per item': product_csv.cost_per_item,
        'Image Src': product_csv.image_src,
        'Image Index': product_csv.image_index,
        'Variant Fulfillment Service': product_csv.variant_fulfillment_service
    })
    
    df.to_csv(filename, index=False)