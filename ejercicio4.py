#Crear un programa de ordenador para gestionar los resultados de la quiniela de fútbol. Para ello vamos a utilizar dos listas:

#Equipos: Que es una lista cuyos elementos son una lista con el nombre de los equipos que juegan el partido. En la quiniela se indican 15 partidos. 
#Ejemplo: equipos = [[“Sevilla”,”Betis”],[“Madrid”,”Barcelona”],…]
#Resultados: Es una lista de enteros donde se indica el resultado. También tiene dos columnas (cada elemento es una lista), 
#en la primera se guarda el número de goles del equipo que está guardado en la primera columna de la tabla anterior,
#y en la segunda los goles del otro equipo. Ejemplo: resultados=[[3,0],[0,0],…]
#El programa ira pidiendo los nombres de los equipos de cada partido y el resultado del partido, a continuación se imprimirá la quiniela de esa jornada.

listaresultados=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
filas=15
columnas=2

listaequipos=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
filas1=15
columnas1=2

print("EQUIPOS")
print("-------")
print("\n\n")

print("LOS EQUIPOS VAN DE DOS EN DOS, QUIERE DECIR QUE CUANDO INTRODUCIMOS EL PRIMER EQUIPO Y EL SEGUNDO ES UNA PAREJA. CON EL RESULTADO ES LA MISMA DINAMICA")
print("\n\n")

for e in range(filas1):
    for w in range(columnas1):
        Equipo=input("Introduce los partidos:  ")
        listaequipos[e][w]=Equipo

print("RESULTADOS ESTIMADOS ")
print("--------------------")
print("\n\n")

for i in range(filas):
    for col in range(columnas):
        resultado=int(input("Resultados: "))
        listaresultados[i][col]=resultado

print("APUESTA REALIZADA")
print("-----------------")
print("\n\n")
for num,letra in zip (listaequipos,listaresultados):
    for o,c in num,letra:
        print (o,c)