from time import gmtime, strftime

m = [[5,3,"","",7,"","","",""],[6,"","",1,9,5,"","",""],["",9,8,"","","","",6,""],[8,"","","",6,"","","",3],[4,"","",8,"",3,"","",1],[7,"","","",2,"","","",6],["",6,"","","","",2,8,""],["","","",4,1,9,"","",5],["","","","",8,"","",7,9]] # Matriz del tablero estándar.

inicio = [[0, 0], [0, 1], [0, 4], [1, 0], [1, 3], [1, 4], [1, 5], [2, 1], [2, 2], [2, 7], [3, 0], [3, 4], [3, 8], [4, 0], [4, 3], [4, 5], [4, 8], [5, 0], [5, 4], [5, 8], [6, 1], [6, 6], [6, 7], [7, 3], [7, 4], [7, 5], [7, 8], [8, 4], [8, 7], [8, 8]] # Posiciones inmutables.

base = 0 # Número que define la base numérica.

letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I"] # Letras que representan las filas de las jugadas hechas.


"""

Índice de variables

m = Matriz a jugar.
inicio = Posición de los números iniciales.
base = Número que define la base numérica. Si es 0 la base a mostrar será decimal y si es 1 la base será 2.
n = Número a poner en la casilla.
fila = Fila a jugar.
columna = Columna a jugar.
inst = Instruccion del menú de bienvenida.
inst1 = Variable de la fila.
inst2 = Variable de la columna.
log = Variable del archivo "jugadas.log".
posicion = Índice de la fila en la matriz inicio.
fin_fila = Número que representa la última fila a evaluar.
fin_columna = Número que representa la última columna a evaluar.
res = Acumulador del resultado.

"""


def instrucciones ():
    print ("""

Inicio

El sudoku se presenta normalmente como una tabla de 9 × 9, compuesta por subtablas de 3 × 3 denominadas "regiones" (también se le llaman "cajas" o "bloques").

Objetivo

Algunas celdas ya contienen números, conocidos como "números dados" (o a veces "pistas"). El objetivo es rellenar las celdas vacías, con un número en cada una de ellas,
de tal forma que cada columna, fila y región contenga los números 1–9 solo una vez.

Tomado de Wikipedia (http://es.wikipedia.org/wiki/Sudoku).

Modalidades

El juego puede jugarse tanto en la bases numéricas 10 o 2.

Log de jugadas

El juego automáticamente graba un archivo que contiene las jugadas reslizadas, el día y la hora exacta en la que comenzó a jugar. Este archivo se llama "jugadas.log"
y se encuentra en la carpeta donde este almacenado el juego.

Juego

- Indique la posición de la fila que desea jugar: Estas se reprentan alfabéticamente desde a A hasta la I. Ésta posición se puede indicar tanto en mayúscula como en
minúscula.
-Indique la columna en la que desea jugar: Estas se representan en números del uno hasta el nueve.
-Indique el número que desea poner en la posición seleccionada: El número no puede ser ni mayor que nueve ni menor que uno.
 * En caso de querer borrar el valor de una casilla, digite un cero cuando este posicionado en la casilla que desea borrar.

Estos pasos se repiten hasta que el tablero este completamente lleno.


""")
    return bienvenida ()


def about (): # Función que muestra la información del desarrollador. Es llamada por bienvenida.
    print ("""


                                                  (#######################/((###################(           ./#%%%%%%%#/,  .#                                  
                                                 .%%%/.....,#%%%,....,/%%%,   #%%%#          ./%%        ,#%%%*        ,(%%%%                                  
                                                 .%,       .#%%%.       .#,   /%%%#            .#      ,%%%(              ,%%.                                 
                                                 ,/        .#%%%.        **   /%%%#             ,     /%%%/                .%.                                 
                                                           .#%%%.             /%%%#                  /%%%(                  ,,                                 
                                                           .#%%%.             /%%%#          //     ,%%%%,                                                     
                                                           .#%%%.             /%%%#        ,#%/     #%%%#                                                      
                                                           .#%%%.             /%%%%#######%%%%/    .%%%%(                                                      
                                                           .#%%%.             /%%%#         .%/    .%%%%(                                                      
                                                           .#%%%.             /%%%#          */     (%%%%.                                                     
                                                           .#%%%.             /%%%#                 .%%%%/                                                     
                                                           .#%%%.             /%%%#               (. ,%%%%,                  /                                 
                                                           .#%%%.             /%%%#              %*   .%%%%/               .#.                                 
                                                           ,%%%%.             (%%%%           .(%/      *%%%%%*         .(%,                                   
                                                       .*/#%%%%%%#/*.     ,*(%%%%%%%%%%%%%%%%%%%%         ./#%%%%%%##%%%/.                                     
                                                                                                                ....                                           
                                                                                                                                                
                                                                              Autor: Jeffrey Alvarado
                                                                                   2014120210

                                                                            Encargado: Aurelio Sanabria

                                                                           Curso: Taller de programación

                                                      Software escrito completamente en el lenguaje de programación Python
                                                 por el estudiante Jeffrey Alvarado para el Instituto Tecnológico de Costa Rica.
                                                  Toda mención, uso o implementación, tanto de la totalidad del código como de
                                                   parte de este, está sujeto a cualquier tipo de norma o restricción que esta
                                                                           institución disponga sobre él.

                                    ---------------------------------------------------------------------------------------------------------

                                                                                       2014
""")
    return bienvenida()


