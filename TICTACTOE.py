import random
tablero = []
#RELLENAR TABLERO
juego =True
for i in range(3):
    fila=[]
    for j in range(3):
        fila+=["□"]
    print(fila)
    tablero.append(fila)


#IMPRIMIR TABLERO
print("Usted es X ----------- la maquina es O")
while juego:
    eleccion = input("Introduzca donde desea poner la ficha(EJEMPLOS: 0,0 | 1,1 | 2,2): ")
    pos = int(eleccion[0])
    pos2 = int(eleccion[2])
    tablero[pos][pos2]="X"
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            print(tablero[i][j],end=" ")
        print()
    for pos2 in range(3):
        if tablero[0][pos2]==tablero[1][pos2]==tablero[2][pos2] and tablero[0][pos2]!="□":
            print("ganaste")
            exit()
    for pos in range(3):
        if tablero[pos][0]==tablero[pos][1]==tablero[pos][2] and tablero[pos][0]!="□":
            print("ganaste")
            exit()
    for i in range(3):
        if tablero[0][0]==tablero[1][1]==tablero[2][2]!="□":
            print("Ganaste")
            exit()
        if tablero[2][2]==tablero[1][1]==tablero[0][0]!="□":
            print("Ganaste")
            exit()