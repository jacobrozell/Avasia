from Avasia.Room.Room import *
from Avasia.Logic.util import *
from Avasia.Logic.config import *
from Avasia.Enemy.EnemyClass import Enemy
from Avasia.Combat.CombatLogic import combat


def courtyard_logic():
    courtyard.print_name()
    print("You make your way to the Cataractan Legion's courtyard to begin your training.")
    print("A large group of people are standing around three men who seem to be giving a speech.")
    print()
    print("One of the men speaks out in a loud booming voice.")
    print()
    talk("Greetings, men and women, welcome.")
    talk("My name is Cellious, I am the leader of the Pridestalkers, commonly known as the hunters.")
    talk("You are all here because Cataracta needs an army.")
    talk("I'm sure word has gotten around.")
    talk("A group of former Agromanians have fled Krothgar and turned against their people for the greater good.")
    talk("They set aside their differences and they warned the people of Aylova.")
    talk("Vashirr, the former King of Nacastrum, is forming an army of magic-wielding warriors.")
    talk("Most of you know how to defend yourselves and have no problem fighting the beasts that threaten us daily.")
    talk("But these marauders are unlike anything we've ever seen.")
    talk("Enough talk, it is time we hone your skills to fight when the time comes.")
    print()
    talk("We will begin training based of what your speciality is.")
    talk("I need Hunters with me; Scouts with Dentros; Guardians with Acustos.")
    talk("You know who you are.")
    print()
    x = 1
    while x == 1:
        hunter = ["HUNTER"]
        scout = ["SCOUT"]
        guardian = ["GUARDIAN"]
        user_class = input("What class are you?") #we should have a explanation as to what class is what and stuff here.
        user_class = user_class.upper()

        if containsAny(user_class, hunter):
            config.player.setAtk(20)
            config.player.setDef(5)
            config.player.setSpeed(10)
            config.player.setHp(65)
            config.player.setClass("hunter")
            break

        elif containsAny(user_class, scout):
            config.player.setAtk(15)
            config.player.setDef(10)
            config.player.setSpeed(20)
            config.player.setHp(50)
            config.player.setClass("scout")
            break

        elif containsAny(user_class, guardian):
            config.player.setAtk(15)
            config.player.setDef(15)
            config.player.setSpeed(5)
            config.player.setHp(100)
            config.player.setClass("guardian")
            break

        else:
            print()

    while True:

        # Tutorial
        # ---------------------------------------

        if config.player.getClass() == "hunter":  # wolf
            print()
            print(">>>Hunter Training<<<")
            print()
            print()
            talk("My name is Cellious.")
            talk("I will be teaching you all about combat and attacks special to our class.")
            print()
            talk("First begin by going into your wolf form.")
            print()
            while True:
                ans = input("Type 'wolf form' to turn into a wolf.")
                print()
                w = ["WOLF FORM", "SHAPESHIFT", "WOLF"]
                if containsAny(ans, w):
                    print("You feel the blood pumping throughout your body.")
                    print("Every cell is your body is awaiting your command.")
                    print("As you cast Wolf Form, they listen.")
                    print("Your blood runs hot and magic energy courses through every fiber of your being.")
                    print("You, as with all the others in your group, are now wolves.")
                    print()
                    break
                else:
                    print("Harness your power and try again!")
                    print()
            talk("Look around at your fellow hunters.")
            talk("Notice all of you have different markings or fangs.")
            talk("Your marking is unique only to you, much like a fingerprint.")
            talk("Though we all appear slightly different, we will fight as brothers and sisters of Cataracta.")
            print()
            talk("We will start with a simple attack called 'strike'.")
            talk("Slash will do your attack stat on the target.")
            talk("Keep in mind some enemies have a defense stat that will soften the blow of your attack.")
            talk("Try this attack out on this training dummy.")
            print()
            training_dummy = Enemy(atk=0,
                                   defense=5,
                                   spd=0,
                                   hp=50,
                                   name="Training Dummy")

            print("A " + training_dummy.name + " appears!")

            while training_dummy.hp > 0:
                print()
                training_dummy.display_stats()
                config.player.display_stats()
                attacks = ["STRIKE"]
                print()
                print("Which attack do you want to use?")
                ans = input(str(attacks))
                print()
                ans.upper()
                slash = ["STRIKE"]
                if containsAny(ans, slash):
                    training_dummy.take_hit(config.player.getAtk())
                    print("You use strike!")
                    print("The " + training_dummy.name + " took " + str(config.player.getAtk()) + " damage!")
                    print("The " + training_dummy.name + "'s defense softened the blow by " + str(training_dummy.defense) +"!")
                    print(training_dummy.name + " has " + str(training_dummy.hp) + " left!")
                    print()
                if training_dummy.hp <= 0:
                    break

            print("You killed " + training_dummy.name + "!")
            print()
            talk("Nicely done!")
            talk("As you can see 'strike' just simply does your attack stat on the target.")
            talk("Not all attacks are this simple.")
            talk("Take 'pounce' for example.")
            talk("This attack hits the target for a reduced attack but lowers the enemies defense.")
            talk("Let's try it out.")
            print()

            td = Enemy(atk=0,
                       defense=5,
                       spd=0,
                       hp=50,
                       name="Training Dummy")

            print("A " + td.name + " appears!")
            while td.hp > 0:
                print()
                td.display_stats()
                config.player.display_stats()
                attacks = ["POUNCE"]
                print()
                print("Which attack do you want to use?")
                ans = input(str(attacks))
                print()
                ans.upper()
                pounce = ["POUNCE"]
                if containsAny(ans, pounce):
                    new_atk = config.player.getAtk() - 5
                    print("You use pounce!")
                    if td.defense > 0:
                        td.defense -= 5
                        print(td.name + " had his defense lowered to " + str(td.defense) + "!")
                    elif td.defense == 0:
                        print(td.name + " can't have his defense lowered anymore!")

                    td.take_hit(config.player.getAtk() - 5)
                    print("The " + td.name + " took " + str(new_atk) + " damage!")
                    print(td.name + " has " + str(td.hp) + " left!")
                    print()

            # Add attacks to Attacks[]
            config.player.add_attack("strike")
            config.player.add_attack("pounce")
            print()
            print("You learned 'STRIKE and 'POUNCE'!")
            print("'STRIKE' and 'POUNCE' were added to your attacks!")
            print()
            talk("Great job!")
            talk("Remember, you can only have up to 4 attacks registered at one time.")
            print()
            print()
            talk("Well, next we are going to...")
            print()
            break

        if config.player.getClass() == "scout":  # fox
            print()
            print(">>>Scout Training<<<")
            print()
            print()
            talk("My name is Dentros.")
            talk("I will be teaching you all about combat and attacks special to our class.")
            print()
            talk("Let's begin by turning into our fox forms.")
            print()
            while True:
                ans = input("Type 'fox form' to turn into a fox.")
                print()
                w = ["FOX FORM", "SHAPESHIFT", "FOX"]
                if containsAny(ans, w):
                    print("You feel the blood pumping throughout your body.")
                    print("Every cell is your body is awaiting your command.")
                    print("As you cast Fox Form, they listen.")
                    print("Your blood runs hot and magic energy courses through every fiber of your being.")
                    print("You, as with all the others in your group, are now foxes.")
                    print()
                    break
                else:
                    print("Harness your power and try again!")
                    print()
            talk("Look around at your fellow scouts.")
            talk("Notice all of you have different markings.")
            talk("Your marking is unique only to you, much like a fingerprint.")
            talk("Though we all appear slightly different, we will fight as brothers and sisters of Cataracta.")
            print()
            talk("We will start with a simple attack called 'slash'.")
            talk("Strike will do your attack stat on the target.")
            talk("Keep in mind some enemies have a defense stat that will soften the blow of your attack.")
            talk("Try this attack out on this training dummy.")
            print()
            training_dummy = Enemy(atk=0,
                                   defense=5,
                                   spd=0,
                                   hp=50,
                                   name="Training Dummy")
            print("A " + training_dummy.name + " appears!")
            print("The training dummy has " + str(training_dummy.hp) + " health and " + str(
                training_dummy.defense) + " defense!")
            while training_dummy.hp > 0:
                print()
                training_dummy.display_stats()
                config.player.display_stats()
                print()
                attacks = ["SLASH"]
                print("Which attack do you want to use?")
                ans = input(str(attacks))
                print()
                ans.upper()
                strike = ["SLASH"]
                if containsAny(ans, strike):
                    training_dummy.take_hit(config.player.getAtk())
                    print("You use slash!")
                    print("The " + training_dummy.name + " took " + str(config.player.getAtk()) + " damage!")
                    print("The " + training_dummy.name + "'s defense softened the blow by " + str(training_dummy.defense) +"!")
                    print(training_dummy.name + " has " + str(training_dummy.hp) + " left!")
                    print()
                if training_dummy.hp <= 0:
                    break

            print("You killed " + training_dummy.name + "!")
            print()
            talk("Nicely done!")
            talk("As you can see 'slash' just simply does your attack stat on the target.")
            talk("Not all attacks are this simple.")
            talk("Take 'claw' for example.")
            talk("This attack hits the target for a reduced attack but lowers the enemies defense.")
            talk("Let's try it out.")
            print()

            td = Enemy(atk=0,
                       defense=5,
                       spd=0,
                       hp=50,
                       name="Training Dummy")

            print("A " + td.name + " appears!")
            print("The training dummy has " + str(td.hp)
                    + " health and " + str(td.defense) + " defense!")
            while td.hp > 0:
                print()
                td.display_stats()
                config.player.display_stats()
                print()
                attacks = ["CLAW"]
                print("Which attack do you want to use?")
                ans = input(str(attacks))
                print()
                ans.upper()
                pounce = ["CLAW"]
                if containsAny(ans, pounce):
                    new_atk = config.player.getAtk() - 5
                    print("You use claw!")
                    if td.defense > 0:
                        td.defense -= 5
                        print(td.name + " had his defense lowered to " + str(td.defense) + "!")
                    elif td.defense == 0:
                        print(td.name + " can't have his defense lowered anymore!")

                    td.take_hit(config.player.getAtk() - 5)
                    print("The " + td.name + " took " + str(new_atk) + " damage!")
                    print()

            # Add attacks to Attacks[]
            config.player.add_attack("slash")
            config.player.add_attack("claw")
            print()
            print("You learned 'SLASH' and 'CLAW'!")
            print("'SLASH' and 'CLAW' were added to your attacks!")
            print()
            talk("Great job!")
            talk("Remember, you can only have up to 4 attacks registered at one time.")
            print()
            print()
            talk("Well, next we are going to...")
            print()
            break

        if config.player.getClass() == "guardian":  # bear
            print()
            print(">>>Guardian Training<<<")
            print()
            print()
            print(""" "My name is Acustos." """)
            print(""" "I will be teaching you all about combat and attacks special to our class." """)
            print(""" "First begin by going into your bear form." """)
            print()
            while True:
                ans = input("Type 'bear form' to turn into a bear.")
                print()
                w = ["BEAR FORM", "SHAPESHIFT", "BEAR"]
                if containsAny(ans, w):
                    print("You feel the blood pumping throughout your body.")
                    print("Every cell is your body is awaiting your command.")
                    print("As you cast Bear Form, they listen.")
                    print("Your blood runs hot and magic energy courses through every fiber of your being.")
                    print("You, as with all the others in your group, are now bears.")
                    print()
                    break
                else:
                    print("Harness your power and try again!")
                    print()
            talk("Look around at your fellow guardians.")
            talk("Notice all of you have different markings or fangs.")
            talk("Your marking is unique only to you, much like a fingerprint.")
            talk("Though we all appear slightly different, we will fight as brothers and sisters of Cataracta.")
            print()
            talk("We will start with a simple attack called 'Swipe'.")
            talk("Swipe will do your attack stat on the target.")
            talk("Keep in mind some enemies have a defense stat that will soften the blow of your attack.")
            talk("Try this attack out on this training dummy.")
            print()
            training_dummy = Enemy(atk=0,
                                   defense=5,
                                   spd=0,
                                   hp=50,
                                   name="Training Dummy")
            print("A " + training_dummy.name + " appears!")
            print("The training dummy has " + str(training_dummy.hp) + " health and " + str(
                training_dummy.defense) + " defense!")
            while training_dummy.hp > 0:
                print()
                training_dummy.display_stats()
                config.player.display_stats()
                print()
                attacks = ["SWIPE"]
                print("Which attack do you want to use?")
                ans = input(str(attacks))
                print()
                ans.upper()
                swipe = ["SWIPE"]
                if containsAny(ans, swipe):
                    training_dummy.take_hit(config.player.getAtk())
                    print("You use swipe!")
                    print("The " + training_dummy.name + " took " + str(config.player.getAtk()) + " damage!")
                    print("The " + training_dummy.name + "'s defense softened the blow by " + str(
                        training_dummy.defense) + "!")
                    print(training_dummy.name + " has " + str(training_dummy.hp) + " left!")
                    print()
                if training_dummy.hp <= 0:
                    break

            print("You killed " + training_dummy.name + "!")
            print()
            talk("Nicely done!")
            talk("As you can see 'swipe' just simply does your attack stat on the target.")
            talk("Not all attacks are this simple.")
            talk("Take 'bite' for example.")
            talk("This attack hits the target for a reduced attack but lowers the enemies defense.")
            talk("Let's try it out.")
            print()
            td = Enemy(atk=0,
                       defense=5,
                       spd=0,
                       hp=50,
                       name="Training Dummy")

            print("A " + td.name + " appears!")
            print("The training dummy has " + str(td.hp)
                  + " health and " + str(td.defense) + " defense!")
            while td.hp > 0:
                print()
                td.display_stats()
                config.player.display_stats()
                print()
                attacks = ["BITE"]
                print("Which attack do you want to use?")
                ans = input(str(attacks))
                print()
                ans.upper()
                BITE = ["BITE"]
                if containsAny(ans, BITE):
                    new_atk = config.player.getAtk() - 5
                    print("You use bite!")
                    if td.defense > 0:
                        td.defense -= 5
                        print(td.name + " had his defense lowered to " + str(td.defense) + "!")
                    elif td.defense == 0:
                        print(td.name + " can't have his defense lowered anymore!")

                    td.take_hit(config.player.getAtk() - 5)
                    print("The " + td.name + " took " + str(new_atk) + " damage!")
                    print(td.name + " has " + str(td.hp) + " left!")
                    print()
            config.player.add_attack("swipe")
            config.player.add_attack("bite")
            print()
            print("You learned 'SWIPE' and 'BITE'!")
            print("'SWIPE' and 'BITE' were added to your attacks!")
            print()
            talk("Great job!")
            talk("Remember, you can only have up to 4 attacks registered at one time.")
            print()
            print()
            talk("Well, next we are going to...")
            print()
            break

    cataracta_battle()


