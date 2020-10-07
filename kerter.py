print("1-háromszög, 2-kör, 3-téglalap, 4-nyolcszög")
szam = int(input("Kérem írja be a választott művelet számát: ")

	haromszogKerulet ():
	a=float(input("Kérem a háromszög egyik odlalát[cm]: "))
	b=float(input("Kérem a háromszög másik oldalát[cm]: "))
	c=float(input("Kérem a háromszög harmadik oldalát[cm]: "))
	return float(a+b+c)
	print(teglalapTerulet())


def nyolcszogKerulet():
		a=float(input("Kérlek add meg a nyolcszög oldalát [cm]: "))
		return 8*a
def nyolcszogTerulet():
		a=float(input("Kérlek add meg a nyolcszög oldalát [cm]: "))
		r=float(input("Kérlek add meg a nyolcszög sugarát [cm]: "))
		return 4*a*r

def haromszogKerulet ():
	a=float(input("Kérem a háromszög egyik odlalát[cm]: "))
	b=float(input("Kérem a háromszög másik oldalát[cm]: "))
	c=float(input("Kérem a háromszög harmadik oldalát[cm]: "))
	return float(a+b+c)
	print(teglalapTerulet())
"""
Tesztelés
print(nyolcszogTerulet())
print(nyolcszogTerulet())
"""

 
print("Mennyi a kör sugara?")
sugar = float(input())
 
print("Kerület =", 2 * sugar * math.pi)
print("Terület =", sugar**2 * math.pi)