def ganador (): # Función que se ejecuta al llenar exitosamente el tablero. La llama tab.
    print ("""

                                                            __| __|  |    _ _|   __| _ _|  _ \    \    _ \  __|   __| 
                                                            _|  _|   |      |   (      |   |  |  _ \   |  | _|  \__ \ 
                                                           _|  ___| ____| ___| \___| ___| ___/ _/  _\ ___/ ___| ____/

                                                                     has completado el tablero con éxito.
                                                            
""")


def grabar_log(fila, columna, n): # Función para grabar en el archivo "jugadas.log". La llama número.
    columna = str(columna)
    n = str (n)
    fila = letras [fila]
    log = open('jugadas.log.txt', 'a')
    log.write(fila + columna + " - " + n + "\n")
    log.close()


def crear_log(): # Función para crear el archivo "jugadas.log" con cada nueva partida. La llama bienvenida.
    log = open('jugadas.log.txt', 'w')
    log.write(strftime("%a, %d %B %Y %I:%M %z", gmtime()) + "\n\nJugadas: \n\n")
    log.close()
    return base_numerica (base)


def final (fila, columna): # Función que revisa si ya se termino o no el juego. La llama tab.
    if fila == 9:
        return True
    elif columna == 9:
        return final (fila + 1, 0)
    elif m [fila][columna] == "":
        return False
    else:
        return final (fila, columna + 1)


def restringidos(fila, columna, posicion): # Función que valida si la posición puede ser editada o no. La llama columna.
    if posicion == 30:
        return False
    elif [fila, columna] == inicio [posicion]:
        return True
    else:
        return restringidos (fila, columna, posicion + 1)


def comp_region_aux (fila, columna, fin_fila, fin_columna, n): # Función que compara el número con la región en la que se quiere poner. La llama comp_region.
    if fila == fin_fila:
        return False
    elif columna == fin_columna:
        return comp_region_aux (fila + 1, columna - 3, fin_fila, fin_columna, n)
    elif n == m [fila][columna]:
        return True
    else:
        return comp_region_aux (fila, columna + 1, fin_fila, fin_columna, n)
        

def comp_region (fila, columna, n): # Función que que decide la región con la que se va a comparar. La llama número.
    if fila < 3 and columna < 3:
        return comp_region_aux (0, 0, 3, 3, n)
    elif fila < 3 and columna < 6:
        return comp_region_aux (0, 3, 3, 6, n)
    elif fila < 3 and columna < 9:
        return comp_region_aux (0, 6, 3, 9, n)
    elif fila < 6 and columna < 3:
        return comp_region_aux (3, 0, 6, 3, n)
    elif fila < 6 and columna < 6:
        return comp_region_aux (3, 3, 6, 6, n)
    elif fila < 6 and columna < 9:
        return comp_region_aux (3, 6, 6, 9, n)
    elif fila < 9 and columna < 3:
        return comp_region_aux (6, 0, 9, 3, n)
    elif fila < 9 and columna < 6:
        return comp_region_aux (6, 3, 9, 6, n)
    else:
        return comp_region_aux (6, 6, 9, 9, n)


def comp_columna (fila, columna, n): # Función que compara el elemento con la columna en la que se quiere poner. La llama numero.
    if fila == 9:
        return False
    elif n == m[fila][columna]:
        return True
    else:
        return comp_columna (fila + 1, columna, n)


def comp_fila (fila, columna, n): # Función que compara el elemento con la fila en la que se quiere poner. La llama numero.
    if columna == 9:
        return False
    elif n == m[fila][columna]:
        return True
    else:
        return comp_fila (fila, columna + 1, n)
    

