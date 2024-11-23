#le code qui reset les berries et l'argent quand on lance le projet
money = 0
berries = 0

#le createur de berries
while True:
    #berries maker command prompt
    bemrcmd = input(">>>  ")

    #.=berries
    if bemrcmd == ".":
        berries += 1

    elif bemrcmd == "help":
        print("Help: toutes le comandes")
        print(".: La commande '.' te donne une berries")
        print("sell: Sa vas le nombre de berries que tu met apres sell (si tu as pas asser de berries, sa ne fonctioneras pas")

    elif bemrcmd.startswith("sell"):
        try:
            amount =int(bemrcmd.split()[1])
            if amount <= berries:
                berries -= amount
                money += amount
                print(f"Money: {money}, Berries: {berries}")

            else:
                print("pas asser de berries")

        except (IndexError, ValueError):
            print("Commande invalide: Utiliser 'sell'<nombre> pour vendre vos berries")

    elif bemrcmd == "exit":
        print(f"Vous avez eu {money} money et {berries} berries")
        break