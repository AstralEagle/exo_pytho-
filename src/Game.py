import random

class PierrePapierCiseau:
    def __init__(self):
        print("Vous avez choisi le Pierre Papier Ciseau")

    def game(self):
        choise = 0
        choises = ["Pierre","Papier", "Ciseau"]
        while True:
            print("")
            for i, choix in enumerate(choises):
                print(f"{i+1} - {choix}")
            choise = int(input("Choisir un geste"))
            print("")
            if choise >0 and choise < 4:
                ai_select = random.randint(1, 3)
                print(f"Vous : {choises[choise-1]}")
                print(f"Adversaire : {choises[ai_select-1]}")
                if (ai_select == 1 and choise == 2) or (ai_select == 2 and choise == 3) or  (ai_select == 3 and choise == 1):
                    print("Vous avez gagner")
                    break
                elif (choise == 1 and ai_select == 2) or (choise == 2 and ai_select == 3) or  (choise == 3 and ai_select == 1):
                    print("Vous avez perdu")
                    break
                else:
                    print("Egalité")
class AuPlusPres:

    nbr_max = 50

    def __init__(self):
        print("Vous avez choisi le Au Plus Près!")
        self.coup = 10
        self.nbr = random.randint(1, AuPlusPres.nbr_max)

    def game(self):
        while True:
            if self.coup > 0:
                print("")
                print(f"Il vous reste {self.coup} coups")
                choise = int(input("Choisir un nombre : "))
                print("")

                if choise == self.nbr:
                    print("Vous avez trouver le bon nombre")
                    break
                elif choise > self.nbr:
                    print("Le chiffre est plus petit")
                elif choise < self.nbr:
                    print("Le chiffre est plus grand")
                self.coup -= 1
            else:
                print("Vous avez perdu")
                break

class Blackjack:
    def __init__(self):
        print("Vous avez choisi le Blackjack")
        self.nbrPlayer = 0
        self.nbrBot = 0
        self.playerStay = False
        self.botStay = False


    def game(self):
        newCarte = self.get_carte()
        self.nbrPlayer += newCarte
        print(f"Vous piochez une carte: {newCarte}")
        newCarte = self.get_carte()
        self.nbrBot += newCarte
        print(f"Votre adversaire aussi: {newCarte}")
        newCarte = self.get_carte()
        self.nbrPlayer += newCarte
        print(f"Vous piochez une carte: {newCarte}, vous etes a {self.nbrPlayer}")
        newCarte = self.get_carte()
        self.nbrBot += newCarte
        print(f"Votre adversaire aussi: {newCarte}, il est a {self.nbrBot}")

        while True:
            if self.playerStay == False:
                while True:
                    print("Voulez-vous piochez une carte?")
                    choice = int(input("1 - Oui / 2 - Non"))
                    if choice == 1:
                        newCarte = self.get_carte()
                        self.nbrPlayer += newCarte
                        print(f"Vous piochez une carte: {newCarte}, vous etes a {self.nbrPlayer}")
                        break
                    elif choice == 2:
                        self.playerStay = True
                        break
                if self.nbrPlayer > 21:
                    print("Vous avez perdu")
                    break
            if self.botStay == False:
                if self.nbrBot < 17 and self.nbrBot < self.nbrPlayer:
                    newCarte = self.get_carte()
                    self.nbrBot += newCarte
                    print(f"Votre adversaire pioche une carte: {newCarte}, il est a {self.nbrBot}")
                    if self.nbrBot > 21:
                        print("Vous avez gagner")
                        break
                else:
                    self.botStay = True

            if self.playerStay and self.botStay:
                if self.nbrBot == self.nbrPlayer:
                    print("Egaliter")
                else:
                    print(("Vous avez gagner", "Vous avez perdu")[self.nbrPlayer < self.nbrBot])
                break


    def get_carte(self):
        return random.randint(2, 11)