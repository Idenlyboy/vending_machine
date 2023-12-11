from modules.Statuses import ProductStatuses, VendingStatuses


def product_data_validated(name, code):
    """check if product attributes validated"""
    is_length_okay = 2 <= len(name) <= 64
    is_code_okay = 10**4 <= code <= 10**5-1
    if is_length_okay and is_code_okay:
        return True
    print('invalid product data')
    return False


def vending_status_validated(status: str):
    """check if vending machine status in STATUSES const dictionary"""
    if status in VendingStatuses.STATUSES.values():
        return True
    print('invalid product state')
    return False


def product_status_validated(product):
    """check if product status is 'released'"""
    is_product_released = product.get_status() == ProductStatuses.STATUSES['released']
    if is_product_released:
        return True
    print('invalid product status')
    return False
