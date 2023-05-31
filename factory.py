import threading

class Factory():
    def __init__(self, capacity=135):
        self.capacity = capacity
        self.storage = 0
        self.semaphore = threading.Semaphore(1)

    def loadCharge(self, weight):
        self.semaphore.acquire()
        if (self.storage + weight <= self.capacity):
            self.storage += weight
            print(f"Carga de {weight} Kg armazenada na fábrica.")
            self.semaphore.release()
        else:
            print(f"Carga de {weight} Kg excede a capacidade da fábrica.")
        self.semaphore.release()

    def unloadTruck(self):
        self.semaphore.acquire()
        print(f"Carga de {self.storage} Kg retirada da fábrica.")
        self.storage = 0