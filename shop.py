import threading
import time


class Shop():
    def __init__(self, name, capacity=45):
        self.name = name
        self.capacity = capacity
        self.stock = 0
        self.semaphore = threading.Semaphore(1)

    def loadShop(self, weight):
        self.semaphore.acquire()
        if (self.stock + weight <= self.capacity):
            self.stock += weight
            print(f"Carga de {weight} Kg recebida na loja: {self.name}.")
        else:
            print(
                f"Carga de {weight} Kg excede a capacidade da loja: {self.name}.")
        self.semaphore.release()

    def sellCharge(self):
        self.semaphore.acquire()
        if (self.stock >= 0):
            self.stock = 0
            print(f"Carga de {self.stock} Kg vendida na loja: {self.name}.")
        else:
            print(f"Loja: {self.name} sem estoque para vender.")
        self.semaphore.release()

    def run(self, factory):
        while True:
            time.sleep(1)
            self.loadShop(factory.storage)
            self.sellCharge()
