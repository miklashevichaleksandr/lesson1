def get_vat(price, vat_rate):
    price = int(price)
    vat_rate = int(vat_rate)
    if price > 0:
        vat = price / 100 * vat_rate
        price_no_vat = price - vat
        print(price_no_vat)

price1 = input('Please enter price: ')
vat_rate1 = input('Please enter VAT: ')

get_vat(price1, vat_rate1)