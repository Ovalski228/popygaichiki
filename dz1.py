class Cat:
    def __init__(self, name):
        self.name = name
        self.hunger = 0  # Уровень голода (0 - не голоден, 10 - очень голоден)
        self.energy = 10  # Уровень энергии (0 - устал, 10 - полон энергии)
        self.mood = 5  # Настроение (0 - плохое, 10 - отличное)

    def eat(self, food_amount):
        if food_amount > 0:
            self.hunger = max(0, self.hunger - food_amount)
            print(f"{self.name} поел(а) и теперь голод = {self.hunger}")
        else:
            print(f"{self.name} не хочет есть.")

    def sleep(self, hours):
        if hours > 0:
            self.energy = min(10, self.energy + hours)
            print(f"{self.name} поспал(а) и теперь энергия = {self.energy}")
        else:
            print(f"{self.name} не хочет спать.")

    def play(self, time):
        if time > 0 and self.energy > 0:
            self.energy = max(0, self.energy - time)
            self.mood = min(10, self.mood + time // 2)
            print(f"{self.name} играл(а) {time} минут и теперь энергия = {self.energy}, настроение = {self.mood}")
        else:
            print(f"{self.name} слишком устал(а) для игры.")

    def show_status(self):
        print(f"{self.name}: голод = {self.hunger}, энергия = {self.energy}, настроение = {self.mood}")

cat = Cat("Барсик")
cat.show_status()
cat.eat(3)
cat.sleep(5)
cat.play(20)
cat.show_status()
