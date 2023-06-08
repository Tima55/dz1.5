#Программа загадывает число от 0 до 1000.
#Необходимо угадать число за 10 попыток. Программа должна
#подсказывать «больше» или «меньше» после каждой попытки.
import random
number = random.randint(0, 1000)
N= int(input('Угадайте число от 0 до 1000, у вас 10 попыток : '))
#print(number)
if N>=0 and N<=1000:
    for i in range(10):
        if N>number:
            print('меньше')
            N= int(input('Угадайте число от 0 до 1000: '))  
        elif N<number:
            print('больше')
            N= int(input('Угадайте число от 0 до 1000: ')) 
        elif N==number:
            print('Вы угадали!!!')    
            break