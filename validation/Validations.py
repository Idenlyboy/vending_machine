from modules.Product import Product


def product_data_validated(name, code):
    if 2 <= len(name) <= 64 and '1' + '0' * 10 <= str(code) <= '9' * 11:
        return True
    else:
        print('invalid product data')
        return False


def vending_product_validated(product: Product):
    if product.name != '' and product.condition == 'released' and product.code != -1:
        return True
    else:
        return False


def conditions_validated(condition):
    if type(condition) is str and 2 <= len(condition) <= 50:
        return True
    else:
        print('invalid condition data')
        return False


def list_products_validated(product):
    if product.get_condition() == 'work':
        return True
    else:
        print('invalid list of products data')
        return False
