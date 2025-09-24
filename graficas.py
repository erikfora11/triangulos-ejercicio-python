def grafica1(x):
    i,j  =0,0
    while i < x:
        j = 0
        while j < i:
            print("*",end="")
            j += 1
        i += 1
        print("")

def grafica2(x):
    i,j  =0,0
    while i < x:
        j = x - i
        while j > 0:
            print(" ",end="")
            j -= 1
        j = 0
        while j < i:
            print("*",end="")
            j += 1
        i += 1  
        print("")      

def grafica3(x):
     i,j  =0,0
     while i < x:
        j = 0
        espacios = x - i - 1
        asteriscos = 2 * i + 1
        while j<espacios:
            print(" ",end="")
            j += 1
        j = 0
        while j < asteriscos:
            print("*",end="")
            j += 1
        print("")    
        i += 1

def grafica4(x):
     i,j  =0,0
     while i < x:
        j = 0
        espacios = x - i + 1
        asteriscos = 2 * i + 1
        print(" "*espacios + "*"*asteriscos+" "*asteriscos)
        i += 1
     i = x
     while i >= 0: 
        espacios = x - i + 1
        asteriscos = 2 * i + 1
        print(" "*espacios + "*"*asteriscos+" "*asteriscos)
        i -= 1
