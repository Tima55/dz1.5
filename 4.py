#Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на
#  единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
N = float(input('Введите число: '))
if N>=0 and N<=100000:
    if N%1==0 and N%N==0:
        print('Число является простым')
    else:
        print('Число является составным')
else:
    print('Не подходит по ограничениям')