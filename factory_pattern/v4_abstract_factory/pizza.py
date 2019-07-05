# pizza.py

import abc


class Pizza(abc.ABC):

    def __init__(self):
        self.name = None

        self.dough = None
        self.sauce = None
        self.veggies = []
        self.clams = None
        self.pepperoni = None
        self.cheese = None

    @abc.abstractmethod
    def prepare(self):
        pass

    def bake(self):
        print('bake for 25 mins at 350')

    def cut(self):
        print('cutting the pizza into 8 slices')

    def box(self):
        print('put pizza in official box')

    def set_name(name: str):
        self.name = name

    def get_name() -> str:
        return name


class CheesePizza(Pizza):
    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        self.ingredient_factory = ingredient_factory

    def prepare():
        print(f'Preparing {self.name}')
        dough = self.ingredient_factory.create_dough()
        sauce = self.ingredient_factory.create_sauce()
        cheese = self.ingredient_factory.create_cheese()


class ClamPizza(Pizza):
    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        self.ingredient_factory = ingredient_factory

    def prepare():
        print(f'Preparing {self.name}')
        dough = self.ingredient_factory.create_dough()
        sauce = self.ingredient_factory.create_sauce()
        cheese = self.ingredient_factory.create_cheese()
        clam = self.ingredient_factory.create_clams()
