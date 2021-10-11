while 1:
    try:
        i=0
        b= []
        n = int(input("Введите размерность: "))
        if n<0:
            print("Ошибка")
            continue
        while i<n:
            try:
                i+=1
                c = int(input())
                b.append(c)
            except ValueError:
                print("Введи заново")
                i -= 1
        for Y in range(n):
            for P in range(Y, n):
                if b[Y] > b[P]:
                    b[P], b[Y] = b[Y], b[P]
        delta = int(input("Введите delta: " ))
        if delta<0:
            print("Ошибка")
            continue
        k = 0
        for x in b:
            if x == b[0] + delta:
                k+= 1
        print(k)
        break
    except ValueError:
        print("Ошибка")
