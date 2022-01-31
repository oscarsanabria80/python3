articulo=[]

c=int(input("Cantidad de productos: "))
for i in range(0,c):
    n=input("nombre: ")
    p=float(input("precio: "))
    lista2=[]
    lista2.append(n)
    lista2.append(p)
    articulo.append(lista2)
    
    



opciones=int(input("\n\n 1. Media de los productos \n\n 2. Nombre de los articulos que valen más de 100€ \n\n 3. Nombre del articulo \n\n 4. Salir \n\n\n\n Elige una Opción:  "))
print("\n\n")
while opciones !=4:
    if opciones==1:
        for suma in articulo:
              if suma[1]<=0:
                  sum(suma)
                  print("La media de los productos es:  ", sum/c)  
    if opciones==2:
        for elemento in articulo:
            if elemento[1]>=100:

                print(elemento[0])
    if opciones==3:
        nom=input("Nombre del producto:  ")
        for producto in articulo:
            if producto[0]==nom:
                print(producto[1])
            else:
                print("ERROR")


    opciones=int(input("\n\n 1. Media de los productos \n\n 2. Nombre de los articulos que valen más de 100€ \n\n 3. Nombre del articulo \n\n 4. Salir \n\n\n\n Elige una Opción:  "))