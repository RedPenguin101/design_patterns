import duck as d
import turkey as t
import turkeyadapter as ad

duck = d.MallardDuck()
turkey = t.WildTurkey()

turkeyadapter = ad.TurkeyAdapter(turkey)

print("turkey says:")
turkey.gobble()
turkey.fly()

print("\nduck says:")
duck.quack()
duck.fly()

print("\nturkeyadapter says:")
turkeyadapter.quack()
turkeyadapter.fly()

