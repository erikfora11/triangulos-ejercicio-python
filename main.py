import graficas as graf

menu ="""
Seleccione que grafica le gustaria crear:
1.Triangulo rectangulo.
2.Triangulo rectangulo invertido.
3.Triangulo equilatero
4.Rombo
5.Salir
"""


while(True):
    print(menu)

    opcion = int(input("Ingrese un numero:"))
    
    if opcion == 1:
        graf.grafica1(int(input("ingresa la longitud del triangulo")))
    elif opcion == 2:
        graf.grafica2(int(input("ingresa la longitud del triangulo")))
    elif opcion == 3:
        graf.grafica3(int(input("ingresa la longitud del triangulo")))
    elif opcion == 4:
        graf.grafica4(int(input("ingresa la longitud del triangulo")))
    elif opcion == 5:
        break
