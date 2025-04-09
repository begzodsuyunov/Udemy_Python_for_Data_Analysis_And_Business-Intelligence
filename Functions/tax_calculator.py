
def tax_calculator(amount, tax = 0.06):
    tax_total = round(amount * tax, 2)
    total = round(amount  + tax_total, 2)
    return [amount, tax_total, total]
