import threading
import time


class Shop():
    def __init__(self, name, capacity=45):
        self.name = name
        self.capacity = capacity
        self.stock = 0
        self.semaphore = threading.Semaphore(1)

    def loadStock(self, weight):
        self.semaphore.acquire()
        if (self.stock + weight <= self.capacity):
            self.stock += weight
            print(f"Carga de {weight} Kg recebida na {self.name}.")
        else:
            print(
                f"Carga de {weight} Kg excede 1a capacidade da {self.name}.")
        self.semaphore.release()

    def sellStock(self):
        self.semaphore.acquire()
        if (self.stock > 0):
            print(f"Carga de {self.stock} Kg vendida na {self.name}.")
            self.stock = 0
        else:
            print(f"{self.name} sem estoque para realizar a venda.")
        self.semaphore.release()

    def run(self, factory):
        while True:
            time.sleep(1)
            self.loadStock(factory.deliveryStorage())
            time.sleep(1)
            self.sellStock()
