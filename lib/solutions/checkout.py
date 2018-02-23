
def sku_lookup(sku):
    price_table = [
        {
            'item': 'A',
            'price': 50,
            'offers': [
                '3A for 130',
            ],
        },
        {
            'item': 'B',
            'price': 30,
            'offers': [
                '2B for 45',
            ],
        },
        {
            'item': 'C',
            'price': 20,
            'offers': [],
        },
        {
            'item': 'D',
            'price': 15,
            'offers': [],
        },
    ]
    for item in price_table:
        if sku == item.get('item'):
            return item
    return None

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    sku_list = list(skus)
    total = 0
    for sku in sku_list:
        sku_item = sku_lookup(sku)
        if not sku_item:
            return -1
        price = sku_item.get('price', -1)
        if price < 0:
            return -1
        total += price
