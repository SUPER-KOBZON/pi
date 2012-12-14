working = True
while working:
    from decimal import*
    try:
        x =input('Вывести П?: (Yes/No)\n')
        if x in ("Да", "yes", "Yes", "y", "Y", "да"):
            g = int (input('С точностью до какого знака вывести П?: \n'))
            
            def Pu(g):    
                precision = 5
                getcontext().prec = int(g)

                a = 1
                b = Decimal(1) / Decimal(2).sqrt()
                t = Decimal(1) / Decimal(4)
                p = 1
                pi = 0
                for x in range(0, precision):
                    nextA = (a + b) / 2
                    nextB = (a * b).sqrt()
                    nextT = t - p * ((a - nextA) ** 2)
                    nextP = 2 * p
                    pi = ((a + b) ** 2) / (4 * t)
                    a,b,t,p = nextA,nextB,nextT,nextP
                print (pi)
                
            Pu(g)
        else:
                raise ValueError
    except ValueError:
        f = input("ведены неверные значения, продолжить?(Yes/No) \n")
        if f not in ("Да", "yes", "y", "Y" "Yes","да"):
            working = False
            print("КОНЕЦ!")
    
            

