import random
def quiz():
    i = 0
    print("*" * 15, "Угадай число", "*" * 15)
    score = 0
    while True:
        rand = random.randint(1, 10)
        number = int(input("Введите ваше число:"))
        i += 1
        if number == 0:
            break
        if number == rand:
            score += 1
            print("Ты угадал число, твой счёт: ", score, "из", i)
        else:
            print("В следующий раз повезёт!")
quiz()
