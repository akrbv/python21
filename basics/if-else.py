"=============Логические операторы==============="
# логические операторы - выражения, которые возвращают True, если правда, False - если ложь

5 == 5 # True
4 == 5 # False

5 != 5 # False
5 != 2 # True

5 > 10 # False
10 > 5 # True
5 > 5 # False

5 < 10 # True
10 < 5 # False
5 < 5 # False

5 <= 10 # True
10 <= 5 # False
5 <= 5 # True

5 >= 10 # False
10 >= 5 # True
5 >= 5 # True

'5' == 5 # False


"============Boolean Type================"
# Булевый тип данных - имеет всего 2 значения True и False
bool(1) # True
bool(0) # False
bool(-277) # True

bool('hello') # True
bool('') # False
bool(' ') # True

bool(True) # True
bool(False) # False


"============None Type=============="
# None - тип данных с одним значением None, который используется для обозначения пустых значений или отсутствия значения
bool(None) # False
bool('None') # True

a = None
print(bool(a)) # False
print(a is None) # True
# is это проверка на полное соответствие


"==============Условные операторы================"
# условные операторы нужны для того, чтобы при разных входных данных код работал по разному

if условие1:
    тело1
    # будет работать только если условие1 верно

if условие1:
    тело1
    # будет работать только если условие1 верно
else:
    тело2
    # будет работать если условие1 не верно

if условие1:
    тело1
    # будет работать только если условие1 верно
elif условие2:
    тело2
    # будет работать если условие1 не верно и условие2 верно

if условие1:
    тело1
    # будет работать только если условие1 верно
elif условие2:
    тело2
    # будет работать если условие1 не верно и условие2 верно
else:
    тело3
    # будет работать если условие1 не верно и условие2 не верно






# в одной конструкции мы можем использовать только один if
# в одной конструкции мы можем использовать неограниченное кол-во elif или не указывать вообще
# else мы так-же можем использовать только один раз или не указывать вообще












"=============And or not================="
# and - и
# or - или
a = 5
b = 6

a == 5 and b == 6 # True (правая сторона True, левая тоже True)
a == 5 and b == 5 # False (правая сторона True, но левая False)
a == 4 and b == 5 # False (обе стороны False)

a == 5 or b == 6 # True (правая сторона True, левая тоже True)
a == 5 or b == 5 # True (правая сторона True, но левая False)
a == 4 or b == 5 # False (обе стороны False)

# если обе части выдают True - будет True
# если обе части выдают False - будет False
# если одна часть True, вторая False:
# 1. если стоит and - выйдет False
# 2. если стоит or - выйдет True

not True # False
not False # True
not a == 5 # False (потому что a == 5)
not a == 4 # True (потому что a == 5)



'==================Тернарные операторы====================='
# условия в одну строку
тело1 if условие else тело2

res = 'Hello' if a == 5 else 'Bye' 
print(res) 
# Hello, если a == 5
# Bye, если a != 5










a = int(input('Введите число: '))

if a > 0:
    print(f'Число {a} - положительное')
elif a < 0:
    print(f'Число {a} - отрицательное')
else:
    print(f'Число {a} - это 0')



"======FizzBuzz======"
# выведите числа от 1 до 100
# если число кратно 3 - вывести Fizz
# если число кратно 5 - вывести Buzz
# если число кратно и 5 и 3 - вывести FizzBuzz
# если число не кратно ни 5 ни 3 - вывести число

for i in range(1, 17):
    if i % 3 == 0:
        if i % 5 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

for i in range(1, 17):
    if i % 3 == 0 and i % 5 ==0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)




for i in range(1, 17):
    if i % 3 == 0 and i % 5 ==0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

#второй вариант

for i in range(1, 17):
    if i % 3 == 0:
        if i % 5 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

#f - это форматирование строк
#range - создает последовательность, к примеру от 1 до 10
# range(20) - диопазон 

#таски 1
пароль = input('введите пароль: ')
if пароль.isdigit() and len(пароль) >= 8:
    print('Ваш пароль сохранен')

if not пароль.isdigit():
    print('Ваш пароль должен содержать только буквы')

if not len(пароль) >= 8:
    print('Ваш пароль должен содержать не менее 8 символов')

#isdigit он возвращает в true, если в строках содержатся только числа, этот метод относится только к строкам(буквам), состоит из чисел
#len - количество символов (длина)


# таск2
point = input('Введите свои баллы по математике, английскому языку и литературе через запятую: ').split(', ')
math = int(point[0])
english = int(point[1])
litr = int(point[-1])

average = (math + english + litr) / 3
if average > 69:
    print(f'вы допущены к экзаменам. Ваш средний балл составляет: {round(average, 1)}')
else:
    print('вы не допущены к экзаменам : ')

# split - относится к типу данных строки, конвертирует в числа, то есть int
# else - в противном случае
#деление всегда возвращает float
# f - F-строки задаются с помощью литерала «f» перед кавычками. буквально означают «formatted string». Эти строки улучшают читаемость кода, а также работают быстрее чем другие способы форматирования. 
# {} динамическая переменная


f_num = float(input("введите первое число>>"))
oper = input('Введите операцию>>')
s_num = float(input("введите второе число>>"))
if oper == '+':
    print(f_num + s_num)
elif oper == '-':
    print(f_num - s_num)
и тд
input()
while contin == 'y'




lang = 'EN'
lang_opt = input('Enter L to change language or other key to continue:  ')
while lang_opt == 'l':
    if lang == 'RU':
        lang = 'EN'
        lang_opt = input('Enter L to change language or other key to continue:  ')
    else:
        lang = 'RU'
        lang_opt = input('Введите L, чтобы сменить язык, или любую клавишу, чтобы продолжить:  ')
if lang == 'EN':
    f = 'Enter first number:  '
    o = 'Enter operation (+,-, /, *):  '
    s = 'Enter second number:  '
    r = 'Result: '
    e = 'Error'
    v = 'Enter "yes" to continue and other key to finish:  '
if lang == 'RU':
    f = 'Введите первое число:  '
    o = 'Введите операцию (+,-, /, *):  '
    s = 'Введите второе число:  '
    r = 'Результат: '
    e = 'Ошибка'
    v = 'Введите "yes", чтобы продолжить, и любую клавишу, чтобы закончить:  '
prodolzhit = 'yes'
while prodolzhit == 'yes':
    f_num = float(input(f))
    oper = input(o)
    sec_num = float(input(s))
    if oper == '+':
        print(r, f_num + sec_num)
    elif oper == '-':
        print(r, f_num - sec_num)
    elif oper == '/':
        print(r, f_num / sec_num)
    elif oper == '*':
        print(r, f_num * sec_num)
    else:
        print(e)
    prodolzhit = input(v)