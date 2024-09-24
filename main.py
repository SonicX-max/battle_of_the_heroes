import random


# Класс героя
class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        damage = random.randint(0, self.attack_power)
        other.health -= damage
        print(f"{self.name} атакует {other.name} на {damage} урона!")

    def is_alive(self):
        return self.health > 0

    def get_health(self):
        # Возвращаем 0, если здоровье героя отрицательное
        return max(self.health, 0)


# Класс игры
class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        print(f"Игра началась! {self.player.name} против Компьютера.")

        while self.player.is_alive() and self.computer.is_alive():
            # Ход игрока
            input("Нажмите Enter, чтобы атаковать!")
            self.player.attack(self.computer)
            self.show_health()
            if not self.computer.is_alive():
                print(f"{self.player.name} победил!")
                break

            # Ход компьютера
            self.computer.attack(self.player)
            self.show_health()
            if not self.player.is_alive():
                print("Компьютер победил!")
                break

        self.ask_for_rematch()

    def show_health(self):
        # Отображаем здоровье игрока и компьютера, если оно < 0, выводим как 0
        print(f"У {self.player.name} осталось {self.player.get_health()} здоровья.")
        print(f"У Компьютера осталось {self.computer.get_health()} здоровья.\n")

    def ask_for_rematch(self):
        while True:
            choice = input("Хотите сыграть еще раз? (да/нет): ").strip().lower()
            if choice == 'да':
                self.reset_game()
                break
            elif choice == 'нет':
                print("Спасибо за игру! До встречи!")
                exit(0)
            else:
                print("Неверный ввод, попробуйте снова.")

    def reset_game(self):
        # Сброс здоровья для новой игры
        self.player.health = 100
        self.computer.health = 100
        self.start()


# Запуск игры
def main():
    player_name = input("Введите имя вашего героя: ")
    game = Game(player_name)
    game.start()


if __name__ == "__main__":
    main()
