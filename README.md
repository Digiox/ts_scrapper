# Tendance sensuelle scrapper

## Prerequisites

- Python 3.11.0 or higher

## Install

``git clone origin git@github.com:Digiox/ts_scrapper.git``

``cd ts_scrapper``

### Create venv environnement

``python -m venv venv``

### Activating environnement 

``.\venv\Scripts\activate`` (Windows)

``source venv/bin/activate`` (macOS or Linux)

### Fetch dependencies

``python libs.py``

Then Select "fetch" option


## Run the tool

You have to way to use this tool:

- With a set of product urls
- with a page of products


### Run with a set of product urls

``python scrapper.py``

Choose "url_list" option

### Run with a page of products

``python scrapper.py``

Choose "page" option


# Ready !


You can now use the product_import.csv file in your shopify store, if there is a lot of products, it might take a while.

# More informations

For the moment the tool only handle a tiny amout of features, it will be updated in the future.

If you are de developper, feel free to contribute to this project.

### Datas filled by the tool

- Handle (unique anchor)
- Title
- Body (HTML) (Product description)
- Vendor
- Status (always draft, you have to manually activate your product on Shopify)
- Variants
- Variant SKU
- Variant price (Selling price calculated for selling from france)
- Cost per item (Price on Tendance sensuelle)
- Image src
- Image index (Image position in the images list)
- Variant Fulfillment Service (Always manual)

## Download executable

[Download here](https://github.com/Digiox/ts_scrapper/suites/18921825956/artifacts/1105183460).