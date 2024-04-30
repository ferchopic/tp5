import os


class State:
    """Base class for radio states"""

    def scan(self):
        """Scan to the next station."""
        self.pos += 1
        if self.pos == len(self.stations):
            self.pos = 0
        print("Scanning... Station {} ({})".format(
            self.stations[self.pos], self.name))


class AmState(State):
    """State class for AM radio"""

    def __init__(self, radio):
        self.radio = radio
        self.stations = ["1250", "1380", "1510"]
        self.pos = 0
        self.name = "AM"

    def toggle_am_fm(self):
        """Switch to FM state."""
        print("Switching to FM")
        self.radio.state = self.radio.fm_state


class FmState(State):
    # State class for FM radio

    def __init__(self, radio):
        self.radio = radio
        self.stations = ["81.3", "89.1", "103.9"]
        self.pos = 0
        self.name = "FM"

    def toggle_am_fm(self):
        # Switch to AM state
        print("Switching to AM")
        self.radio.state = self.radio.am_state


class Radio:
    """Radio class with AM and FM states"""

    def __init__(self):
        self.fm_state = FmState(self)
        self.am_state = AmState(self)
        self.state = self.fm_state  # Initial state is FM

    def toggle_am_fm(self):
        """Toggle between AM and FM states."""
        self.state.toggle_am_fm()

    def scan(self):
        """Scan for the next station."""
        self.state.scan()


if __name__ == "__main__":
    os.system("clear")
    print("\nCreating a radio object and storing the following actions")
    radio = Radio()
    actions = [radio.scan] * 3 + [radio.toggle_am_fm] + [radio.scan] * 3
    actions *= 2

    print("Executing actions and observing state changes:")
    for action in actions:
        action()
