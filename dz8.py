import tkinter as tk
import requests
from bs4 import BeautifulSoup
from tkinter import messagebox

def get_dollar_exchange_rate():
    url = "https://www.cbr.ru/scripts/XML_daily.asp"
    response = requests.get(url)

    if response.status_code != 200:
        return None

    # Парсинг XML
    from xml.etree import ElementTree as ET
    tree = ET.fromstring(response.content)

    # Находим курс доллара
    for valute in tree.findall(".//Valute"):
        if valute.find("CharCode").text == "USD":
            value = valute.find("Value").text
            nominal = int(valute.find("Nominal").text)
            return float(value.replace(",", ".")) / nominal

    return None

def on_convert_button_click():
    try:
        amount = float(entry_amount.get())
        converter = CurrencyConverter()
        result = converter.convert_to_usd(amount)
        label_result.config(text=f"{amount} в вашей валюте = {result:.2f} USD")
    except ValueError as ve:
        messagebox.showerror("Ошибка", str(ve))
    except Exception as e:
        messagebox.showerror("Ошибка", "Произошла ошибка при конвертации.")
        
class CurrencyConverter:
    def __init__(self):
        self.dollar_rate = get_dollar_exchange_rate()
        if self.dollar_rate is None:
            raise ValueError("Не удалось получить курс доллара с сайта Центрального банка России.")

    def convert_to_usd(self, amount: float):
        return amount / self.dollar_rate


# Создание окна
root = tk.Tk()
root.title("Конвертер валют")

# Добавление элементов интерфейса
label_instruction = tk.Label(root, text="Введите количество вашей валюты:")
label_instruction.pack(padx=10, pady=5)

entry_amount = tk.Entry(root)
entry_amount.pack(padx=10, pady=5)

convert_button = tk.Button(root, text="Конвертировать в USD", command=on_convert_button_click)
convert_button.pack(padx=10, pady=10)

label_result = tk.Label(root, text="")
label_result.pack(padx=10, pady=5)

# Запуск интерфейса
root.mainloop()
