from Domain.VendingMachine.Statuses.Statuses import VendingStatuses
from Domain.Product.Statuses.Statuses import ProductStatuses


def vending_status_validated(status: str):
    """check if vending machine status in STATUSES const dictionary"""
    if status in VendingStatuses.STATUSES.values():
        return True
    print('invalid product status')
    return False


def product_status_validated(product):
    """check if product status is 'released'"""
    is_product_released = product.get_status() == ProductStatuses.STATUSES['released']
    if is_product_released:
        return True
    print('invalid product status')
    return False
