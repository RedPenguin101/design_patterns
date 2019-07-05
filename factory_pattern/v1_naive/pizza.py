# pizza.py

def order_pizza(type: str):
    if type == 'cheese':
        pizza = CheesePizza()
    elif type == 'greek':
        pizza = GreekPizza()
    elif type == 'pepperoni':
        pizza == PepperoniPizza()

    '''
    the above code is what could change if we have more pizza types, or remove
    them. We would have to modify it, violating open-closed.
    '''

    pizza.prepare()
    pizza.bake()
    pizza.cut()
    pizza.box()

    return pizza


class Pizza:
    def __init__(self):
        self.is_prepared = False
        self.is_baked = False
        self.is_cut = False
        self.is_boxed = False

    def prepare(self):
        self.is_prepared = True

    def bake(self):
        self.is_baked = True

    def cut(self):
        self.is_cut = True

    def box(self):
        self.is_boxed = True


class CheesePizza(Pizza):
    pass

class GreekPizza(Pizza):
    pass

class PepperoniPizza(Pizza):
    pass

