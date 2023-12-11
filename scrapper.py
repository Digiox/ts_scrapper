from typing import Optional
from src.run_with_page import run_with_page
from src.classes.Product_csv import Product_csv
from src.save_import_file import save_import_file
from src.extract_product_data import extract_product_data
from src.generate_product_import_csv import generate_product_import_csv
from src.get_page_content import get_page_content
from src.login import login

from src.purge_import_files import purge_import_files


# Constants
URL_LOGIN = "https://www.tendance-sensuelle.com/fr/connexion"
PRODUCT_URL = "https://www.tendance-sensuelle.com/fr/body/7434-le-numero-1-body-clara-morgane-noir.html"
product_import_file_name = 'product_import.csv'
CREDENTIALS = {
    'email': 'heaventouchshop@gmail.com',
    'passwd': 'Titoul84400!',
    'back': 'index',
    'SubmitLogin': ''
}










def main():
    mode = input("Enter the mode (url_list or page): ")

    
    product_csv: Product_csv = Product_csv()
    

    
    purge_import_files(product_import_file_name)
    
    try:
        session = login(URL_LOGIN, CREDENTIALS)

        if mode == "url_list":
            with open('src/entry_datas/urls.txt', 'r') as file:
                urls = file.readlines()
            
            for url in urls:
                url = url.strip()
                soup = get_page_content(session, url)
                try:
                    product_data = extract_product_data(soup)
                except Exception as e:
                    print(f"Can't extract product data on product {url}: {e}")
                    continue
                product_csv: Product_csv = generate_product_import_csv(product_data, product_import_file_name, product_csv)
        elif mode == "page":
            with open('src/entry_datas/page.txt', 'r') as file:
                url = file.readline().strip()
            run_with_page(url, product_import_file_name, session, product_csv)
        
            
                
        # save Product_csv object to csv file
        if product_csv is not None:
            
            save_import_file(product_csv, product_import_file_name)
            print(f"File {product_import_file_name} saved successfully.")
        else:
            print("No data to save.")
        
        
        
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
