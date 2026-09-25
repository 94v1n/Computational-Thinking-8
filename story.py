place = input("You wake up. where will you go today? Vampire Lair, or Ogre Cave? ")
if place == "Vampire Lair":
    print("Alright. Pick your poison.")
    weapon1 = input("A wooden stake or 10 cloves of garlic?")
    if weapon1 == "stake":
        print("You cook the vampire a steak. Very rare, so theres lots of blood. ")
        print()
        print("He gets bloated. You stab him with a wooden stake, and he dies. ")
        print("The End")
    if weapon1 == "garlic":
        print("Look, vampires may hate garlic, but they wont be killed by it. ")
        print()
        print("You die a martyr of garlic by the hands of the vampire.")
        print("The End")
    else:
        print("The vampire kills you while you are fantacising about something that's not there")
if place == "Ogre Cave":
    print("Alright. Pick your poison")
    weapon2 = input("Steel Sword, or Magic Missle Spell? ")
    if weapon2 == "sword":
        print("You stab the left foot. He stumbles, and trips. You Impale him.")
        print()
        print("He says 'Kevin' before he dies.")
        print("The end")