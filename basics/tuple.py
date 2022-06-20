"=============Tuple================"
# кортеж - неизменяемый, индексиремый, упорядоченный, итерируемый тип данных, предназначенный для хранения любых данных в определенном порядке (в целом не отличается от списков, просто не изменяемый, поэтому занимает меньше памяти)

tuple1 = (1,2,3) # (1,2,3)
tuple2 = ('hello', 2.5, 19, (2,3), [1,2,3])
tuple3 = tuple('hello') # ('h', 'e', 'l', 'l', 'o')
tuple4 = tuple([1,2,3]) # (1,2,3)

tuple4 = 1,2,3 # (1,2,3)
tuple5 = (5) # 5 (int)
tuple6 = 5, # (5,)
tuple7 = 'hello',


"==========Методы tuple============"
# count считает количество принятого элемента в кортеже
list_ = (1,2,1,4,1,5,1,7,2,4,4)
list_.count(1) # 4
list_.count(2) # 2
list_.count(4) # 3

list_ = ('hello', 'hello', 'hello')
list_.count('h') # 0
list_.count('hello') # 3
len(list_) # 3

# index возвращает индекс первого вхождения принятого элемента
list1 = (1,2,3,4,1,2,3,5,4,1)
list1.index(3) # 2
list1.index(1) # 0



for k in dict.keys():
    print(k)


dict_ = {"a":2, "b":3, "c":4}
print dict_.keys(3)

















list_ = [1,2,3]
if list_.count(list_[0]) > 1 or list_.count(list_[1]) > 1:
    print('yes')
elif list_.count(list_[2]) > 1:
    print('yes')
else:
    print('ERROR')