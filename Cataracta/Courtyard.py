from Room.Room import Room
import Logic.config as config
from Logic.util import talk, containsAny
import Logic.Save as save


def courtyard_logic():
    save.saveParameters()
    courtyard.print_name()
    print("You make your way to the Cataractan Legion's courtyard to begin your training.")
    print("A large group of people are standing around three men who seem to be giving a speech.")
    print()
    print("One of the men speaks out in a loud booming voice.")
    print()
    talk("Greetings, men and women, welcome.")
    talk("My name is Cellious, I am the leader of the Packstalkers, commonly known as the hunters.")
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
    print()

    # Introduce Classes
    talk("Hunters are known as the Packstalkers. They use the aspect of the Wolf.")
    talk("Scouts are known as the Skulks of Cataracta. They use the aspect of the Fox.")
    talk("Guardians are known as the Varatho Guardians. They use the aspect of the Bear.")
    print()
    talk("I need Hunters with me; Scouts with Dentros; Guardians with Acustos.")
    talk("You know who you are.")
    print()
    while True:
        hunter = ["HUNTER"]
        scout = ["SCOUT"]
        guardian = ["GUARDIAN"]
        user_class = input("What class are you? (Hunter, Scout, Guardian)")
        user_class = user_class.upper()

        if containsAny(user_class, hunter):
            # Attack
            config.player.set_atk(20)
            config.player.set_max_atk(20)

            # Defense
            config.player.set_def(5)
            config.player.set_max_def(5)

            # Speed
            config.player.set_speed(10)
            config.player.set_max_speed(10)

            # Luck
            config.player.set_luck(15)
            config.player.set_max_luck(15)

            # Hp
            config.player.set_hp(80)
            config.player.set_max_hp(80)

            config.player.set_class("hunter")
            config.player.addForm("Wolf")

            break

        elif containsAny(user_class, scout):
            # Attack
            config.player.set_atk(10)
            config.player.set_max_atk(10)

            # Defense
            config.player.set_def(5)
            config.player.set_max_def(5)

            # Speed
            config.player.set_speed(25)
            config.player.set_max_speed(25)

            # Luck
            config.player.set_luck(5)
            config.player.set_max_luck(5)

            # Hp
            config.player.set_hp(75)
            config.player.set_max_hp(75)

            config.player.set_class("scout")
            config.player.addForm("Fox")
            break

        elif containsAny(user_class, guardian):
            # Attack
            config.player.set_atk(5)
            config.player.set_max_atk(5)

            # Defense
            config.player.set_def(5)
            config.player.set_max_def(5)

            # Speed
            config.player.set_speed(0)
            config.player.set_max_speed(0)

            # Luck
            config.player.set_luck(10)
            config.player.set_max_luck(10)

            # Hp
            config.player.set_hp(80)
            config.player.set_max_hp(80)

            config.player.set_class("guardian")
            config.player.addForm("Bear")
            break

        else:
            print()

    while True:

        # Tutorial
        # ---------------------------------------

        if config.player.get_class() == config.player.hunterId:  # wolf
            print()
            print(">>>Hunter Training<<<")
            print()
            print()
            print("You follow the tall man wearing the pelts and skulls of beasts he has presumably slain.")
            talk("My name is Cellious.")
            talk("I will help you hone your skills under the aspect of the wolf.")
            print()
            talk("First, you must let yourself go.")
            talk("You must shed yourself of your human mantle and assume the form you hold in you.")
            print()
            while True:
                ans = input("Type 'wolf form' to turn into a wolf.")
                print()
                w = ["WOLF FORM", "SHAPESHIFT", "WOLF"]
                if containsAny(ans, w):
                    print("You focus your mind and search your soul for the spirit Cellious spoke of.")
                    print("Your blood runs hot, you can feel and hear your heart pounding in your chest.")
                    print("Every fiber of your being begins to shift your Druidic form into one of a vicious creature.")
                    print("Your spine cracks and your ears shift upward.")
                    print("Your nose changes form and your jaw extends as your teeth begin to protrude from your mouth.")
                    print("Finally, your body comes to a pause and your mind calms.")
                    print()
                    print("You, as with all the others in your group, are now Wolves.")
                    print()
                    break
                else:
                    print("You make an attempt to shift, but fail to do so.")
                    talk("Focus and search your soul! Try again!")
                    print()

            print("Cellious laughs and looks around with a prideful grin.")
            talk("Take a look around at your fellow Packstalkers.")
            talk("Notice all of you have different markings and fangs.")
            talk("Your marks are unique only to you and you alone.")
            talk("Though we appear different to one another, we hunt as one.")
            print()
            talk("You now walk as a lion amongst sheep.")
            talk("All creatures will fear your bloodthirsty form as you stride toward your prey.")
            print()
            talk("Now to the good part. Let's try some friendly duels.")

            # IMPLEMENT DUELS HERE AGAINST ANOTHER WOLF
            print("\n\nNEED TO IMPLEMENT\n\n")

            talk("Good.")
            talk("As you can see, a good strategy can lead to devastating attacks.")
            talk("You must learn to use all of your skills in unison.")
            print()
            talk("For example, next we are goi-")
            print("Cellious is interrupted by a flash of bright light followed by a cascade of darkness.")
            print()
            break

        if config.player.get_class() == config.player.scoutId:  # fox
            print()
            print(">>>Scout Training<<<")
            print()
            print()
            print("You follow the older man carrying a staff and await further instruction.")
            talk("My name is Dentros.")
            talk("I will teach you how to properly carry yourself in your frail form.")
            talk("We may not be as intimidating as Packstalkers or as large as the Varatho Guardians, "
                 "but we can strike just as hard.")
            print()
            talk("Let us begin by transforming into our proper form.")
            talk("You must allow yourself to be free of your Druid form and become one with those who roam these woods.")
            print()
            while True:
                ans = input("Type 'fox form' to turn into a fox.")
                print()
                w = ["FOX FORM", "SHAPESHIFT", "FOX"]
                if containsAny(ans, w):
                    print("As you search for the aspect of the fox hiding inside you, you feel your body begin to heat.")
                    print("Your mind, body, and soul become one.")
                    print("Your spine cracks and your ears shift upward.")
                    print("Your nose changes form and your jaw extends as your teeth begin to sharpen.")
                    print("Finally, your body comes to a pause and your mind calms.")
                    print()
                    print("You, along with the others in your group, are now Fox.")
                    break
                else:
                    print("You make an attempt to shift, but fail to do so.")
                    talk("It's okay. Relax yourself and try again.")
                    print()
            talk("Well done!")
            talk("Look at those around you.")
            talk("Notice the differences between each of you.")
            talk("Your markings are unique to you and only you.")
            talk("Though we all appear different, we all must communicate and work together.", "\n")
            talk("The information we can gather may be the difference between life or death for our people.")
            talk("But scouting isn't the only thing we are good for.")
            talk("There are times when we must strike our enemies or be prepared to defend ourselves.", "\n")
            talk("Now to the good part. Let's try some friendly duels.")

            # IMPLEMENT DUELS HERE AGAINST ANOTHER FOX
            print("\n\nNEED TO IMPLEMENT\n\n")

            talk("Nicely done!")
            talk("As you can see, focusing and exploiting weaknesses in your enemy is what the Skulks are all about.")
            talk("To work effectively, you must use all your abilities in unison.")
            print()
            talk("For example, next we are goi-")
            print("Dentros is interrupted by a flash of bright light followed by a cascade of darkness.")
            print()
            break

        if config.player.get_class() == config.player.guardianId:  # bear
            print()
            print(">>>Guardian Training<<<")
            print()
            print()
            talk("You follow the large Druidic woman who is plated in metals and blue crystals.")
            talk("My name is Acustos.")
            talk("I will teach you all that you must know to defend our people.")
            talk("Our role in protecting our kind is one of the most important.")
            talk("Should something or someone threaten our home, we are the first and last line of defense.")
            print()
            while True:
                ans = input("Type 'bear form' to turn into a bear.")
                print()
                w = ["BEAR FORM", "SHAPESHIFT", "BEAR"]
                if containsAny(ans, w):
                    print("You take a deep breath and focus your mind on the Aspect of the Bear.")
                    print("The blood rushing through your body pushes outward, forcing your body to grow.")
                    print("Your spine cracks and your ears round off and shrink.")
                    print("Your nose changes form and your jaw extends as your teeth begin to sharpen.")
                    print("Your body becomes covered in rough fur and your hands become claws.")
                    print("Finally, your body comes to a pause and your mind calms.")
                    print()
                    print("You, along with the others in your group, are now Bears.")
                    break
                else:
                    print("You make an attempt to shift, but fail to do so.")
                    talk("When the time comes, you must be able to transform at will and without fail! Try again!")
                    print()
            talk("Great work, Guardians!")
            talk("Now, look around you.")
            talk("Notice that all of you appear different to each other.")
            talk("Your markings and build are unique to you and only you.")
            talk("Even though we look different, we must stand as one against the forces that seek to tear us apart.", "\n")
            talk("But your stature alone will not save you.")
            talk("You must learn to fight!", "\n")
            talk("Now to the good part. Let's try some duels.")

            # IMPLEMENT DUELS HERE AGAINST ANOTHER BEAR
            print("\n\nNEED TO IMPLEMENT\n\n")

            talk("Nicely done!")
            talk("You must use everything you can to defend our people.")
            talk("There are many abilities you possess that can turn the tide of battle.")
            print()
            talk("For example, next we are goi-")
            print("Acustos is interrupted by a flash of bright light followed by a cascade of darkness.")
            print()
            break

    cataracta_battle()
    config.current_room_id = "c_portal_room"
    return "reload"


