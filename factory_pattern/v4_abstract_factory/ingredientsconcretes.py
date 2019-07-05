# ingredientsconcretes.py

from ingredientsabstracts import PizzaIngredientFactory
from ingredientsabstracts import (Dough, Sauce, Cheese, Veggies, Pepperoni,
        Clams)

class NYPizzaIngredientFactory(PizzaIngredientFactory):

    def create_dough():
        return ThinCrustDough()

    def create_sauce():
        return MarinaraSauce()

    def create_cheese():
        return ReggianoCheese()

    def create_veggies():
        veggies = [Garlic(), Onion(), Mushroom(), RedPepper()]
        return veggies

    def create_pepperoni():
        return SlicedPepperoni()

    def create_clams():
        return FreshClams()


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):

    def create_dough():
        return ThickCrustDough()

    def create_sause():
        return PlumTomatoSauce()

    def create_cheese():
        return MozzerallaCheese()

    def create_veggies():
        veggies = [Spinach(), BlackOlives(), EggPlant(), ]
        return veggies

    def create_pepperoni():
        return SlicedPepperoni()

    def create_clams():
        return FrozenClams()

class ThickCrustDough(Dough):
    pass
