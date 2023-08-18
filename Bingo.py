import random
from colorama import Back, Fore, init, Style
init(autoreset=True)

#Funciones
def crear_carton():
    '''Llena la matriz de un tamaño definido de 7x8 con strings vacías.'''
    matriz = [[""] * 7 for i in range(8)]
    return matriz

def mostrar_carton(matriz_jugador, matriz_pc):
    '''Imprime la matriz que conforma el cartón de bingo.'''
    
    '''!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'''
    for f in range(8):
        for c in range(7):
            print("%4s" %matriz_jugador[f][c], end="")
            if c==5:
                print("                   ", end="")
        for c in range(7):
            print("%4s" %matriz_pc[f][c], end="")
        print()
    
       
def llenar_carton(mat, bingo):
    '''Rellena el cartón evitando números repetidos en una misma columna.'''
    for f in range(8):
        for c in range(7):
            if f == 0 or f == 7 or c == 0 or c == 6:
                pass
            elif f == 1:
                mat[f][c] = bingo[c-1]               
            else:
                flag=False
                while flag==False:
                    if c==1:
                        n=random.randint(1,15)
                    elif c==2:
                        n=random.randint(16,30)
                    elif c==3:
                        n=random.randint(31,45)
                    elif c==4:
                        n=random.randint(46,60)
                    else:
                        n=random.randint(61,75)
                
                    flag=verificar_valor(n, c, mat) 
                
                mat[f][c]=n
                
    return mat

def verificar_valor(n, c, mat):
    flag=True
    for f in range(2,7):
        if n==mat[f][c]:
            flag=False
            break
    return flag
    
def presentacion_juego():
    try:
        archivo=open("BingoInicio.txt", "rt")
        linea=archivo.readline()
        while linea:
            print(linea.rstrip())
            linea=archivo.readline()
    except FileNotFoundError as mensaje:
        print("No se puede leer el archivo:", mensaje)
    except OSError as mensaje:
        print("No se puede leer el archivo:", mensaje)
    finally:
        try:
            archivo.close()
        except NameError:
            pass

def imprimir_reglas():
    while True:
        try:
            print("¿Desea leer las reglas?")
            respuesta=input("Ingrese SÍ o NO: ")
            respuesta=respuesta.upper()
            assert respuesta=="SI" or respuesta=="SÍ" or respuesta=="NO" 
            break
        except AssertionError:
            print("La respuesta ingresada no es válida.")
    
    if respuesta=="SI" or respuesta=="SÍ":
        try:
            reglas=open("BingoReglas.txt", "rt", encoding="utf8")
            linea=reglas.readline()
            while linea:
                print(linea.rstrip())
                linea=reglas.readline()
        except FileNotFoundError as mensaje:
            print("No se puede leer el archivo:", mensaje)
        except OSError as mensaje:
            print("No se puede leer el archivo:", mensaje)
            
        finally:
            try:
                reglas.close()
            except NameError:
                pass
    
def determinar_dificultad():
    '''Determina la cantidad de bolillas que van a ser extraídas durante la partida de bingo'''
    print()
    print("Hay tres dificultades posibles: ")
    print("1. Fácil (Largo del juego: 60 bolillas)")
    print("2. Media (Largo del juego: 55 bolillas)")
    print("3. Difícil (Largo del juego: 50 bolillas)")
    print()
    while True:
        try:
            dificultad=int(input("Elija la dificultad del juego: "))
            assert 1<=dificultad<=3
            break
        except AssertionError:
            print("La dificultad varía entre 1 y 3. Inténtelo de nuevo.")
   
    print("La dificultad elegida es: ", dificultad)
    
    if dificultad==1:
        cantidad=60
    elif dificultad==2:
        cantidad=55
    else:
        cantidad=50
    return cantidad
    
#-----------------------FUNCIONES DEL JUEGO------------------------------
def verificar_respuesta_si_no():
    while True:
        try:
            print("¿Desea tachar algún número de su cartón?")
            respuesta=input("Ingrese SÍ o NO: ")
            respuesta=respuesta.upper()
            assert respuesta=="SI" or respuesta=="SÍ" or respuesta=="NO" 
            break
        except AssertionError:
            print("La respuesta ingresada no es válida.")
            
    return respuesta

def verificar_columna():
    while True:
        try:
            print("¿En qué columna desea tachar un número?")
            respuesta=input("Las respuestas válidas son las letras 'B', 'I', 'N', 'G', 'O': ")
            respuesta=respuesta.upper()
            assert respuesta=="B" or respuesta=="I" or respuesta=="N" or respuesta=="G" or respuesta=="O"
            break
        except AssertionError:
            print("La columna ingresada no es válida.")
            
    return respuesta

def verificar_fila():
    while True:
        try:
            print("¿En qué fila desea tachar un número?")
            respuesta=int(input("Las filas se enumeran del 1 al 5: "))
            assert 1<=respuesta<=5
            break
        except AssertionError:
            print("La fila ingresada no es válida.")
            
    return respuesta

