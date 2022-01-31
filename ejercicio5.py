f=open ("passwd.txt")
lineas=f.readlines()
f.close()

lista=[]
for linea in lineas:
    lista.append(linea.split(":"))

print(lista)

nombre=input ("Dime el Nombre:  ")
encontrado=False
for usuario in lista:
    if nombre==usuario[0]:
        Encontrado=True
        sal=usuario[1][:30]
        passwd=input("Contraseña: ")
        print(usuario[1])
        print(sal)
    if not encontrado:
        print("Usuario no existe")