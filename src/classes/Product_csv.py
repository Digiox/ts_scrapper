class Product_csv:
    def __init__(self, handle: list[str] = [], title: list[str] = [], body: list[str] = [], vendor: list[str] = [], status: list[str] = [], option1_name: list[str] = [], option1_value: list[str] = [], variant_sku: list[str] = [], variant_price: list[float] = [], cost_per_item: list[float] = [], image_src: list[str] = []):
        self.handle = handle
        self.title = title
        self.body = body
        self.vendor = vendor
        self.status = status
        self.option1_name = option1_name
        self.option1_value = option1_value
        self.variant_sku = variant_sku
        self.variant_price = variant_price
        self.cost_per_item = cost_per_item
        self.image_src = image_src
        self.image_index = []
        self.variant_fulfillment_service = []
