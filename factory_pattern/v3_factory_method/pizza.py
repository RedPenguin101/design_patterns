# pizza.py
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
        # this is the method which acts as a factory, hence Factory Method
        # pattern
        pass


class NYStylePizzaStore(PizzaStore):

    def create_pizza(self, type: str):

        pizza = None

        if type == 'cheese':
            pizza = NYStyleCheesePizza()
        elif type == 'greek':
            pizza = NYStyleGreekPizza()
        elif type == 'pepperoni':
            pizza == NYStylePepperoniPizza()

        return pizza


class ChicagoStylePizzaStore(PizzaStore):

    def create_pizza(self, type: str):

        pizza = None

        if type == 'cheese':
            pizza = ChicagoStyleCheesePizza()
        elif type == 'greek':
            pizza = ChicagoStyleGreekPizza()
        elif type == 'pepperoni':
            pizza == ChicagoStylePepperoniPizza()

        return pizza


class Pizza(abc.ABC):

    def __init__(self):
        self.name = None

        self.is_prepared = False
        self.is_baked = False
        self.is_cut = False
        self.is_boxed = False

        self.dough = None
        self.sauce = None
        self.toppings = []

    def prepare(self):
        print(f'preparing {self.name}')
        print('tossing dough...')
        print('adding sauce...')
        print('adding toppings: ')
        for topping in self.toppings:
            print(topping)

        self.is_prepared = True

    def bake(self):
        print('bake for 25 mins at 350')
        self.is_baked = True

    def cut(self):
        print('cutting the pizza into 8 slices')
        self.is_cut = True

    def box(self):
        print('put pizza in official box')
        self.is_boxed = True


class NYStyleCheesePizza(Pizza):

    def __init__(self):

        self.name = "NY style sauce and cheese pizza"

        self.is_prepared = False
        self.is_baked = False
        self.is_cut = False
        self.is_boxed = False

        self.dough = "thin crust style"
        self.sauce = "marinara sauce"
        self.toppings = ['Grated reggiano cheese']


class NYStyleGreekPizza(Pizza):
    pass

class NYStylePepperoniPizza(Pizza):
    pass

class ChicagoStyleGreekPizza(Pizza):
    pass

class ChicagoStyleCheesePizza(Pizza):

    def __init__(self):

        self.name = "Chicago style sauce and cheese pizza"

        self.is_prepared = False
        self.is_baked = False
        self.is_cut = False
        self.is_boxed = False

        self.dough = "thick crust style"
        self.sauce = "plum tomato sauce"
        self.toppings = ['shredded mozzarella cheese']

    def cut(self):
        print('cutting the pizza into square slices')
