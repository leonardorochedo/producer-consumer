import threading
import time


class Truck(threading.Thread):
    def __init__(self, name, capacity=100):
        super().__init__()
        self.name = name
        self.capacity = capacity
        self.charge = 0
        self.semaphore = threading.Semaphore(1)
        self.dock = None

    def loadTruck(self, weight):
        self.semaphore.acquire()
        if (self.charge + weight <= self.capacity):
            self.charge += weight
            print(f"Carga de {weight} Kg carregada no caminhão: {self.name}.")
        else:
            print(
                f"Carga de {weight} Kg excede a capacidade do caminhão: {self.name}.")
        self.semaphore.release()

    def unloadTruck(self):
        self.semaphore.acquire()
        print(
            f"Carga de {self.charge} Kg descarregada do caminhão: {self.name}.")
        self.charge = 0
        self.semaphore.release()

    def run(self, dock, factory):
        while True:
            time.sleep(1)
            self.loadTruck(80)
            dock.unloadTruckInFactory(self)
            factory.loadCharge(self.charge)
