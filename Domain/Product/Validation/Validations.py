

def product_data_validated(name, code):
    """check if product attributes validated"""
    is_length_okay = 2 <= len(name) <= 64
    is_code_okay = 10**3 <= code <= 10**4-1
    if is_length_okay and is_code_okay:
        return True
    print('invalid product data')
    return False






