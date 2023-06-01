import threading


class Factory():
    def __init__(self, capacity=135):
        self.capacity = capacity
        self.storage = 0
        self.semaphore = threading.Semaphore(1)

    def increaseStorage(self, charge):
        self.semaphore.acquire()
        if (self.storage + charge <= self.capacity):
            if (charge > 0):
                self.storage += charge
                print(f"Carga de {charge} Kg armazenada na fábrica.")
        else:
            print(f"Carga de {charge} Kg excede a capacidade da fábrica.")
        self.semaphore.release()

    def deliveryStorage(self):
        self.semaphore.acquire()
        print(f"Carga de 40 Kg retirada da fábrica.")
        self.storage -= 40
        self.semaphore.release()
        return 40
