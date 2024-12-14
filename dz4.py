result = []
def divider(a, b):
    if a < b:
        raise ValueError
    if b > 100:
        raise IndexError
    return a/b

data = {10: 2, 2: 5, "123": 4, 18: 0, "empty_list": 15, 8 : 4}
for key in data:
    try:
        res = divider(key, data[key])  # Исправлено: data[key], а не data[kem]
        result.append(res)
    except TypeError:
        print(f"TypeError: Операнды должны быть числами. Ключ: {key}, значение: {data[key]}")
    except ValueError:
        print("ValueError: a должно быть больше или равно b")
    except ZeroDivisionError:
        print("ZeroDivisionError: Деление на ноль")
    except IndexError:
        print("IndexError: b не может быть больше 100")
    except KeyError:
        print(f"KeyError: Ключ 'kem' не найден в словаре")
    except Exception as e:
        print(f"Непредвиденное исключение: {e}")

print(result)
