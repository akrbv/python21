'=============Функции================='

# Функция - это именованный блок кода, который может принимать аргументы
# и возвращать результат
# Функция всегда возвращает что-то, пишутся с маленькой буквы и принято называть глаголом 

           # в скобочки передаем параметры - это переменные
def my_sum(a,b):
    return a + b, a/b, a*b  - #можно использовать несколько вариантов, они перейдут в tuple

res = my_sum(5,4)
print(res)

#пример №2
def my_sum(a,b):
    return a + b

res = my_sum(5,4)
print(res) #9

'================параметры==================' это перемнные 
# параметры - локальные переменные внутри функции,значения которым мы задаем при вызове функции
# функции (переменные, которые мы указали внутри скобочек при создании функции(когда написали def))
# сначала определяем обязательные, потом с дефолтом, потом *, и в конце **

'================виды параметров=================='
# бывают обязательные и необязательные 

# 1) обязательные
# 2) необязательные
# 2.1) по дефолту (со значением по умолчанию) (объявляем переменную со значение через =)
# 2.2) args (нужны чтобы передавать несколько аргументов)
# 2.3) kwargs 

 
'================Аргументы==================' это значения
# это значения, которые мы передаем параметрам при вызове функции 
# бывают позиционными и именованными
# сначала всегда передаются позиционные потом именнованные


# 1) позиционные
# 2) именованные
def sum_or_add_10(a,b=10):
    #b - параметр с дефолтом 10
    return a+b

print(sum_or_add_10(2,3)) #5
print(sum_or_add_10(5)) #15
print(sum_or_add_10(2,9)) #11
print(sum_or_add_10(15)) #25


'================== * - звездочка====================='
# 1. знак умножения
# 2. распаковка

# распаковка 1 звездой списки
list_ [1,2,3,4,5]
list2 = [*list_] #распаковываем значения в списке в новый список, то же самое, что и comprehension

# дописать про dict



# объединяем все 

пример с def
def func2



# пример с базой данных

database = {
        'Бекзат': "скала"
        "Эртай" : "пароль"
        "Оомат" : "кыргызстан"
        "имран" : "12345"
        "Жийде" : "return"
        "Манас" : "маке"
        "Арафат": "54321"
        "Гулсана": "312"
        "Бекназ": "Арёль"
        "Закир": "@@@"
        "Айгерим": "moon02"

}
def login(**data):
    username = data.get('username')
    password = data.get('password')
    