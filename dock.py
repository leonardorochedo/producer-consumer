import threading
from factory import Factory

class Dock():
    def __init__(self, factory: Factory):
        self.truck = None
        self.factory = factory
        self.semaphore = threading.Semaphore(1)

    def unloadTruckInFactory(self, truck, charge):
        self.semaphore.acquire()
        if self.truck is None:
            self.truck = truck
            self.factory.increaseStorage(self.truck.unloadTruck())
            self.truck = None
        else:
            print("Já há um caminhão carregado na doca.")
        self.semaphore.release()
