class Subject:
    def __init__(self):
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def unsubscribe(self, observer):
        self.observers.remove(observer)

    def notify(self, id):
        for observer in self.observers:
            observer.update(id)


class Observer:
    def __init__(self, id):
        self.id = id

    def update(self, received_id):
        if received_id == self.id:
            print(
                f"¡El ID {received_id} coincide con el ID del Observer {self.id}!")


class ObserverA(Observer):
    def __init__(self):
        super().__init__("ABCD")


class ObserverB(Observer):
    def __init__(self):
        super().__init__("EFGH")


class ObserverC(Observer):
    def __init__(self):
        super().__init__("IJKL")


class ObserverD(Observer):
    def __init__(self):
        super().__init__("MNOP")


if __name__ == "__main__":
    subject = Subject()
    observer_a = ObserverA()
    observer_b = ObserverB()
    observer_c = ObserverC()
    observer_d = ObserverD()

    subject.subscribe(observer_a)
    subject.subscribe(observer_b)
    subject.subscribe(observer_c)
    subject.subscribe(observer_d)

    # Emitiendo 8 IDs
    ids = ["ABCD", "1234", "EFGH", "5678", "IJKL", "9101", "MNOP", "1112"]
    print("Emisión de IDs:")
    for id in ids:
        subject.notify(id)
