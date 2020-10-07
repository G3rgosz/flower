def nyolcszogKerulet():
		a=float(input("Kérlek add meg a nyolcszög oldalát [cm]: "))
		return 8*a
def nyolcszogTerulet():
		a=float(input("Kérlek add meg a nyolcszög oldalát [cm]: "))
		r=float(input("Kérlek add meg a nyolcszög sugarát [cm]: "))
		return 4*a*r


print("1-háromszög, 2-kör, 3-téglalap, 4-nyolcszág")

"""
Tesztelés
print(nyolcszogTerulet())
print(nyolcszogTerulet())
"""


def korkerulet():
    a=int(input("számot: "))
    return a*2*3,14
