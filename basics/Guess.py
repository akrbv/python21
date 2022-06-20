import random

guesses_made = 3
name = input('Привет! Введите своё имя?\n')
play = print ('Хочешь играть?'.format(name))
random_value = random.randint(0,100)
attempt = 0
print("Загадано число от 0 до 10. Попробуйте отгадать за 10 попыток")

for i in range(1,11):
    choice = int(input("Введите число: "))
    if choice > random_value:
        print("Многовато будет")
    elif choice < random_value:
        print("Маловато будет")
    else:
        print(f"Точно! Количество попыток - {i}")
        break
    attempt += 1
    print(f"Осталось попыток {10-attempt}")
if attempt >= 10:
    print(f"Попытки закончились! Было загадано {random_value}")
