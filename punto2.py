class StringIterator:
    def __init__(self, string):
        self.string = string
        self.index = 0
        self.reverse_index = len(string) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.string):
            char = self.string[self.index]
            self.index += 1
            return char
        else:
            raise StopIteration

    def reverse(self):
        while self.reverse_index >= 0:
            char = self.string[self.reverse_index]
            self.reverse_index -= 1
            yield char


if __name__ == "__main__":
    my_string = "5"

    # Iterating forward
    print("Iterating forward:")
    string_iterator = StringIterator(my_string)
    for char in string_iterator:
        print(char, end=" ")
    print("\n")

    # Iterating backward
    print("Iterating backward:")
    for char in string_iterator.reverse():
        print(char, end=" ")
