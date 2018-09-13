__author__ = 'Иванов Сергей Борисович'
# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    pass


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))

def my_round(a,b):
    lst=str(a).split('.')
    a1 = lst[0]
    a2 = lst[1]
    print('Число: ' + str(a) + ' округляем до ' + str(b) + ' знаков после запятой')
    if (int(a2[b])) < 5:
        #Удаляем лишние нули справа
        res = del_zero(a2[0:b])
        res = a1 +'.' + str(res)
    else:
        res = int(a2[0:b]) + 1
        if len(str(res)) > b:
            res = int(a1)+1
        else:
            res = del_zero(res)
            res = a1 +'.' + str(res)
    return(str(res))

def del_zero(item):
    while not (int(item) % 10):
        item = int(item) // 10
    return item
    
print('Результат: ', my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    pass


print(lucky_ticket(123006))
print(lucky_ticket(123213))
print(lucky_ticket(436751))

def lucky_ticket(bilet):
    sum1 = summa(str(bilet)[0:3])
    sum2 = summa(str(bilet)[3:])
    if sum1 == sum2:
        return 'Счастливый'
    else:
        return 'Не счастливый'

def summa(my_string):
    my_sum = 0
    for i in range(len(my_string)):
        my_sum+=int(my_string[i])
    return my_sum

print(lucky_ticket(123006))
