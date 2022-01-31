#Queremos guardar el nombre de los artículos de un almacén y sus precios. Como estructura de datos vamos a usar dos listas: artículos, donde vamos a guardar el nombre de los artículos y precios donde vamos a guardar los precios. 
# De tal forma que el artículo en la posición n de la lista artículos tendrá el precio correspondiente a la misma posición en la lista precios.

#Realiza un programa que pida por teclado artículos y sus precios (el programa pedirá cuantos artículos se van a introducir)
# , al finalizar dará la siguiente información:

    #El precio medio de los artículos.
    #El nombre de los artículos que valen más de 100 euros.
    #Nos pedirá un nombre de un artículo y si existe nos dará su precio, sino nos dará un error.


articulo=[]
precio1=[]
cantidad=int(input("Dime la cantidad de articulo que deseas introducir:  "))
for i in range(cantidad):
    nombre=input("Nombre del articulo:  ")
    precio=float(input("Precio:  "))
    articulo.append(nombre)
    precio1.append(precio)

opciones=int(input("\n\n 1. Media de los productos \n\n 2. Nombre de los articulos que valen más de 100€ \n\n 3. Nombre del articulo \n\n 4. Salir \n\n\n\n Elige una Opción:  "))
print("\n\n")
while opciones !=4:
    if opciones==1:
        l=sum(precio1)
        print("\n\n")
        print("La media de los productos es:  ",l/cantidad)
        print("\n\n")
    if opciones==2:
        for e,i in zip(articulo,precio1):
            if i >=100:
                print("\n\n")
                print("Articulos: ",e)
                print("\n\n")
        
    if opciones==3:
        nombredearticulo=input("Dime el nombre que deseas buscar en la lista:  ")
        for o,l in zip (articulo,precio1):
            if o ==nombredearticulo:
                print(l)
    opciones=int(input("\n\n 1. Media de los productos \n\n 2. Nombre de los articulos que valen más de 100€ \n\n 3. Nombre del articulo \n\n 4. Salir \n\n\n\n Elige una Opción:  "))