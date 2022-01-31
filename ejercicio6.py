from crypt import crypt

f = open ("/home/oscarsanabria/Escritorio/Lenguaje\ de\ Marca/entrega\ 9\ de\ enero\ /passwd.txt")
lineas = f.readlines()
f.close

lista = []
for linea in lineas:
    lista.append(linea.split(":"))

f = open ("/home/oscarsanabria/Escritorio/Lenguaje\ de\ Marca/entrega\ 9\ de\ enero\ /contraseña.txt")
contras = f.read().splitlines()
f.close

contrabuena = "no en el archivo"
print(contras)
encontrado = False
nombre = input("Nombre: ")
for usuario in lista:
    if nombre == usuario[0]:
        encontrado = True
        contraReal = usuario[1]
        sal=usuario[1][:30]
        for contra in contras:
            if crypt(contra,sal) == contraReal:
                print("correcto")
                contrabuena = contra

print(contrabuena)
if not encontrado:
    print("el usuario no existe")