def numero (fila, columna, base): # Función que valida el número a poner en la casilla. La llama columna.
    try:
        n = int(input("\nDigite el número que desea poner en la casilla: "))
    except ValueError:
        print ("\nEsa opción no es válida, por favor digite una opción válida.")
        return numero (fila, columna, base)
    if n == 0:
        m [fila][columna] = ""
        return tab (base)
    elif n > 9 or n < 0:
        print ("\nEse número no es válido, por favor digite un número válido.")
        return numero (fila, columna, base)
    elif comp_columna (0, columna, n) == True or comp_fila (fila, 0, n) == True or comp_region (fila, columna, n) == True:
        print ("\nEsa número no puede ir en esa casilla, por favor digite otro número.")
        return numero (fila, columna, base)
    else:
        m [fila][columna] = n
        grabar_log (fila, columna + 1, n)
        return tab (base)


def columna (fila, base): # Función que valida la columna. La llama fila.
    try:
        inst2 = int(input("\nDigite el número de la columna que desea jugar: ")) - 1
    except ValueError:
        print ("\nEsa opción no es válida, por favor digite una opción válida.")
        return columna (fila, base)
    if inst2 < 0 or inst2 > 8:
        print ("\nEsa opción no es válida, por favor digite una opción válida.")
        return columna (fila, base)
    elif restringidos (fila, inst2, 0) == True:
        print ("\nEsa posición no es corregible, digite otra posición.")
        return columna (fila, base)
    else:
        return numero (fila, inst2, base)


def fila (base): # Función que valida la fila. La llama tab.
    inst1 = input("\nDigite la letra de la fila que desea jugar: ")
    if inst1 == "a" or inst1 == "A":
        inst1 = 0
        return columna (inst1, base)
    elif inst1 == "b" or inst1 == "B":
        inst1 = 1
        return columna (inst1, base)
    elif inst1 == "c" or inst1 == "C":
        inst1 = 2
        return columna (inst1, base)
    elif inst1 == "d" or inst1 == "D":
        inst1 = 3
        return columna (inst1, base)
    elif inst1 == "e" or inst1 == "E":
        inst1 = 4
        return columna (inst1, base)
    elif inst1 == "f" or inst1 == "F":
        inst1 = 5
        return columna (inst1, base)
    elif inst1 == "g" or inst1 == "G":
        inst1 = 6
        return columna (inst1, base)
    elif inst1 == "h" or inst1 == "H":
        inst1 = 7
        return columna (inst1, base)
    elif inst1 == "i" or inst1 == "I":
        inst1 = 8
        return columna (inst1, base)
    else:
        print ("\nEsa opción no es válida, por favor digite una opción válida.")
        return fila (base)

        
