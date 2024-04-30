import os


class Memento:
    def __init__(self, file, content):
        self.file = file
        self.content = content


class FileWriterUtility:
    def __init__(self, file):
        self.file = file
        self.content = ""
        self.mementos = []

    def write(self, string):
        self.content += string

    def save(self):
        memento = Memento(self.file, self.content)
        self.mementos.append(memento)
        if len(self.mementos) > 4:
            # Remove the oldest if more than 4 states stored
            self.mementos.pop(0)

    def undo(self, num_back):
        if num_back >= len(self.mementos):
            num_back = len(self.mementos) - 1
        memento = self.mementos[-1 - num_back]
        self.file = memento.file
        self.content = memento.content


class FileWriterCaretaker:
    def save(self, writer):
        writer.save()

    def undo(self, writer, num_back):
        writer.undo(num_back)


if __name__ == '__main__':
    os.system("clear")
    print("Create an object that will manage the previous version")
    caretaker = FileWriterCaretaker()

    print("Create the object whose state is to be preserved")
    writer = FileWriterUtility("GFG.txt")

    print("Something is written to the object and saved")
    writer.write("IS2 class at UADER\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("Additional information is written")
    writer.write("Additional material from the design patterns class\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("Additional information II is written")
    writer.write("Additional material from the design patterns class II\n")
    print(writer.content + "\n\n")

    print("Invoke <undo> to retrieve the second previous state")
    caretaker.undo(writer, 1)
    print("The current state is shown")
    print(writer.content + "\n\n")

    print("Invoke <undo> to retrieve the oldest state")
    caretaker.undo(writer, 3)
    print("The current state is shown")
    print(writer.content + "\n\n")
