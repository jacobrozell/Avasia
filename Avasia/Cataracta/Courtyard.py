from Avasia.Room.Room import *
from Avasia.Logic.util import *
from Avasia.Enemy.EnemyClass import Enemy
from Avasia.Combat.CombatLogic import combat


def courtyard_logic():
    if config.courtyard == 1:
        return "go back"
    config.courtyard = 1
    print()
    print(">>>Training Courtyard<<<")
    print()
    print()
    print("Good Morning and welcome."
          "\nMy name is Cellious."
          "\nYou're here because Kaefden needs an army."
          "\nI'm sure word has gotten around..."
          "\nA group of former Agromanians have escaped from Krothgar."
          "\nThey set aside our differences and they warned us."
          "\nVashirr, the former King of Nacastrum, is training an army of magic-wielding warriors."
          "\nThis is a threat unlike anything we have ever seen."
          "\n"
          "\nWe will begin training based of what your speciality is."
          "\nI need Hunters with me; Scouts with Dentros; Guardians with Acustos."
          "\nYou know who you are."
          "\n")
    while True:
        hunter = ["HUNTER"]
        scout = ["SCOUT"]
        guardian = ["GUARDIAN"]
        user_class = input("Which class are you apart of?")
        user_class = user_class.upper()

        if containsAny(user_class, hunter):
            config.player_hp = 65
            config.player_defense = 5
            config.player_atk = 20
            config.player_spd = 10
            config.class_id = "hunter"
            break

        elif containsAny(user_class, scout):
            config.player_hp = 50
            config.player_defense = 10
            config.player_atk = 15
            config.player_spd = 20
            config.class_id = "scout"
            break

        elif containsAny(user_class, guardian):
            config.player_hp = 100
            config.player_defense = 15
            config.player_atk = 15
            config.player_spd = 5
            config.class_id = "guardian"
            break

        else:
            print()
    while True:

        # Tutorial #
        # ---------------------------------------

        if config.class_id == "hunter":  # wolf
            print()
            print(">>>Hunter Training<<<")
            print()
            print()
            print(""" "My name is Cellious." """)
            print(""" "I will be teaching you all about combat and attacks special to our class." """)
            print()
            print(""" "First begin by going into your wolf form." """)
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
            print("Look around at your fellow hunters.")
            print("Notice all of you have different markings or fangs.")
            print("Your marking is unique only to you, much like a fingerprint.")
            print("Though we all appear slightly different, we will fight as brothers and sisters of Cataracta.")
            print()
            print("We will start with a simple attack called 'strike'.")
            print("Slash will do your attack stat on the target.")
            print("Keep in mind some enemies have a defense stat that will soften the blow of your attack.")
            print("Try this attack out on this training dummy.")
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
                attacks = ["STRIKE"]
                print("Which attack do you want to use?")
                ans = input(str(attacks))
                print()
                ans.upper()
                slash = ["STRIKE"]
                if containsAny(ans, slash):
                    training_dummy.take_hit(config.player_atk)
                    print("You use strike!")
                    print("The " + training_dummy.name + " took " + str(config.player_atk) + " damage!")
                    print("The " + training_dummy.name + "'s defense softened the blow by " + str(training_dummy.defense) +"!")
                    print(training_dummy.name + " has " + str(training_dummy.hp) + " left!")
                    print()
                if training_dummy.hp <= 0:
                    break

            print("You killed " + training_dummy.name + "!")
            print()
            print(""" "Nicely done!" """)
            print(""" "As you can see 'strike' just simply does your attack stat on the target." """)
            print(""" "Not all attacks are this simple." """)
            print(""" "Take 'pounce' for example." """)
            print(""" "This attack hits the target for a reduced attack but lowers the enemies defense." """)
            print(""" "Let's try it out." """)
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
                attacks = ["POUNCE"]
                print("Which attack do you want to use?")
                ans = input(str(attacks))
                print()
                ans.upper()
                pounce = ["POUNCE"]
                if containsAny(ans, pounce):
                    new_atk = config.player_atk - 5
                    print("You use pounce!")
                    if td.defense > 0:
                        td.defense -= 5
                        print(td.name + " had his defense lowered to " + str(td.defense) + "!")
                    elif td.defense == 0:
                        print(td.name + " can't have his defense lowered anymore!")

                    td.take_hit(config.player_atk - 5)
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
            print(""" "Great job!" """)
            print(""" "Remember, you can only have up to 4 attacks registered at one time." """)
            print()
            print()
            print(""" "Well, next we are going to..." """)
            print()
            break

        # Need this to be written like hunter.
        if config.class_id == "scout":  # fox
            print()
            print(">>>Scout Training<<<")
            print()
            print()
            print(""" "My name is Dentros." """)
            print(""" "I will be teaching you all about combat and attacks special to our class." """)
            print()
            print("Let's begin by turning into our fox forms.")
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
            print("Look around at your fellow scouts.")
            print("Notice all of you have different markings.")
            print("Your marking is unique only to you, much like a fingerprint.")
            print("Though we all appear slightly different, we will fight as brothers and sisters of Cataracta.")
            print()
            print("We will start with a simple attack called 'slash'.")
            print("Strike will do your attack stat on the target.")
            print("Keep in mind some enemies have a defense stat that will soften the blow of your attack.")
            print("Try this attack out on this training dummy.")
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
                attacks = ["SLASH"]
                print("Which attack do you want to use?")
                ans = input(str(attacks))
                print()
                ans.upper()
                strike = ["SLASH"]
                if containsAny(ans, strike):
                    training_dummy.take_hit(config.player_atk)
                    print("You use slash!")
                    print("The " + training_dummy.name + " took " + str(config.player_atk) + " damage!")
                    print("The " + training_dummy.name + "'s defense softened the blow by " + str(training_dummy.defense) +"!")
                    print(training_dummy.name + " has " + str(training_dummy.hp) + " left!")
                    print()
                if training_dummy.hp <= 0:
                    break

            print("You killed " + training_dummy.name + "!")
            print()
            print(""" "Nicely done!" """)
            print(""" "As you can see 'slash' just simply does your attack stat on the target." """)
            print(""" "Not all attacks are this simple." """)
            print(""" "Take 'FIEEKEJFEJFEJFJEF' for example." """)
            print(""" "This attack hits the target for a reduced attack but lowers the enemies defense." """)
            print(""" "Let's try it out." """)
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
                attacks = ["POUNCE"]
                print("Which attack do you want to use?")
                ans = input(str(attacks))
                print()
                ans.upper()
                pounce = ["POUNCE"]
                if containsAny(ans, pounce):
                    new_atk = config.player_atk - 5
                    print("You use pounce!")
                    if td.defense > 0:
                        td.defense -= 5
                        print(td.name + " had his defense lowered to " + str(td.defense) + "!")
                    elif td.defense == 0:
                        print(td.name + " can't have his defense lowered anymore!")

                    td.take_hit(config.player_atk - 5)
                    print("The " + td.name + " took " + str(new_atk) + " damage!")
                    print(td.name + " has " + str(td.hp) + " left!")
                    print()

            # Add attacks to Attacks[]
            config.player.add_attack("slash")
            config.player.add_attack("pounce")
            print()
            print("You learned 'SLASH' and 'POUNCE'!")
            print("'SLASH' and 'POUNCE' were added to your attacks!")
            print()
            print(""" "Great job!" """)
            print(""" "Remember, you can only have up to 4 attacks registered at one time." """)
            print()
            print()
            print(""" "Well, next we are going to..." """)
            print()
            break

        # Need this to be written like hunter.
        if config.class_id == "guardian":  # bear
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
            print("Look around at your fellow guardians.")
            print("Notice all of you have different markings or fangs.")
            print("Your marking is unique only to you, much like a fingerprint.")
            print("Though we all appear slightly different, we will fight as brothers and sisters of Cataracta.")
            print()
            print("We will start with a simple attack called 'Swipe'.")
            print("Swipe will do your attack stat on the target.")
            print("Keep in mind some enemies have a defense stat that will soften the blow of your attack.")
            print("Try this attack out on this training dummy.")
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
                attacks = ["SWIPE"]
                print("Which attack do you want to use?")
                ans = input(str(attacks))
                print()
                ans.upper()
                swipe = ["SWIPE"]
                if containsAny(ans, swipe):
                    training_dummy.take_hit(config.player_atk)
                    print("You use swipe!")
                    print("The " + training_dummy.name + " took " + str(config.player_atk) + " damage!")
                    print("The " + training_dummy.name + "'s defense softened the blow by " + str(
                        training_dummy.defense) + "!")
                    print(training_dummy.name + " has " + str(training_dummy.hp) + " left!")
                    print()
                if training_dummy.hp <= 0:
                    break

            print("You killed " + training_dummy.name + "!")
            print()
            print(""" "Nicely done!" """)
            print(""" "As you can see 'swipe' just simply does your attack stat on the target." """)
            print(""" "Not all attacks are this simple." """)
            print(""" "Take 'bite' for example." """)
            print(""" "This attack hits the target for a reduced attack but lowers the enemies defense." """)
            print(""" "Let's try it out." """)
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
                attacks = ["BITE"]
                print("Which attack do you want to use?")
                ans = input(str(attacks))
                print()
                ans.upper()
                BITE = ["BITE"]
                if containsAny(ans, BITE):
                    new_atk = config.player_atk - 5
                    print("You use bite!")
                    if td.defense > 0:
                        td.defense -= 5
                        print(td.name + " had his defense lowered to " + str(td.defense) + "!")
                    elif td.defense == 0:
                        print(td.name + " can't have his defense lowered anymore!")

                    td.take_hit(config.player_atk - 5)
                    print("The " + td.name + " took " + str(new_atk) + " damage!")
                    print(td.name + " has " + str(td.hp) + " left!")
                    print()
            config.player.add_attack("swipe")
            config.player.add_attack("bite")
            print()
            print("You learned 'SWIPE' and 'BITE'!")
            print("'SWIPE' and 'BITE' were added to your attacks!")
            print()
            print(""" "Great job!" """)
            print(""" "Remember, you can only have up to 4 attacks registered at one time." """)
            print()
            print()
            print(""" "Well, next we are going to..." """)
            print()
            break

    cataracta_battle()


