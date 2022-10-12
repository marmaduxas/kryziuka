
def sum(a, b, c):
    return a + b + c

def lenta(zaidejasX, zaidejasO):
    septyni = 'X' if zaidejasX[7] else ('O' if zaidejasO[7] else 7)
    astuoni = 'X' if zaidejasX[8] else ('O' if zaidejasO[8] else 8)
    devyni = 'X' if zaidejasX[9] else ('O' if zaidejasO[9] else 9)
    keturi = 'X' if zaidejasX[4] else ('O' if zaidejasO[4] else 4)
    penki = 'X' if zaidejasX[5] else ('O' if zaidejasO[5] else 5)
    sesi = 'X' if zaidejasX[6] else ('O' if zaidejasO[6] else 6)
    vienas = 'X' if zaidejasX[1] else ('O' if zaidejasO[1] else 1)
    du = 'X' if zaidejasX[2] else ('O' if zaidejasO[2] else 2)
    trys = 'X' if zaidejasX[3] else ('O' if zaidejasO[3] else 3)

    print(f"| {septyni} | {astuoni} | {devyni} |")
    print(f"|--|---|--|")
    print(f"| {keturi} | {penki} | {sesi} |")
    print(f"|--|---|--|")
    print(f"| {vienas} | {du} | {trys} |")


def laimejo_kai(zaidejasX, zaidejasO):
    wins = [[7, 8, 9], [4, 5, 6], [1, 2, 3], [1, 5, 9], [7, 5, 3], [7, 4, 1], [8, 5, 2], [9, 6, 3]]
    for win in wins:
        if (sum(zaidejasX[win[0]], zaidejasX[win[1]], zaidejasX[win[2]]) == 3):
            print("Žaidėjas X laimėjo")
            return 1
        if (sum(zaidejasO[win[0]], zaidejasO[win[1]], zaidejasO[win[2]]) == 3):
            print("Žaidėjas O laimėjo")
            return 0
    return -1


if __name__ == "__main__":
    zaidejasX = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    zaidejasO = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ejimas = 1
    print("Kryžiukai - Nuliukai")
    while (True):
        lenta(zaidejasX, zaidejasO)
        if (ejimas == 1):
            print("X' Žaidėjo ėmjimas")
            ejimas = int(input("Pasirinkite norima skaičių: "))
            zaidejasX[ejimas] = 1
        else:
            print("O' Žaidėjo ėmjimas")
            ejimas = int(input("Pasirinkite norima skaičių: "))
            zaidejasO[ejimas] = 1

        laimejotas = laimejo_kai(zaidejasX, zaidejasO)
        if (laimejotas != -1):
            print("Pabaiga")
            break

        ejimas = 1 - ejimas
