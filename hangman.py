from random import choice

попытки = ()
   """
     У вас 6 попыток
    """,
    """
     Осталось 10 попытки
    """,
    """
     Осталось 9 попытки
    """,
    """
     Осталось 8 попытки
    """,
    """
     Осталась 7 попытка
    """,
    """
     Осталась 6 попытка
    """,
    """
     Осталась 5 попытка
    """,
    """
     Осталась 4 попытка
    """,
    """
     Осталась 3 попытка
    """,
    """
     Осталась 2 попытка
    """,
      """
     Осталась 1 попытка
    """,
    """
     К сожалению, попытки закончились :(
    """
)

max_wrong = len(попытки)
WORDS = ('питон', 'игра', 'программирование')

word = choice(WORDS)
so_far = '*' * len(word)
wrong = 0
used = []

while wrong < max_wrong and so_far != word:
    print(попытки[wrong])
    print('\nВы использовали следующие буквы:\n', used)
    print('\nНа данный момент слово выглядит вот так:\n', so_far)

    guess = input('\nВведите своё предположение: ')

    while guess in used:
        print('Вы уже угадали букву', guess)
        guess = input('Введите своё предположение: ')

    used.append(guess)

    if guess in word:
        print('\nДа! \'' + guess + '\' есть в слове!')

        new = ''
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print('\nИзвините, буквы \'' + guess + '\' нет в слове.')
        wrong += 1

if wrong == max_wrong:
    
    print('\nВы проиграли!')
else:
    print('\nВы угадали слово!')

print('\nЗагаданное слово было \'' + word + '\'')
