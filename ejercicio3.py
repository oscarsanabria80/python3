#Queremos hacer un programa que trabaje con las notas de los alumnos de una clase:

    #El programa pedirá cuantos alumnos tiene la clase.
    #A continuación, pedirá el nombre del alumno, y cuantas notas tiene ese alumno.
    #Se pedirán las notas del alumno introducido (cada alumno puede tener una cantidad de notas distintas). 
    # Las notas se validarán para que sea un número del 1 al 10).

#Piensa en el estructura de datos donde vas a guardar la información. Al finalizar el programa nos mostrará el siguiente menu:

    #Notas medias: Nos muestra una lista de alumnos y su nota media. Si su nota media es aprobado aparecerá la palabra “APROBADO” en la línea del alumno.
    #Buscar por nombre: Nos pide una cadena y nos muestra todos los alumnos que **comienzan por dicha cadena y la lista de sus notas.
    #Añadir alumno: No pide el nombre de un alumno, cuántas notas tienes y pide las notas.
    #Eliminar alumno: Nos pide un nombre y elimina el primer alumno que encuentre con ese nombre.
    #Salir

alumnos = []
notas=[]
cantidad = int(input("Introduce la cantidad de alumnos que vamos a guardar:"))
for num in range(cantidad):
    alumno = input("Nombre del alumno:")

    while alumno in alumnos:
        print("Alumno ya existe.")
        alumno = input("Nombre del alumno:")

    nota = float(input("Dame una nota del alumno (NUMERO -1 PARA TERMINAR DEE INTRODUCIR NOTAS):"))
    while nota > 10:
        print ("INTRODUCE UN VALOR DEL 1 AL 10")
        nota = float(input("Dame una nota del alumno (NUMERO -1 PARA TERMINAR DEE INTRODUCIR NOTAS):"))
    while nota !=-1:
        notas.append(nota)
        nota = float(input("Dame una nota del alumno (NUMERO -1 PARA TERMINAR DEE INTRODUCIR NOTAS):"))
        alumnos.append(alumno)

        while nota > 10:
            print ("INTRODUCE UN VALOR DEL 1 AL 10")
            nota = float(input("Dame una nota del alumno (NUMERO -1 PARA TERMINAR DEE INTRODUCIR NOTAS):"))

opciones=int(input("ELIGE UNA OPCION:\n\n 1. Notas Medias\n\n 2. Buscar Por Nombres\n\n 3. Añadir alumnos\n\n 4. Eliminar alumnos\n\n 5. Salir\n\n Introduce tu opcion aqui:  "))

while opciones !=5:

    if opciones ==1:
        for r, s in zip(alumnos,notas):
            print(r,sum(notas)/len(notas))
    if opciones ==2:
        cadena=input("Introduzca una cadena:  ")
        for s,p in zip(alumnos,notas):
            if s == cadena:
                print(s,p)
    if opciones ==3:
        cantidad = int(input("Introduce la cantidad de alumnos que vamos a guardar:"))
        for num in range(cantidad):
            alumno = input("Nombre del alumno:")

            while alumno in alumnos:
                print("Alumno ya existe.")
                alumno = input("Nombre del alumno:")

            nota = float(input("Dame una nota del alumno (NUMERO -1 PARA TERMINAR DEE INTRODUCIR NOTAS):"))
            while nota > 10:
                print ("INTRODUCE UN VALOR DEL 1 AL 10")
                nota = float(input("Dame una nota del alumno (NUMERO -1 PARA TERMINAR DEE INTRODUCIR NOTAS):"))
            while nota !=-1:
                notas.append(nota)
                nota = float(input("Dame una nota del alumno (NUMERO -1 PARA TERMINAR DEE INTRODUCIR NOTAS):"))
                alumnos.append(alumno)

            while nota > 10:
                print ("INTRODUCE UN VALOR DEL 1 AL 10")
                nota = float(input("Dame una nota del alumno (NUMERO -1 PARA TERMINAR DEE INTRODUCIR NOTAS):"))
    if opciones==4:
            nombre=input("Nombre Del Alumno:  ")

            for l in alumnos:
                if nombre ==l:
                    alumnos.remove(l)
                    print(alumnos)
                
    opciones=int(input("ELIGE UNA OPCION:\n\n 1. Notas Medias\n\n 2. Buscar Por Nombres\n\n 3. Añadir alumnos\n\n 4. Eliminar alumnos\n\n 5. Salir\n\n Introduce tu opcion aqui:  "))
