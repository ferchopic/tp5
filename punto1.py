class Handler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle(self, number):
        if not self.can_handle(number):
            if self.successor:
                self.successor.handle(number)
            else:
                print(f"The number {
                      number} was not consumed by any class.")

    def can_handle(self, number):
        raise NotImplementedError()


class PrimeHandler(Handler):
    def can_handle(self, number):
        if number > 1:
            for i in range(2, number):
                if number % i == 0:
                    return False
            print(f"The number {
                  number} is prime and was consumed by the prime numbers class.")
            return True
        return False


class EvenHandler(Handler):
    def can_handle(self, number):
        if number % 2 == 0:
            print(f"The number {
                  number} is even and was consumed by the even numbers class.")
            return True
        return False


class NumberProcessor:
    def __init__(self):
        self.handler_chain = EvenHandler(PrimeHandler())

    def process_numbers(self, numbers):
        for number in numbers:
            self.handler_chain.handle(number)


if __name__ == "__main__":
    processor = NumberProcessor()
    numbers_to_process = range(1, 101)
    processor.process_numbers(numbers_to_process)
