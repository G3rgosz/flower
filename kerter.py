print("1-háromszög, 2-kör, 3-téglalap, 4-nyolcszög")
szam = int(input("Kérem írja be a választott művelet számát: ")
if (szam = 4):
	def nyolcszogKerulet():
		a=float(input("Kérlek add meg a nyolcszög oldalát [cm]: "))
		return 8*a
	def nyolcszogTerulet():
		a=float(input("Kérlek add meg a nyolcszög oldalát [cm]: "))
		r=float(input("Kérlek add meg a nyolcszög sugarát [cm]: "))
		return 4*a*r
	print(nyolcszogKerulet())
	print(nyolcszogTerulet())
if else (szam = 2):
	print("Mennyi a kör sugara?")
	sugar = float(input())

	print("Kerület =", 2 * sugar * 3.14,"cm")
	print("Terület =", sugar**2 * 3.14,"cm^2")
if else (szam = 1):
	def haromszogKerulet ():
		a=float(input("Kérem a háromszög egyik odlalát[cm]: "))
		b=float(input("Kérem a háromszög másik oldalát[cm]: "))


		c=float(input("Kérem a háromszög harmadik oldalát[cm]: "))
		return float(a+b+c)
	print(teglalapTerulet())
else:
	print(nincs ilyen lehetőség)

"""
Tesztelés
print(nyolcszogTerulet())
print(nyolcszogTerulet())
"""

 