def cataracta_battle():
    print()
    print("Suddenly, a bright light surrounds the entire training courtyard."
          "\nHundreds of tall, muscular, barbaric men appear armed with axes, maces, and swords.")
    print()

    if config.class_id == "guardian":
        print("Acustos shouts above the chaos.")
        print(""" "Guardians, training is over!" """)
        print(""" "It's time to show these Agromanian bastards who they're messing with!" """)
        print()
    elif config.class_id == "scout":
        print("Dentros shouts above the chaos.")
        print(""" "Scouts, training is over!" """)
        print(""" "It's time to show these Agromanian bastards who they're messing with!" """)
        print()

    elif config.class_id == "hunter":
        print("Cellious shouts above the chaos.")
        print(""" "Hunters, training is over!" """)
        print(""" "It's time to show these Agromanian bastards who they're messing with!" """)
        print()

    print("One character stands out from the crowd.")
    print("He stands tall and proud with a long staff in his left hand.")
    print("A scar crosses his left eye, down to his chin.")
    print("The man is dressed in black and purple robes.")
    print("As fighting breaks out all around you, the man levitates up and calls in a dark whisper "
          "that seems to stop the very movement of time.")
    print(""" "People of Cataracta. Join us or die." """)
    print()
    print("Many shouts of protests exit from your fellow druids.")
    print("The man laughs in such a way that sends shivers down your spine.")
    print("An Agromanian approaches you, with his weapon drawn, ready to strike you down.")
    print()

    # Always set new stats for enemy before combat!!!!
    config.enemy_atk = 15
    config.enemy_defense = 5
    config.enemy_spd = 9
    config.enemy_hp = 60
    config.enemy_name = "Agromanian Grunt"

    # Done!!!
    combat()

    print()

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
    print("You find yourself shouting protests along with all of your fellow Catarctan people.")
    print("This is your purpose. To serve Kaefden. You serve your hometown.")
    print("You will fight or die.")
    print()
    config.enemy_atk = 10
    config.enemy_defense = 10
    config.enemy_spd = 7
    config.enemy_hp = 90
    config.enemy_name = "Agromanian Warrior"
    combat()
    # Add Story
    # Remember to set current_room_id to something to avoid infinite loop!


courtyard = Room(name="", des="", id="courtyard", directions="", on_enter=courtyard_logic)

