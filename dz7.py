1)class IterableWithGenerator:
    def __init__(self, data):
        self.data = data
    def __iter__(self):
        # Возвращаем генератор, который будет итерироваться по данным
        return (item for item in self.data)
# Пример использования
iterable = IterableWithGenerator([1, 2, 3, 4, 5])
# Итерация по объекту
for value in iterable:
    print(value)


2)import re

def safe_calculator(func):
    def wrapper(expression):
        try:
            # Проверяем, чтобы в выражении были только разрешённые символы
            if not re.match(r'^[\d+\-*/().\s]+$', expression):
                raise ValueError("Недопустимые символы в выражении")
            # Вызываем оригинальную функцию
            result = func(expression)
            return result
        except ZeroDivisionError:
            return "Ошибка: Деление на ноль"
        except ValueError as ve:
            return f"Ошибка: {ve}"
        except Exception as e:
            return f"Ошибка: {e}"
    return wrapper

@safe_calculator
def calculate(expression):
    return eval(expression)

# Пример использования
print(calculate("2 + 3 * 5"))  # 17
print(calculate("10 / 0"))     # Ошибка: Деление на ноль
print(calculate("2 + два"))    # Ошибка: Недопустимые символы в выражении
print(calculate("2 + (3 * 5")) # Ошибка: invalid syntax
