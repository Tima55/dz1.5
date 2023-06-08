N = int(input('Сколько рядов у ёлки?: '))
N1 = 0
s = '*'
y = '**'
if N>0:
    while N1 != N:
        N1+=1
        print(s.center(100))
        s+=y
else:
    print('Введите положительное число!!!')