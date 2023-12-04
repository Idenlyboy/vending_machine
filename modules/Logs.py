from datetime import datetime


class Logs:

    def __init__(self):
        logs = []

    def removed_by_code(self, product):
        self.logs.append(f'removed product {product.name} with code {product.code} at {datetime}\n')
        return

    def added_product(self, product):
        self.logs.append(f'added product {product.name} with code {product.code} at {datetime}\n')
        return

    def bought_product(self, product_code):
        self.logs.append(f'bought product with code {product_code} at {datetime}\n')
        return

    def changed_condition(self, old_condition, new_condition):
        self.logs.append(f'changed condition from {old_condition} to {new_condition} at {datetime}\n')
        return

    def show_logs(self, *args):
        """shows logs with/without parameters ('-a' = all, '-l5' = last 5 notes,
        '-l20', '-l50', '-l100')"""
        for arg in [*args]:
            match arg:
                case '':
                    print(*self.logs)
                case '-a':
                    print(*self.logs)
                case '-l5':
                    print(*self.logs[-1 * min(5, len(self.logs)):])
                case '-l20':
                    print(*self.logs[-1 * min(20, len(self.logs)):])
                case '-l50':
                    print(*self.logs[-1 * min(50, len(self.logs)):])
                case '-l100':
                    print(*self.logs[-1 * min(100, len(self.logs)):])
        return

