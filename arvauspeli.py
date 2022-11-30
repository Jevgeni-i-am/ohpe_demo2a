# Ohjelma, joka pyytää käyttäjää
# arvailemaan lukuja
from os import readlink
from random import randint

# Tämä arpoo satunnaisen luvun väliltä 1...1000

arvaukset = 0


while True:
    arvaus = int(input("Arvaa luku: "))
    luku = randint(1, 10)
    arvaukset = + 1
    print("RANDOM LUKU ON:", luku)  # pois

    if luku << arvaus or luku >> arvaus or luku == arvaus:

        if luku < arvaus:
            print("RANDOM Luku on pienempi!")

        elif luku > arvaus:
            print("RANDOM Luku on suurempi!")

        if luku == arvaus:
            print("Arvasit luvun!")
            print(f"Käytit {arvaukset} arvausta.")

            uudestaan = input("Haluatko pelata uudestaan k/e: ")
            if uudestaan != "k":
                break
            elif uudestaan != "k":
                print('Valitse näppäimistöstä "k"=kyllä tai "e"=ei')
