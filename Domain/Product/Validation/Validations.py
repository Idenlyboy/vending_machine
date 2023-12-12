

def product_data_validated(name, code):
    """check if product attributes validated"""
    is_length_valid = 2 <= len(name) <= 64
    is_code_valid = 10**3 <= code <= 10**4-1
    if is_length_valid and is_code_valid:
        return True
    print('invalid product data')
    return False






