from random import random


# MAX_STEPEN = 3
MAX_STEPEN = 9


def baci_puno_virsli(broj_virsli):
    virsle = []
    for _ in range(broj_virsli):
        x = random()
        y = random()
        virsle.append((x, y))

    return virsle

def is_jedinicna_virsla(x, y):
    return (x**2 + y**2) <= 1

def chaos_computing(broj_virsli=10):
    count = 0
    for x, y in baci_puno_virsli(broj_virsli):
        if is_jedinicna_virsla(x, y):
            count += 1

    return count / broj_virsli * 4

def main():
    for stepen_virslosti in range(MAX_STEPEN):
        broj_virsli=10**stepen_virslosti
        virsioliki_pi = chaos_computing(broj_virsli)

        print("%10d -> %f" % (broj_virsli, virsioliki_pi))

    print('')

if __name__ == "__main__":
    main()
