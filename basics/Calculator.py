f_num = (input("введите первое число>> "))
oper = input('Выберите операцию из следующих +-*/%**// : * >> ')
s_num = (input("введите второе число>> "))

if oper == '+':
    print(f_num + s_num)
elif oper == '-':
    print(f_num - s_num)
elif oper == '/':
    print(f_num / s_num)
elif oper == '*':
    print(f_num * s_num)
elif oper == '%':
    print(f_num % s_num)
elif oper == '//':
    print(f_num // s_num)
elif oper == '**':
    print(f_num ** s_num)
else:
    print('Данной операции нет в системе')