def tab (base): # Función que muestra el tablero. La llama numero y base_numerica.
    print("\n\t\t\t\t\t       1        2        3         4        5        6         7        8        9    ")
    print("\t\t\t\t\t  ╔══════════════════════════╗╔══════════════════════════╗╔══════════════════════════╗")
    print("\t\t\t\t\t  ║┌------┐ ┌------┐ ┌------┐║║┌------┐ ┌------┐ ┌------┐║║┌------┐ ┌------┐ ┌------┐║")
    print("\t\t\t\t\tA ║| %4s | | %4s | | %4s |║║| %4s | | %4s | | %4s |║║| %4s | | %4s | | %4s |║" %(conversion (m[0][0], base), conversion (m[0][1], base), conversion (m[0][2], base), conversion (m[0][3], base), conversion (m[0][4], base), conversion (m[0][5], base), conversion (m[0][6], base), conversion (m[0][7], base), conversion (m[0][8], base)))
    print("\t\t\t\t\t  ║└------┘ └------┘ └------┘║║└------┘ └------┘ └------┘║║└------┘ └------┘ └------┘║")
    print("\t\t\t\t\t  ║┌------┐ ┌------┐ ┌------┐║║┌------┐ ┌------┐ ┌------┐║║┌------┐ ┌------┐ ┌------┐║")
    print("\t\t\t\t\tB ║| %4s | | %4s | | %4s |║║| %4s | | %4s | | %4s |║║| %4s | | %4s | | %4s |║" %(conversion (m[1][0], base), conversion (m[1][1], base), conversion (m[1][2], base), conversion (m[1][3], base), conversion (m[1][4], base), conversion (m[1][5], base), conversion (m[1][6], base), conversion (m[1][7], base), conversion (m[1][8], base)))
    print("\t\t\t\t\t  ║└------┘ └------┘ └------┘║║└------┘ └------┘ └------┘║║└------┘ └------┘ └------┘║")
    print("\t\t\t\t\t  ║┌------┐ ┌------┐ ┌------┐║║┌------┐ ┌------┐ ┌------┐║║┌------┐ ┌------┐ ┌------┐║")
    print("\t\t\t\t\tC ║| %4s | | %4s | | %4s |║║| %4s | | %4s | | %4s |║║| %4s | | %4s | | %4s |║" %(conversion (m[2][0], base), conversion (m[2][1], base), conversion (m[2][2], base), conversion (m[2][3], base), conversion (m[2][4], base), conversion (m[2][5], base), conversion (m[2][6], base), conversion (m[2][7], base), conversion (m[2][8], base)))
    print("\t\t\t\t\t  ║└------┘ └------┘ └------┘║║└------┘ └------┘ └------┘║║└------┘ └------┘ └------┘║")
    print("\t\t\t\t\t  ╚══════════════════════════╝╚══════════════════════════╝╚══════════════════════════╝")
    print("\t\t\t\t\t  ╔══════════════════════════╗╔══════════════════════════╗╔══════════════════════════╗")
    print("\t\t\t\t\t  ║┌------┐ ┌------┐ ┌------┐║║┌------┐ ┌------┐ ┌------┐║║┌------┐ ┌------┐ ┌------┐║")
    print("\t\t\t\t\tD ║| %4s | | %4s | | %4s |║║| %4s | | %4s | | %4s |║║| %4s | | %4s | | %4s |║" %(conversion (m[3][0], base), conversion (m[3][1], base), conversion (m[3][2], base), conversion (m[3][3], base), conversion (m[3][4], base), conversion (m[3][5], base), conversion (m[3][6], base), conversion (m[3][7], base), conversion (m[3][8], base)))
    print("\t\t\t\t\t  ║└------┘ └------┘ └------┘║║└------┘ └------┘ └------┘║║└------┘ └------┘ └------┘║")
    print("\t\t\t\t\t  ║┌------┐ ┌------┐ ┌------┐║║┌------┐ ┌------┐ ┌------┐║║┌------┐ ┌------┐ ┌------┐║")
    print("\t\t\t\t\tE ║| %4s | | %4s | | %4s |║║| %4s | | %4s | | %4s |║║| %4s | | %4s | | %4s |║" %(conversion (m[4][0], base), conversion (m[4][1], base), conversion (m[4][2], base), conversion (m[4][3], base), conversion (m[4][4], base), conversion (m[4][5], base), conversion (m[4][6], base), conversion (m[4][7], base), conversion (m[4][8], base)))
    print("\t\t\t\t\t  ║└------┘ └------┘ └------┘║║└------┘ └------┘ └------┘║║└------┘ └------┘ └------┘║")
    print("\t\t\t\t\t  ║┌------┐ ┌------┐ ┌------┐║║┌------┐ ┌------┐ ┌------┐║║┌------┐ ┌------┐ ┌------┐║")
    print("\t\t\t\t\tF ║| %4s | | %4s | | %4s |║║| %4s | | %4s | | %4s |║║| %4s | | %4s | | %4s |║" %(conversion (m[5][0], base), conversion (m[5][1], base), conversion (m[5][2], base), conversion (m[5][3], base), conversion (m[5][4], base), conversion (m[5][5], base), conversion (m[5][6], base), conversion (m[5][7], base), conversion (m[5][8], base)))
    print("\t\t\t\t\t  ║└------┘ └------┘ └------┘║║└------┘ └------┘ └------┘║║└------┘ └------┘ └------┘║")
    print("\t\t\t\t\t  ╚══════════════════════════╝╚══════════════════════════╝╚══════════════════════════╝")
    print("\t\t\t\t\t  ╔══════════════════════════╗╔══════════════════════════╗╔══════════════════════════╗")
    print("\t\t\t\t\t  ║┌------┐ ┌------┐ ┌------┐║║┌------┐ ┌------┐ ┌------┐║║┌------┐ ┌------┐ ┌------┐║")
    print("\t\t\t\t\tG ║| %4s | | %4s | | %4s |║║| %4s | | %4s | | %4s |║║| %4s | | %4s | | %4s |║" %(conversion (m[6][0], base), conversion (m[6][1], base), conversion (m[6][2], base), conversion (m[6][3], base), conversion (m[6][4], base), conversion (m[6][5], base), conversion (m[6][6], base), conversion (m[6][7], base), conversion (m[6][8], base)))
    print("\t\t\t\t\t  ║└------┘ └------┘ └------┘║║└------┘ └------┘ └------┘║║└------┘ └------┘ └------┘║")
    print("\t\t\t\t\t  ║┌------┐ ┌------┐ ┌------┐║║┌------┐ ┌------┐ ┌------┐║║┌------┐ ┌------┐ ┌------┐║")
    print("\t\t\t\t\tH ║| %4s | | %4s | | %4s |║║| %4s | | %4s | | %4s |║║| %4s | | %4s | | %4s |║" %(conversion (m[7][0], base), conversion (m[7][1], base), conversion (m[7][2], base), conversion (m[7][3], base), conversion (m[7][4], base), conversion (m[7][5], base), conversion (m[7][6], base), conversion (m[7][7], base), conversion (m[7][8], base)))
    print("\t\t\t\t\t  ║└------┘ └------┘ └------┘║║└------┘ └------┘ └------┘║║└------┘ └------┘ └------┘║")
    print("\t\t\t\t\t  ║┌------┐ ┌------┐ ┌------┐║║┌------┐ ┌------┐ ┌------┐║║┌------┐ ┌------┐ ┌------┐║")
    print("\t\t\t\t\tI ║| %4s | | %4s | | %4s |║║| %4s | | %4s | | %4s |║║| %4s | | %4s | | %4s |║" %(conversion (m[8][0], base), conversion (m[8][1], base), conversion (m[8][2], base), conversion (m[8][3], base), conversion (m[8][4], base), conversion (m[8][5], base), conversion (m[8][6], base), conversion (m[8][7], base), conversion (m[8][8], base)))
    print("\t\t\t\t\t  ║└------┘ └------┘ └------┘║║└------┘ └------┘ └------┘║║└------┘ └------┘ └------┘║")
    print("\t\t\t\t\t  ╚══════════════════════════╝╚══════════════════════════╝╚══════════════════════════╝")
    if final (0, 0) == True:
        return ganador()
    else:
        return fila(base)


