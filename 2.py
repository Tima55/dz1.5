N = str(input('Нажмите Enter: '))
x=2
y=2
N1=1
if N == '':
    while N1!=73:
        z = x * y
        print(x,'X',y,'=',z,"\t")
        N1+=1
        y+=1    
        if y>10:
            print("\n")
            x+=1
            y=2
            y+1
            