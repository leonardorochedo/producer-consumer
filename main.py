import threading
import time

from truck import Truck
from dock import Dock
from factory import Factory
from shop import Shop

dock = Dock()
factory = Factory()

trucks = []
shops = []

# Cria os caminhões e as lojas
for i in range(5):
    trucks.append(Truck("Caminhão "+ str(i+1)))
    shops.append(Shop("Loja "+ str(i+1)))

# Inicia as threads
dock.start()
factory.start()

for f in trucks:
    f.start()

for f in shops:
    f.join()