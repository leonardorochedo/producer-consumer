import threading

class Truck():
    def __init__(self, name:str, capacity=100):
        self.name = name
        self.capacity = capacity
        self.charge = 0
        self.semaphore = threading.Semaphore(1)

    def loadTruck(self, weight):
        self.semaphore.acquire()
        if(self.charge + weight <= self.capacity):
            self.charge += weight
            print(f"Carga de {weight} Kg carregada no caminhão: {self.name}.")
            self.semaphore.release()
        else:
            print(f"Carga de {weight} Kg excede a capacidade do caminhão: {self.name}.")
        self.semaphore.release()

    def unloadTruck(self):
        self.semaphore.acquire()
        print(f"Carga de {self.load} Kg descarregada do caminhão: {self.name}.")
        self.charge = 0
        self.semaphore.release()