import random
import sqlite3
import tkinter as tk
from tkinter import messagebox, simpledialog

def initialize_database():
    conn = sqlite3.connect("game_results.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            attempts INTEGER
        )
    """)
    conn.commit()
    conn.close()

def save_result(name, attempts):
    conn = sqlite3.connect("game_results.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO results (name, attempts) VALUES (?, ?)", (name, attempts))
    conn.commit()
    conn.close()

def show_leaderboard():
    conn = sqlite3.connect("game_results.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT name, COUNT(id) as victories
        FROM results
        GROUP BY name
        ORDER BY victories DESC
        LIMIT 10
    """)
    results = cursor.fetchall()
    conn.close()

    leaderboard = "Таблица лидеров:\n\n"
    for idx, (name, victories) in enumerate(results, start=1):
        leaderboard += f"{idx}. {name}: {victories} побед\n"

    messagebox.showinfo("Таблица лидеров", leaderboard)

def check_guess(app, guess):
    app.attempts += 1
    if guess == app.ball_position:
        name = simpledialog.askstring("Поздравляем!", "Введите ваше имя:")
        if name:
            save_result(name, app.attempts)
        messagebox.showinfo("Поздравляем!", f"Вы угадали! Шарик был под стаканом {guess}. Попыток: {app.attempts}")
        reset_game(app)
    else:
        update_cups(app)

def update_cups(app):
    for i in range(3):
        cup_label = app.cups[i]
        if i + 1 == app.ball_position:
            cup_label.config(text="O") if app.show_ball else cup_label.config(text="[ ]")
        else:
            cup_label.config(text="[ ]")

def reset_game(app):
    app.ball_position = random.randint(1, 3)
    app.attempts = 0
    update_cups(app)

def toggle_ball_visibility(app):
    app.show_ball = not app.show_ball
    update_cups(app)

class BallGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Угадай, где шарик")
        
        self.ball_position = random.randint(1, 3)
        self.attempts = 0
        self.show_ball = False
        
        self.cups = []
        for i in range(3):
            btn = tk.Button(root, text="[ ]", font=("Arial", 24), width=5, height=2, command=lambda i=i: check_guess(self, i + 1))
            btn.grid(row=0, column=i, padx=10, pady=10)
            self.cups.append(btn)
        
        self.toggle_button = tk.Button(root, text="Показать/Скрыть шарик", command=lambda: toggle_ball_visibility(self))
        self.toggle_button.grid(row=1, column=0, columnspan=3, pady=10)

        self.leaderboard_button = tk.Button(root, text="Таблица лидеров", command=show_leaderboard)
        self.leaderboard_button.grid(row=2, column=0, columnspan=3, pady=10)
        
        update_cups(self)

if __name__ == "__main__":
    initialize_database()
    root = tk.Tk()
    app = BallGameApp(root)
    root.mainloop()
