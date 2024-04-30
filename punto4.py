import os


class State:
    def scan(self):
        raise NotImplementedError()

    def toggle_amfm(self):
        raise NotImplementedError()


class AmState(State):
    def __init__(self, radio):
        self.radio = radio
        self.stations = ["1250", "1380", "1510"]
        self.pos = 0
        self.name = "AM"

    def toggle_amfm(self):
        print("Cambiando a FM")
        self.radio.state = self.radio.fmstate

    def scan(self):
        self.pos += 1
        if self.pos == len(self.stations):
            self.pos = 0
        print("Sintonizando... Estación {} {}".format(
            self.stations[self.pos], self.name))


class FmState(State):
    def __init__(self, radio):
        self.radio = radio
        self.stations = ["81.3", "89.1", "103.9"]
        self.pos = 0
        self.name = "FM"

    def toggle_amfm(self):
        print("Cambiando a AM")
        self.radio.state = self.radio.amstate

    def scan(self):
        self.pos += 1
        if self.pos == len(self.stations):
            self.pos = 0
        print("Sintonizando... Estación {} {}".format(
            self.stations[self.pos], self.name))


class Radio:
    def __init__(self):
        self.fmstate = FmState(self)
        self.amstate = AmState(self)
        self.state = self.fmstate

    def toggle_amfm(self):
        self.state.toggle_amfm()

    def scan(self):
        self.state.scan()


class MemoryRadio:
    def __init__(self):
        self.memory = {
            "M1": {"AM": "1250", "FM": "81.3"},
            "M2": {"AM": "1380", "FM": "89.1"},
            "M3": {"AM": "1510", "FM": "103.9"},
            "M4": {"AM": "1200", "FM": "95.5"}
        }
        self.current_memory = 1

    def next_memory(self):
        self.current_memory += 1
        if self.current_memory > 4:
            self.current_memory = 1

    def scan_memory(self):
        memory_label = "M" + str(self.current_memory)
        am_frequency = self.memory[memory_label]["AM"]
        fm_frequency = self.memory[memory_label]["FM"]
        print(f"Sintonizando memoria {memory_label}: AM {
              am_frequency}, FM {fm_frequency}")


if __name__ == "__main__":
    os.system("clear")
    print("\nCrea un objeto radio y almacena las siguientes acciones")
    radio = Radio()
    memory_radio = MemoryRadio()
    actions = [radio.scan] * 3 + [radio.toggle_amfm] + \
        [radio.scan] * 3 + [memory_radio.scan_memory] * 4
    actions *= 2

    print("Recorre las acciones ejecutando la acción, el objeto cambia la interfaz según el estado")
    for action in actions:
        action()
