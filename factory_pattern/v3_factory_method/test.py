from pizza import NYStylePizzaStore, ChicagoStylePizzaStore

nyStore = NYStylePizzaStore()
chiStore = ChicagoStylePizzaStore()

pizza = nyStore.order_pizza('cheese')
print('------------------------')

pizza = chiStore.order_pizza('cheese')
