import random

class CipherObject:
    def __init__(self, *numbers):
        self._numbers = numbers  
        self._result = self._process_numbers()  

    def _process_numbers(self):
        operations = [
            (lambda x, y: x + y, 'сложение'),
            (lambda x, y: x - y, 'вычитание'),
            (lambda x, y: x * y, 'умножение'),
            (lambda x, y: x / y if y != 0 else 0, 'деление')
        ]
        result = self._numbers[0]
        for num in self._numbers[1:]:
            operation, name = random.choice(operations)
            result = operation(result, num)
        return round(result, 2)

    def __str__(self):
        return f"Результат вычислений: {self._result}"


cipher = CipherObject(10, 5, 3)
print(cipher)
