# Connor also worked on this with me.
# Try playing it first without looking for the secrets that Connor and I added.
# P.S. You don't need to go specifically those places.... Try doing something, different.

place = input("You wake up. where will you go today? Vampire Lair, Siren Rock, or Ogre Cave? ")
if place == "Vampire Lair" or place == "Vampire" or place == "Lair":
    print("Alright. Pick your poison.")
    weapon1 = input("A wooden stake or 10 cloves of garlic?")
    if weapon1 == "Stake":
        print("You cook the vampire a steak. Very rare, so theres lots of blood. ")
        print()
        print("He gets bloated. You stab him with a wooden stake, and he dies. ")
        print("You Win. The End")
    elif weapon1 == "Garlic":
        print("Look, vampires may hate garlic, but they wont be killed by it. ")
        print()
        print("You die a martyr of garlic by the hands of the vampire.")
        print("You die. The End")
    else:
        print("The vampire kills you while you are fantacising about something that's not there")
        print("You Die. The End.")
elif place == "Ogre Cave" or place == "Ogre" or place == "Cave":
    print("Alright. Pick your poison")
    weapon2 = input("Steel Sword, or Magic Missle Spell? Or, just by chance, use your cousin Sylvie's ducks? ")
    if weapon2 == "Sword":
        print("You stab the left foot. He stumbles, and trips. You Impale him.")
        print()
        print("He says 'Tim' before he dies.")
        print("I wonder if he knew Tim the Enchanter. Good man Tim, good man.")
        print("You Win. The End")
    elif weapon2 ==  "Magic Missle":
        print("The Missle hits the ogre, and he explodes. Maybe you should have left the blast zone though.")
        print()
        print("The explosion also hits you.")
        print("You Die. The End")
    elif weapon2 == "Holy Hand Grenade":
        print("1")
        print("2")
        print("5")
        print("...")
        print("...")
        print("I mean 3!")
        print("You count to 5, i mean 3, and throw the grenade. The Ogre gets annhilated by the holy hand grenade.")
        print("Tim would be proud.")
        print("You Win. The End.")
    elif weapon2 == "Ducks":
        print("You grab a peice of bread and throw it at the orge and then duck for cover.")
        print()
        print("You can't see but even with your hands over your ears you still hear a big boom.")
        print("I really hope you brought a umbrella.")
        print("You walk away without looking back.")
        print("You win...")
        print("I guess...")
        print("But at what cost?")
    else:
        print("The Ogre kills you while you are fantasising about something that's not there.")
        print("You Die. The End")
elif place == "Siren Rock" or place == "Siren" or place == "Rock":
    print("Alright. Pick your poison.")
    weapon3 = input("Sledge hammer, or Harpoon? ")
    print("Remember to put wax in your ears!")
    if weapon3 == "Hammer":
        print("Ah yes. A hammer. Against psychotic mermaids.")
        print()
        print("Who thought this was a good idea?")
        print("Well, the slow weapon against the fast monster.")
        print("You Die. The end.")
    elif weapon3 == "Harpoon":
        print("Good choice. Using a harpoon against an aquatic enemy.")
        print()
        print("You throw the harpoon at the siren, piercing it.")
        print("It is very dead. You do wonder what it's song sounds like though....")
        print("You Win. The End")
    else:
        print("The Siren kill you while you are fantasising about something that's not there")
else:
    print("You can't go there.")
    print("Can you at least stop by Camelot to pick me up a shrubbery?")
    print("NEW ACHEIVMENT!!")
    print("QUEST FOR THE SHRUBBERY")
    print("You must find a shrubbery for me")
    print("Where do ya wanna look?")
    quest_place = input("Forest, or Town? ")
    if quest_place == "Forest":
        print("You stumbe into the Forest, unsure what you might find. You come across some knights.")
        print("You think they might want to help you, but all they say is 'NI'.")
        print("So you find and Ork Camp.")
        print("YOU SEE A SHRUBBERY!!!!")
        method1 = input("How do you want to do this? Make peace with them, or Steal the Shrubbery? ")
        if method1 == "Peace":
            print("Wow. Your so dumb.")
            print("Orks are savages. They fight each other so often, their speicies got dumber as a result.")
            print("Peace was never an option.")
            print("The Orks tie you to a spit over an open flame, after you've already been killed.")
            print("You Die. The End")
        if method1 == "Steal":
            print("Good thinking. Orks are very dumb. You get in, grab the shrubbery, and get out.")
            print("Wow, you actually got me a shrubbery. You've done better than Shiv...")
            print("You Win. The End.")
    if quest_place == "Town":
        print("You stroll into town, eyes out for a shrubbery.")
        print("But the monsters are mad at you. You didn't fight them!")
        print("All three monsters jump you. Siren, Vampire, and Ogre. ")
        print("What do you do?")
        method2 = input("Run Away, or Fight them? ")
        if method2 == "Run":
            print("You dash into a house, hiding from the monsters. But then you see it! A shrubbery!")
            print('You touch it. Suddenly, a horn blows from the forest.')
            print("A bunch of knights run out of he forest, attacking the monsters")
            print("'NI' they shout, as they defeat their foes. And, you got a shrubbery for me!")
            print("You Win. The End")
        if method2 == "Fight":
            print("You can beat one if your smart, but not all three.....")
            print("The Siren lures you, the ogre bonks your head, and the vampire turns you into a vampire.")
            print("You Die. The End")
    else:
        print("Look, I gave you one chance already. Don't mess this up again.")