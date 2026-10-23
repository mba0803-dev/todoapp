tasks = []

while True:
    print("\n===== MENU =====")
    print("1. Ajouter une tâche")
    print("2. Voir les tâches")
    print("3. Supprimer une tâche")
    print("4. Quitter")

    choice = input("Choix : ")

    if choice == "1":
        task = input("Nouvelle tâche : ")
        tasks.append(task)
        print("Felicitation ,vous avez ajouter la tache.")

    elif choice == "2":
        if len(tasks) == 0:
            print("Aucune tâche.")
        else:
            print("\nListe des tâches :")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if len(tasks) == 0:
            print("Aucune tâche à supprimer.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            number = int(input("Numéro à supprimer : "))
            if 1 <= number <= len(tasks):
                tasks.pop(number - 1)
                print("Tâche supprimée.")
            else:
                print("Numéro invalide.")

    elif choice == "4":
        print("Au revoir.")
        break

    else:
        print("Choix invalide.")