# pizza.py

class PizzaStore:
    def __init__(self):
        self.factory = SimplePizzaFactory()

    def order_pizza(self, type: str):

        self.factory.create_pizza(type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza


class SimplePizzaFactory:

    def create_pizza(type: str):

        pizza = None

        if type == 'cheese':
            pizza = CheesePizza()
        elif type == 'greek':
            pizza = GreekPizza()
        elif type == 'pepperoni':
            pizza == PepperoniPizza()

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

