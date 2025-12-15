def CC15():
    print("AniWantchlist")

    anime = []
    reyal = True

    while reyal == True:
        wl = input("Enter the Anime you want to watch: ")
        print("Anime has been added to your Watch List.")
        print("Type exit when finished.")
        anime.append(wl)
        if wl == "exit":
            print("Your listing is finish, exiting!")
            anime.pop()
            break

    print(f"Here is the Summation List of your Anime: ")
    for walist in anime:
        print(f"- {walist}")
