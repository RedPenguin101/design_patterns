# pizzastore.py

import abc

class PizzaStore(abc.ABC):

    def order_pizza(self, type: str):

        pizza = self.create_pizza(type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza

    @abc.abstractmethod
    def create_pizza(self, type: str):
        pass


class NYStylePizzaStore(PizzaStore):

    def create_pizza(self, type: str):

        pizza = None
        ingredient_factory = NYPizzaIngredientFactory()

        if type == 'cheese':
            pizza = CheesePizza(ingredient_factory)
            pizza.set_name('New York Style Cheese Pizza')
        elif type == 'clam':
            pizza = ClamPizza(ingredient_factory)
            pizza.set_name('New York Style Clam Pizza')

        return pizza


class ChicagoStylePizzaStore(PizzaStore):

    def create_pizza(self, type: str):

        pizza = None
        ingredient_factory = ChicagoPizzaIngredientFactory()

        if type == 'cheese':
            pizza = CheesePizza(ingredient_factory)
            pizza.set_name('Chicago Style Cheese Pizza')
        elif type == 'clam':
            pizza = ClamPizza(ingredient_factory)
            pizza.set_name('Chicago Style Clam Pizza')

        return pizza
