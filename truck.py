import threading
import time


class Truck(threading.Thread):
    def __init__(self, name, capacity=100):
        super().__init__()
        self.name = name
        self.capacity = capacity
        self.charge = 0
        self.semaphore = threading.Semaphore(1)

    def loadTruck(self, weight):
        self.semaphore.acquire()
        if (self.charge + weight <= self.capacity):
            self.charge += weight
            print(f"Carga de {weight} Kg carregada no {self.name}.")
        else:
            print(
                f"Carga de {weight} Kg excede a capacidade do {self.name}.")
        self.semaphore.release()

    def unloadTruck(self):
        self.semaphore.acquire()
        print(
            f"Carga de {self.charge} Kg descarregada do {self.name}.")
        self.charge = 0
        self.semaphore.release()
        return self.charge

    def run(self, dock, factory):
        while True:
            time.sleep(2)
            self.loadTruck(80)
            time.sleep(3)
            dock.unloadTruckInFactory(self, self.charge)
            time.sleep(1)
            factory.increaseStorage(self.charge)