def ubicar_coordenada(carton, columna, fila):
    fila=fila+1
    if columna=="B":
        columna=1
    elif columna=="I":
        columna=2
    elif columna=="N":
        columna=3
    elif columna=="G":
        columna=4
    else:
        columna=5
    
    return columna, fila 

#------------------------------SUMA DE PUNTOS--------------------
def contar_puntos(carton):
    puntos=0
    puntos=puntos+puntos_filas(carton)*100
    puntos=puntos+puntos_columnas(carton)*100
    puntos=puntos+puntos_diagonal_primaria(carton)*200
    puntos=puntos+puntos_diagonal_secundaria(carton)*200
    puntos=puntos+esquinas(carton)*50
    puntos=puntos+bonus(carton)*500
    
    return puntos

def puntos_filas(carton):
    flag=True
    cont=0
    for f in range (2, 7):
        for c in range (1, 6):
            if carton[f][c]!="X":
                flag=False
        if flag==True:
            cont=cont+1
        else:
            flag=True
    return cont

def puntos_columnas(carton):
    flag=True
    cont=0
    for c in range (1, 6):
        for f in range (2, 7):
            if carton[f][c]!="X":
                flag=False
        if flag==True:
            cont=cont+1
        else:
            flag=True
    return cont

def puntos_diagonal_primaria(carton):
    flag=True
    cont=0
    fila=2
    columna=1
    while fila<=6:
        if carton[fila][columna]!="X":
            flag=False
            break
        else:
            fila=fila+1
            columna=columna+1
    if flag==True:
        return 1
    else:
        return 0

def puntos_diagonal_secundaria(carton):
    flag=True
    cont=0
    fila=6
    columna=2
    while fila>=2:
        if carton[fila][columna]!="X":
            flag=False
            break
        else:
            fila=fila-1
            columna=columna+1
    if flag==True:
        return 1
    else:
        return 0

def esquinas(carton):
    if carton[2][1]=="X" and carton[2][5]=="X" and carton[6][1]=="X" and carton[6][5]=="X":
        return 1
    else:
        return 0
    
def bonus(carton):
    flag=True
    for f in range(2, 7):
        for c in range(1, 6):
            if carton[f][c]!="X":
                flag=False
                break
    
    if flag==True:
        return 1
    else:
        return 0

#-----------------FIN CONTADOR DE PUNTOS--------------------------

#Programa principal

#-----------------Preparación del juego-----------------
presentacion_juego()
print()
imprimir_reglas()
print()
print("Ahora sí, ¡comencemos!")
cantidad=determinar_dificultad()
carton_jugador=crear_carton()
carton_pc=crear_carton()
bingo = ["B","I","N","G","O"]
carton_jugador=llenar_carton(carton_jugador, bingo)
carton_pc=llenar_carton(carton_pc, bingo)
while carton_jugador==carton_pc:
    carton_pc=llenar_carton(carton_pc)
#-----------------------------------------------
'''CREACIÓN DEL BOLILLERO'''
mostrar_carton(carton_jugador, carton_pc)

bolillero=()
for i in range(1, 76):
    bolillero=bolillero+(i,)
    
bolillas_jugador=[]
bolillas_pc=[]
bolillas_salidas=[]

#---------------------Desarrollo del juego----------------------------
#-------------------Sacar bolilla del bolillero-----------------------
for i in range(cantidad):
    numero_bolilla=random.choice(bolillero)
    
    while numero_bolilla in bolillas_salidas:
        numero_bolilla=random.choice(bolillero)
    
    print("Ha salido la bolilla", numero_bolilla)
    print()
    bolillas_salidas.append(numero_bolilla)

    '''Verificar bolilla en el cartón del jugador'''

    respuesta1=verificar_respuesta_si_no()
    print()
    while respuesta1=="SÍ" or respuesta1=="SI":
        columna=verificar_columna()
        print()
        fila=verificar_fila()
        print()
        columna, fila=ubicar_coordenada(carton_jugador, columna, fila)
        if numero_bolilla==carton_jugador[fila][columna]:
            print("El número", numero_bolilla, "se encuentra en la coordenada indicada.")
            carton_jugador[fila][columna]="X"
            bolillas_jugador.append(numero_bolilla)
            break
        else:
            print("El número de la coordenada no coincide con el de la bolilla.")
            respuesta1=verificar_respuesta_si_no()

    '''Verificar bolilla en el cartón de la PC'''

    for f in range(2,7):
        for c in range (1, 6):
            if carton_pc[f][c]==numero_bolilla:
                carton_pc[f][c]="X"
                bolillas_pc.append(numero_bolilla)
                break
    print()        
    print(bolillas_salidas)
    mostrar_carton(carton_jugador, carton_pc)
    print(bolillas_jugador)
    print(bolillas_pc)
    print()

#----------------CONTAR PUNTOS--------------------

print("Ya salieron todas las bolillas.")
print()
puntos_jugador=contar_puntos(carton_jugador)
puntos_pc=contar_puntos(carton_pc)
print(puntos_jugador, puntos_pc)