def cataracta_battle():
    print("Before anyone can respond to the sudden change of scenery, a dark portal forms.")
    print("Almost instantaneously, hundreds of burly men charge from the portal.")
    print("You immediately realize that these are Agromanians.")

    if config.player.get_class() == "guardian":
        print("As the slaughter of your people begins, Acustos shouts above the chaos.")
        talk("Varatho Guardians, training is over!")
        talk("Your time has come, hold your ground!")
        print()
    elif config.player.get_class() == "scout":
        print("As the slaughter of your people begins, Dentros shouts above the chaos.")
        talk("Skulks, training is over!")
        talk("Use what you've learned and defend yourselves!")
        print()

    elif config.player.get_class() == "hunter":
        print("As the slaughter of your people begins, Cellious shouts above the chaos.")
        talk("Packstalkers, training is over!")
        talk("Shows these cowards what you're made of!")
        print()

    print("One character stands out from the hoard of Agromanians pouring from the portal.")
    print("He stands tall and proud, holding a staff formed of grey wood and purple stones in his left hand.")
    print("A scar crosses his left eye, and continues down to his chin.")
    print("He is dressed in black and purple robes, unlike the Agromanian.")
    print("As he makes his way across the courtyard, he points the tip of his staff toward your group.")
    print("The end of the staff begins to glow and a blast of dark purple energy is launched in your direction.")
    print()
    print("You manage to jump out of the way before it arrives, but some of your group aren't as lucky.")
    print("The magic burns clean through a few of your group members and you watch as their bodies fall to the ground.")
    print()
    print("The man's skill in magic shows beyond doubt that he is Vashirr, the mage you've heard stories about.")
    print("Vashirr pauses for a moment and then begins to speak in a rough voice.")
    print()
    talk("Druid! Your opposition has forced my hand.")
    talk("Know that Vashirr has brought an end to your twisted kind.")
    print()
    print("Shouts of defiance rage from the Cataractan people.")
    talk("Your weak attempts to defend yourselves only delay the inevitable.")
    print()
    print("An Agromanian approaches you, with his weapon drawn, ready to strike you down.")
    print()

    # Always set stats for enemy before combat!!!!
    config.enemy.setStats(nameIn="Agromanian Grunt",
                          atkIn=15,
                          defIn=5,
                          hpIn=60,
                          spdIn=9)
    config.enemy.set_text("The " + config.enemy.get_name() + " lays his mace into the side of your head.")

    print("\n\nNEED TO IMPLEMENT\n\n")
    config.player.set_hp(config.player.get_max_hp())
    print()
    # --------------------------------------------------------------------
    print("As the battle continues, weak Agromanian's fall to their death.")
    print("The people of Cataracta seem to be easily taking Vashirr's army down.")
    print("But as you take one Agromanian down, three more take its place.")
    print()
    print("The dark portal continues to spew out Agromanian warriors like a waterfall.")
    print("Before you can even think about what is going on around you, another Agromanian charges toward you.")
    print()
    config.enemy.setStats(nameIn="Agromanian Warrior",
                          atkIn=15,
                          defIn=10,
                          hpIn=90,
                          spdIn=7)
    config.enemy.set_text("The " + config.enemy.get_name() + " plows his sword into your chest.")

    print("\n\nNEED TO IMPLEMENT\n\n")

    print()
    print("With another foe slain, you look around you to find the next target.")
    print("But you quickly realize that all of the fighting has come to a stand still.")
    print()
    print("You gaze upon the countless dead Cataractan lying on the ground in pools of blood.")
    print("Your people have swiftly become outmatched by the Agromanian's sheer numbers.")
    print("Completely surrounded, you know that there is nothing you can do to stop the onslaught that has occured,")
    print("But you will die fighting.")
    print()
    print("Just as the hundreds of Agromanian begin to charge toward you, Vashirr calls for them to hault.")
    print("The Agromanian stop like well-trained pets and await their orders.")
    print()
    talk("You there.")
    print("Vashirr levitates up into the air to get past the barbarians surrounding you and places himself opposite you.")
    print("Just as he walks in close proximity to you, you attempt to jump at him.")
    print("Unfortunately, you only get a short distance before he blast you with his staff, causing you to be paralyzed.")
    print()
    talk("Compose yourself, druid. Today, you live.")
    talk("I do, however, have a task for you.")
    talk("I want you to bring a message to the King Kaefden IV.")
    talk("Tell him that the Legions of Cataracta have fallen and that King Kimious has shared his people's fate.")
    talk("Tell him of the horrors his ignorance have brought to your people.")
    talk("Tell him that I am coming.")
    print()
    print("Vashirr turns around and gestures at his men before walking through his portal.")
    print("They all roar and turn towards all the homes and buildings in Cataracta.")
    print("Cataractan bodies are thrown into the Varatho River.")
    print("Houses are burned to the ground")
    print("The keep is being destroyed and defiled.")
    print("You are powerless to stop it.")
    print()
    print("One of the Agromanian trudges to you and smashes your head with the hilt of his axe.")
    print("You are knocked out cold.")
    print("------------------------------------------------------------------------------------------------\n\n\n")
    print("Time passes and you awaken alone in the same place you were before.")
    print("You stumble up off the ground and immediately smell burning fires. ")
    print("You look to the Cataractan castle. Now in flames and rubble.")
    print("The entire city is in ashes.")
    print()
    print("You feel a rush of despair and anger.")
    print("Without a soul in sight, you start walking, mostly out of instinct.")
    print("You head from the courtyard into the ruined gates of the once beautiful Cataractan Castle.")
    print("The blue crystals that line the hallway, called Anula, are completely shattered and in disrepair.")
    print("You make it to the throne room and find King Kimious dead on the floor, surrounded by his most trusted guards.")
    print()
    talk("What hope is there against a force such as this?", "You think to yourself.\n")
    print("You pass a room that emanates a faint glow.")
    print("As you walk into the room, you are greeted with a large stone circle with runes on the ground.")
    print("At the center is a silver ring with the same runes, perpendicular to the ground.")
    print("You realise that this is one of the teleporters that were made by the Mages when the people of Avasia united long ago.")
    print("Called 'Rings of Malkos', these portals were installed in every major city to allow easy and quick access from place to place.")
    print()
    print("On the ground near the center of the ring is a golden staff")
    print("This staff is the key to activating the portal.")
    print("It appears as though the Agromanians had removed it from its holding place to stop forces from Aylova from coming to help.")
    print()
    print("Realizing that even though you'd be doing what Vashirr wants, you must warn the people of Kaefden before they succumb to the same fate.")
    print("You quickly grab the staff and slam it down into its holding place.")
    print("All of the runes lining the ground and Ring of Malkos burst to life with a radiant glow.")
    print()
    print("With your home destroyed and your people slain, you enter the portal.")
    print()
    print("Hopefully, King Kaefden will know what to do.")
    print("Your journey starts here.")
    print()


courtyard = Room(name="Courtyard", des="", id="courtyard", directions="", on_enter=courtyard_logic)
