import threading

from truck import Truck
from dock import Dock
from factory import Factory
from shop import Shop

# Instancia a doca e a fábrica
factory = Factory()
dock = Dock(factory)

# Instancia os caminhões e lojas
trucks = []
shops = []

for i in range(2):
    trucks.append(Truck("Caminhão " + str(i+1)))

for i in range(3):
    shops.append(Shop("Loja " + str(i+1)))

# Inicia as threads dos caminhões
for truck in trucks:
    threading.Thread(target=truck.run, args=(dock, factory)).start()

# Inicia as threads das lojas
for shop in shops:
    threading.Thread(target=shop.run, args=(factory,)).start()