def binario (n, res): # Función para convertir un número a binario. La llama conversion.
    if n == "":
        return ("")
    elif n == 0:
        return res
    else:
        return binario (n // 2, str(n%2) + res)


def conversion (n, base): # Función que administra las conversiones. La llama tab.
    if base == 0:
        return n
    else:
        return binario (n , "")


def base_numerica (base): # Función que llama a las conversiones. La llama crear_log.
    print ("""
1) Decimal
2) Binario""")
    try:
        inst = int(input("\nElija el sistema numérico: "))
    except ValueError:
        print ("\nEsa opción no esta en el menú, digite una opción del menú.")
        return base_numerica(base)
    if inst == 1:
        return tab (base)
    elif inst == 2:
        base = 1
        return tab (base)
    else:
        print ("\nEsa opción no esta en el menú, digite una opción del menú.")
        return base_numerica (base)

    
def bienvenida (): # Funcion de entrada, es llamada por instrucciones, about y al inicio del programa.
    print("""
                                                                             ------------MENU------------

    			                                                           1) Partida nueva

    			                                                      2) Instrucciones del juego

    				                                               3) Sobre el desarrollador

    				                                                      4) Salir
""")
    try:
        inst = int(input("\nDigite una opción del menú: "))
    except ValueError:
        print ("\nEsa opción no esta en el menú, digite una opción del menú.")
        return bienvenida()
    if inst == 1:
        return crear_log()
    elif inst == 2:
        return instrucciones ()
    elif inst == 4:
        print ("\nMuchas gracias por jugar.")
    elif inst == 3:
        return about ()
    else:
        print ("\nEsa opción no esta en el menú, digite una opción del menú.")
        return bienvenida ()


print ("""

                                                           ▄████████ ███    █▄  ████████▄   ▄██████▄     ▄█   ▄█▄ ███    █▄  
                                                          ███    ███ ███    ███ ███   ▀███ ███    ███   ███ ▄███▀ ███    ███ 
                                                          ███    █▀  ███    ███ ███    ███ ███    ███   ███▐██▀   ███    ███ 
                                                          ███        ███    ███ ███    ███ ███    ███  ▄█████▀    ███    ███ 
                                                        ▀███████████ ███    ███ ███    ███ ███    ███ ▀▀█████▄    ███    ███ 
                                                                 ███ ███    ███ ███    ███ ███    ███   ███▐██▄   ███    ███ 
                                                           ▄█    ███ ███    ███ ███   ▄███ ███    ███   ███ ▀███▄ ███    ███ 
                                                         ▄████████▀  ████████▀  ████████▀   ▀██████▀    ███   ▀█▀ ████████▀  
                                                              ▀                    
                                                        ================ Instituto Tecnológico de Costa Rica ===============

                                                        Bienvenido a Sudoku para Python.
""")


bienvenida () # Llamada inicial.
