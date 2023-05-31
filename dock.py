import threading


class Dock():
    def __init__(self):
        self.truck = None
        self.semaphore = threading.Semaphore(1)

    def unloadTruckInFactory(self, truck):
        self.semaphore.acquire()
        if self.truck is None:
            self.truck = truck
            self.truck.unloadTruck()
            self.truck = None
        else:
            print("Já há um caminhão carregado na doca.")
        self.semaphore.release()
