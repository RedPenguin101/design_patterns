import abc

class Beverage(abc.ABC):
    def cost(self):
        pass

    def get_description(self):
        return "unknown beverage"


class HouseBlend(Beverage):
    def cost(self):
        return 0.89


class DarkRoast(Beverage):
    def cost(self):
        return 0.99


class Espresso(Beverage):
    def cost(self):
        return 1.99


class Decaf(Beverage):
    def cost(self):
        return 1.05


class CondimentDecorator(Beverage, abc.ABC):
    def __init__(self, bev: Beverage):
        self.beverage = bev

    def get_description(self):
        return self.beverage.get_description() + ", unknown condiment"


class Milk(CondimentDecorator):
    cond_cost = .1
    def get_description(self):
        return self.beverage.get_description() + ", Milk"

    def cost(self):
        return self.beverage.cost() + self.cond_cost


class Mocha(CondimentDecorator):
    cond_cost = .2
    def get_description(self):
        return self.beverage.get_description() + ", Mocha"

    def cost(self):
        return self.beverage.cost() + self.cond_cost


class Soy(CondimentDecorator):
    cond_cost = .15
    def get_description(self):
        return self.beverage.get_description() + ", Soy"

    def cost(self):
        return self.beverage.cost() + self.cond_cost


class Whip(CondimentDecorator):
    cond_cost = .1
    def get_description(self):
        return self.beverage.get_description() + ", Whip"

    def cost(self):
        return self.beverage.cost() + self.cond_cost


