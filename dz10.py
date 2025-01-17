import sqlite3
from datetime import datetime
import requests
import time
import signal
import sys


running = True


def handle_signal(sig, frame):
    global running
    print("\nЗавершение программы...")
    running = False


def create_database():
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather_data (
            datetime TEXT,
            temperature REAL
        )
    ''')
    conn.commit()
    conn.close()


def get_temperature(city: str):
    url = f'https://wttr.in/{city}?format=%t'  
    response = requests.get(url)
    if response.status_code == 200:
        temp = response.text.strip()
        if temp.startswith('+') or temp.startswith('-'):
            return float(temp.replace('°C', ''))
        raise ValueError('Невозможно извлечь температуру.')
    else:
        raise Exception(f"Ошибка доступа к {url}: код {response.status_code}")


def insert_weather_data(temp):
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  
    cursor.execute('INSERT INTO weather_data (datetime, temperature) VALUES (?, ?)', (now, temp))
    conn.commit()
    conn.close()


def main():
    city = 'Almaty'  

   
    create_database()

    
    while running:
        try:
            temperature = get_temperature(city)
            insert_weather_data(temperature)
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Температура в {city}: {temperature}°C")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

        
        for _ in range(30 * 60):
            if not running:
                break
            time.sleep(1)

if __name__ == '__main__':
    signal.signal(signal.SIGINT, handle_signal)

    try:
        main()
    except KeyboardInterrupt:
        print("Программа остановлена вручную.")
        sys.exit(0)
