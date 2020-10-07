print("1-háromszög, 2-kör, 3-téglalap, 4-nyolcszög")
szam = int(input("Kérem írja be a választott művelet számát: ")

	def haromszogKerulet ():
	a=float(input("Kérem a háromszög egyik odlalát[cm]: "))
	b=float(input("Kérem a háromszög másik oldalát[cm]: "))
	c=float(input("Kérem a háromszög harmadik oldalát[cm]: "))
	return float(a+b+c)
	print(haromszogKerulet())


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


def korkerulet():
    a=int(input("számot: "))
    return a*2*3,14
