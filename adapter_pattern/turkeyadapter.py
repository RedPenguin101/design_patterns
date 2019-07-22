from turkey import Turkey
from duck import Duck


class TurkeyAdapter(Duck):
    def __init__(self, turkey: Turkey):
        self.turkey = turkey

    def quack(self):
        self.turkey.gobble()

    def fly(self):
        for i in range(5):
            self.turkey.fly()
