print("1-háromszög, 2-kör, 3-téglalap, 4-nyolcszög")
szam = int(input("Kérem írja be a választott művelet számát: ")
def nyolcszogKerulet():
		a=float(input("Kérlek add meg a nyolcszög oldalát [cm]: "))
		return 8*a
def nyolcszogTerulet():
		a=float(input("Kérlek add meg a nyolcszög oldalát [cm]: "))
		r=float(input("Kérlek add meg a nyolcszög sugarát [cm]: "))
		return 4*a*r


"""
Tesztelés
print(nyolcszogTerulet())
print(nyolcszogTerulet())
"""