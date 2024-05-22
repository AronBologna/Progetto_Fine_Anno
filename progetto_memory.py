import random
import os

def crea_griglia(righe=4, colonne=4):
    simboli = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:righe * colonne // 2]) * 2
    random.shuffle(simboli)
    return [simboli[i:i+colonne] for i in range(0, righe * colonne, colonne)]

def mostra_griglia(griglia, scoperte):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("   ", end="")
    for i in range(len(griglia[0])):
        print(f"{i+1} ", end="") 
    print()
    for i, riga in enumerate(griglia):
        print(f"{i+1} |", end="") 
        for j, simbolo in enumerate(riga):
            print(simbolo if scoperte[i][j] else "X", end=" |")
        print()
        print("  ", end="")
        for _ in range(len(griglia[0])):
            print("---", end="") 
        print()

def ottieni_mossa(righe, colonne):
    while True:
        try:
            print("prima carta (riga colonna): ", end="")
            riga1, colonna1 = map(int, input().split())
            print("seconda carta (riga colonna): ", end="")
            riga2, colonna2 = map(int, input().split())

            if (1 <= riga1 <= righe and 1 <= colonna1 <= colonne and
                1 <= riga2 <= righe and 1 <= colonna2 <= colonne and
                (riga1, colonna1) != (riga2, colonna2)):
                return riga1 - 1, colonna1 - 1, riga2 - 1, colonna2 - 1
            else:
                print("mossa non valida, assicurati che le coordinate siano entro i limiti della griglia e che le carte scelte siano diverse")
        except ValueError:
            print("mossa non valida, inserisci due numeri separati da uno spazio")

def gioca():
    righe, colonne = 4, 4
    griglia = crea_griglia()
    scoperte = [[False for _ in range(colonne)] for _ in range(righe)]
    tentativi = 0
    coppie_trovate = 0

    while coppie_trovate < righe * colonne // 2:
        mostra_griglia(griglia, scoperte)
        riga1, colonna1, riga2, colonna2 = ottieni_mossa(righe, colonne)

        scoperte[riga1][colonna1] = scoperte[riga2][colonna2] = True
        mostra_griglia(griglia, scoperte)
        tentativi += 1

        if griglia[riga1][colonna1] == griglia[riga2][colonna2]:
            coppie_trovate += 1
            print("Coppia trovata!")
        else:
            scoperte[riga1][colonna1] = scoperte[riga2][colonna2] = False
            print("carte diverse, premi invio per continuare")
            input()

    print(f"hai vinto in {tentativi} tentativi")

if __name__ == "__main__":
    gioca()
