import abc

class GumballMachine:
    def __init__(self, number_of_gumballs: int):
        self.number_of_gumballs = number_of_gumballs

        self.sold_out_state = SoldOutState(self)
        self.sold_state = SoldState(self)
        self.no_quarter_state = NoQuarterState(self)
        self.has_quarter_state = HasQuarterState(self)

        self.current_state = None

        if number_of_gumballs > 0:
            self.current_state = self.no_quarter_state
        else:
            self.current_state = self.sold_out_state

    def set_state(self, state):
        self.current_state = state

    def insert_quarter(self):
        self.current_state.insert_quarter()

    def turn_crank(self):
        self.current_state.turn_crank()

    def eject_quarter(self):
        self.current_state.eject_quarter()

    def release_gumball(self):
        print("a gumball rolls out")
        self.current_state.dispense()
        if self.number_of_gumballs != 0:
            self.number_of_gumballs -= 1


class State(abc.ABC):
    @abc.abstractmethod
    def insert_quarter(self):
        pass

    @abc.abstractmethod
    def turn_crank(self):
        pass

    @abc.abstractmethod
    def eject_quarter(self):
        pass

    @abc.abstractmethod
    def dispense(self):
        pass


class NoQuarterState(State):
    def __init__(self, gumball_machine: GumballMachine):
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        print("you inserted a quarter")
        self.gumball_machine.set_state(self.gumball_machine.has_quarter_state)

    def turn_crank(self):
        print("you need to put a quarter in")

    def eject_quarter(self):
        print("there's no quarter to eject")

    def dispense(self):
        print("you need to put a quarter in")


class HasQuarterState(State):
    def __init__(self, gumball_machine: GumballMachine):
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        print("there's already a quarter in there")

    def turn_crank(self):
        print("the crank turns")
        self.gumball_machine.set_state(self.gumball_machine.sold_state)

    def eject_quarter(self):
        print("the quarter is ejected")

    def dispense(self):
        print("you need to turn the crank first")


class SoldState(State):
    def __init__(self, gumball_machine: GumballMachine):
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        print("you haven't picked up the gumball yet")

    def turn_crank(self):
        print("You can't turn the crank again")

    def eject_quarter(self):
        print("the quarter is ejected")

    def dispense(self):
        if self.gumball_machine.number_of_gumballs == 0:
            self.gumball_machine.set_state(self.gumball_machine.sold_out_state)
            print("sorry, there are no gumballs left")
        else:
            print("the gumball is being dispensed")

        if self.gumball_machine.number_of_gumballs == 1:
            self.gumball_machine.set_state(self.gumball_machine.sold_out_state)
        else:
            self.gumball_machine.set_state(self.gumball_machine.no_quarter_state)


class SoldOutState(State):
    def __init__(self, gumball_machine: GumballMachine):
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        print("there are no gumballs")

    def turn_crank(self):
        print("there are no gumballs")

    def eject_quarter(self):
        print("there are no gumballs")

    def dispense(self):
        print("there are no gumballs")
