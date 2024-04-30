import os


# Memento pattern, example
class Memento:
    def __init__(self, file, content):
        self.file = file
        self.content = content


class FileWriterUtility:

    def __init__(self, file):
        self.file = file
        self.content = ""

    def write(self, string):
        self.content += string

    def save(self):
        return Memento(self.file, self.content)

    def undo(self, memento):
        self.file = memento.file
        self.content = memento.content


class FileWriterCaretaker:

    def save(self, writer):
        self.obj = writer.save()

    def undo(self, writer):
        writer.undo(self.obj)


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

    print("Undo is invoked")
    caretaker.undo(writer)

    print("The current state is shown")
    print(writer.content + "\n\n")

    print("Undo is invoked again")
    caretaker.undo(writer)

    print("The current state is shown")
    print(writer.content + "\n\n")
