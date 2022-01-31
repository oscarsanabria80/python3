dinero=[50000,20000,10000,5000,2000,1000,500,200,100,50,20,10,5,2,1]
total=float(input("Cantidad total: "))
entregada=float(input("Cantidad entregada: "))

devolver1=(entregada-total)
devolver=round((entregada-total)*100)

print ("Cantidad a devolver:", devolver1, "€")


if devolver/dinero[0]>=1:
	print ("%d Billete de 500 euros" % (devolver/dinero[0]))
	devolver=devolver%dinero[0]
if devolver/dinero[1]>=1:
	print ("%d Billete de 200 euros" % (devolver/dinero[1]))
	devolver=devolver%dinero[1]
if devolver/dinero[2]>=1:
	print ("%d Billete de 100 euros" % (devolver/dinero[2]))
	devolver=devolver%dinero[2]
if devolver/dinero[3]>=1:
	print ("%d Billete de 50 euros" % (devolver/dinero[3]))
	devolver=devolver%dinero[3]
if devolver/dinero[4]>=1:
	print ("%d Billete de 20 euros" % (devolver/dinero[4]))
	devolver=devolver%dinero[4]
if devolver/dinero[5]>=1:
	print ("%d Billete de 10 euros" % (devolver/dinero[5]))
	devolver=devolver%dinero[5]
if devolver/dinero[6]>=1:
	print ("%d Billete de 5 euros" % (devolver/dinero[6]))
	devolver=devolver%dinero[6]
if devolver/dinero[7]>=1:
	print ("%d moneda de 2 euros" % (devolver/dinero[7]))
	devolver=devolver%dinero[7]
if devolver/dinero[8]>=1:
	print ("%d moneda de 1 euro" % (devolver/dinero[8]))
	devolver=devolver%dinero[8]
if devolver/dinero[9]>=1:
	print ("%d moneda de 50 centimos" % (devolver/dinero[9]))
	devolver=devolver%dinero[9]
if devolver/dinero[10]>=1:
	print ("%d moneda de 20 centimos" % (devolver/dinero[10]))
	devolver=devolver%dinero[10]
if devolver/dinero[11]>=1:
	print ("%d moneda de 10 centimos" % (devolver/dinero[11]))
	devolver=devolver%dinero[11]
if devolver/dinero[12]>=1:
	print ("%d moneda de 5 centimos" % (devolver/dinero[12]))
	devolver=devolver%dinero[12]
if devolver/dinero[13]>=1:
	print ("%d moneda de 2 centimos" % (devolver/dinero[13]))
	devolver=devolver%dinero[13]
if devolver/dinero[14]>=1:
	print ("%d moneda de 1 centimo" % (devolver/dinero[14]))
	cdevolver=devolver%dinero[14]