def cataracta_battle():
    print()
    print("Suddenly, a bright light surrounds the entire training courtyard."
          "\nHundreds of tall, muscular, barbaric men appear armed with axes, maces, and swords.")
    print()

    if config.player.getClass() == "guardian":
        print("Acustos shouts above the chaos.")
        talk("Guardians, training is over!")
        talk("It's time to show these Agromanian bastards who they're messing with!")
        print()
    elif config.player.getClass() == "scout":
        print("Dentros shouts above the chaos.")
        talk("Scouts, training is over!")
        talk("It's time to show these Agromanian bastards who they're messing with!")
        print()

    elif config.player.getClass() == "hunter":
        print("Cellious shouts above the chaos.")
        talk("Hunters, training is over!")
        talk("It's time to show these Agromanian bastards who they're messing with!")
        print()

    print("One character stands out from the crowd.")
    print("He stands tall and proud with a long staff in his left hand.")
    print("A scar crosses his left eye, down to his chin.")
    print("The man is dressed in black and purple robes.")
    print("As fighting breaks out all around you, the man levitates up and calls in a dark whisper "
          "that seems to stop the very movement of time.")
    talk("People of Cataracta. Join us or die.")
    print()
    print("Many shouts of protests exit from your fellow druids.")
    print("The man laughs in such a way that sends shivers down your spine.")
    print("An Agromanian approaches you, with his weapon drawn, ready to strike you down.")
    print()

    # Always set new stats for enemy before combat!!!!
    config.enemy.setStats(nameIn="Agromanian Grunt",
                          atkIn=15,
                          defIn=5,
                          hpIn=60,
                          spdIn=9)
    # Done!!!
    combat()

    print()

    config.player.hp = config.player.maxhp
    # Need level stat and exp Stat - Jacob 10-26-17
    print("You gain 1000 exp points!")
    print("You grow to level 2!")
    print()
    # --------------------------------------------------------------------
    print("All around you Agromanian's fall to their death.")
    print("Cataractan Hunters, Scouts, and Guardians all stand exhausted from the battles that just raged.")
    print("Another bright light, penetrates from above you.")
    print("Countless more Agromanians appear from the mage's dark magic.")
    print("The mage chuckles with a careless whisper.")
    print()
    print(""" "Last chance." """)
    print()
    print("You find yourself shouting protests along with all of your fellow Cataractan people.")
    print("This is your purpose. To serve Kaefden. You serve your hometown.")
    print("You will fight or die.")
    print()
    config.enemy.setStats(nameIn="Agromanian Warrior",
                          atkIn=15,
                          defIn=10,
                          hpIn=90,
                          spdIn=7)
    combat()
    # Add Story
    print()
    print("With another foe slain, you looked around at the battle raging.")

    print("Except there was no battle raging...")
    print("Cataractan allies lie dead all around you.")
    print("Swords, axes, and spears alike all glimmer in the sunlight.")
    print("You are utterly surrounded.\n")
    print("The man in the purple robes chuckles maliciously.")
    talk("Stand down, warriors.")
    print("He walks slowly over to you.\n")
    talk("Go tell your precious king that the Cataractan Army has failed. Before it even began.")
    talk("Tell him that Vashirr sent you.")
    print("Vashirr ushers an order to an Agromanian.")
    print("As the Agromanian approaches you, you try to stand and fight, but something is holding you back.")
    print("Vashirr smiles as you figure out that he is muttering a holding spell.")
    print("The agromanian roars as he smacks you with the handle of his axe.")
    print("------------------------------------------------------------------------------------------------")
    print()
    print()
    print()
    print("You stumble up off the ground and immediately smell blood and smoke. ")
    print("You look to the Cataractan castle. Now in flames and rubble.")
    print("The entire city is in ashes.")
    print()
    print("You feel a feeling of sorrow and pulsing anger.")
    print("You start walking, mostly out of instinct.")
    # add imagery
    print("After a while, you find yourself at the ruined gates of the once Great Cataractan Castle.")
    print("You walk the anula filled hallway, to the throne room.")
    print("King Kimious lies dead in the floor.")
    print()
    talk("What hope is there against a force such as this?")
    print()
    print("You suddenly remember the portal to Nacastrum.")
    print("After Nacastrum was betrayed by it's king, Vashirr, portals were added in the major cities for quick access.")
    print("The Agromanians must have killed everyone in the castle before teleporting to the courtyard.")
    print("If not, allies from Nacastrum and Aylova alike would have swarmed the castle.")
    print()
    print("You decide that you need to send word of Cataracta's fall to the Keafden.")
    print("The quickest way to the Kaefden Capital, Aylova, is to take the portal in Nacastrum.")
    print("And the quickest way to Nacastrum is through the portal that links the cities.")
    print()
    # add shit
    print("You step through the portal.")

    config.current_room_id = "c_portal_room"
    return "reload"
    # Remember to set current_room_id to something to avoid infinite loop!


courtyard = Room(name="Courtyard", des="", id="courtyard", directions="", on_enter=courtyard_logic)

