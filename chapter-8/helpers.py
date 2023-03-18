def get_tax(price, tax_rate):
    return price * tax_rate


def get_net_price(price, tax_rate):
    return price + get_tax(price, tax_rate)
