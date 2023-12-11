from Game import Blackjack, PierrePapierCiseau, AuPlusPres

print("Hello et bienvenue dans le casino de monsieur Python")

games = ["1 - Blackjack", "2 - Au plus près", "3 - Pierre Papier Ciseau"]

def launchGame(id):
    print("")
    print("")
    print("")
    match id:
        case 1:
            game = Blackjack()
            game.game()
        case 2:
            game = AuPlusPres()
            game.game()
        case 3:
            game = PierrePapierCiseau()
            game.game()
    print("")
    print("")
    print("")


while True:
    print("Choississez votre jeux")
    for game in games:
        print(game)

    select_game = int(input(""))
    launchGame(select_game)



