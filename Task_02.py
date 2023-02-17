# Задание 2: Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

class Player():
    def __init__(self) -> None:
        self.candies = 0
        self.name = ""
        self.order = 0

candies = 2021    
player1 = Player()
player1.name = "player1"
player2 = Player()     

while True:
    try:
        game_type = int(input(f"С кем будете играть? 1 – с компьютером, 2 – с другим игроком: "))
        if game_type == 1:
            player2.name = "Компьютер"
            break
        elif game_type == 2:
            player2.name = "player2"
            break
    except: print("Некорректный выбор!")
while True:
    try:
        first = int(input(f"Кто делает первый ход? 1 – вы, 2 – {player2.name}: "))
        if first == 1:
            current_player = player1
            current_player.order = 1
            break
        elif first == 2:
            current_player = player2
            current_player.order = 1
            break
    except: print("Некорректный выбор!")
while candies > 0:
    if current_player.name == "Компьютер":
        quantity = candies % 29
    else:
        while True:
            try:
                quantity = int(input(f"Сколько конфет возьмёт {current_player.name}? Введите не более 28: "))
                if quantity <= 28: break
            except: print("Некорректный выбор!")
    candies -= quantity
    current_player.candies += quantity
    if candies > 0:
        print(f"{current_player.name} взял {quantity} конфет, теперь у него {current_player.candies} конфет, а осталось {candies} конфет")
        current_player = player2 if current_player == player1 else player1
    else:
        if current_player == player1:
            current_player.candies += player2.candies
            player2.candies = 0
        else:
            current_player.candies += player1.candies
            player1.candies = 0
        print(f"{current_player.name} взял {quantity} конфет. Конфеты закончились. Всё досталось {current_player.name}")
