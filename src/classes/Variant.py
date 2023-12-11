class Variant:
    def __init__(self, variant: str, variant_price: float, cost_per_item: float, sku: str, quantity: str):
        self.variant = variant
        self.variant_price = variant_price
        self.cost_per_item = cost_per_item
        self.sku = sku
        self.quantity = quantity
