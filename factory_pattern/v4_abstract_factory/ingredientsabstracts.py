# ingredientsabstracts.py

import abc


class PizzaIngredientFactory(abc.ABC):

    @abc.abstractmethod
    def create_dough() -> Dough:
        pass

    @abc.abstractmethod
    def create_sauce() -> Sauce:
        pass

    @abc.abstractmethod
    def create_cheese() -> Cheese:
        pass

    @abc.abstractmethod
    def create_veggies() -> Veggies:
        pass

    @abc.abstractmethod
    def create_pepperoni() -> Pepperoni:
        pass

    @abc.abstractmethod
    def create_clams() -> Clams:
        pass
