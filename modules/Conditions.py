from validation.Validations import conditions_validated


class Conditions:

    def __init__(self):
        self.conditions = []
        return

    def insert(self, condition):
        if conditions_validated(condition):
            self.conditions.append(condition)
        return

    def get_conditions(self):
        return self.conditions

    def get_condition_by_index(self, index):
        return self.conditions[index]


class ProductConditions(Conditions):

    def __init__(self):
        self.conditions = ['released', 'paused', 'rejected']
        return



class VendingConditions(Conditions):

    def __init__(self):
        self.conditions = ['work', 'paused', 'service', 'error']
        return

