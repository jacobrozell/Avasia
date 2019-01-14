from Room.Room import Room
import Logic.config as config
from Logic.util import talk, containsAny
import Logic.Save as save


def courtyard_logic():
    save.saveParameters()
    courtyard.print_name()
    print("You enter the courtyard and see dozens of druids training.")
    print("Suddenly, another Druid appears next to you and speaks.\n")

    talk("Nice of you to join us! My name is Dentros.", "\n")

    print("You introduce yourself and tell Dentros that you're here to join the legion.\n")

    talk("Well, let's not waste anytime then!.")
    talk("We have three spirit animals that are best known for their skill in combat.")
    talk("The Wolf, the Bear, and the Fox.")
    talk("Which are you?")
    while True:
        user_class = input()
        user_class.upper()

        if containsAny(user_class, "WOLF"):
            # Attack
            config.player.set_atk(10)
            config.player.set_max_atk(10)

            # Speed
            config.player.set_speed(10)
            config.player.set_max_speed(10)

            # Luck
            config.player.set_luck(5)
            config.player.set_max_luck(5)

            # Hp
            config.player.set_hp(20)
            config.player.set_max_hp(20)

            config.player.set_class("hunter")
            break

        elif containsAny(user_class, "FOX"):
            # Attack
            config.player.set_atk(15)
            config.player.set_max_atk(15)

            # Speed
            config.player.set_speed(15)
            config.player.set_max_speed(15)

            # Luck
            config.player.set_luck(5)
            config.player.set_max_luck(5)

            # Hp
            config.player.set_hp(15)
            config.player.set_max_hp(15)

            config.player.set_class("scout")
            break

        elif containsAny(user_class, "BEAR"):
            # Attack
            config.player.set_atk(10)
            config.player.set_max_atk(10)

            # Speed
            config.player.set_speed(1)
            config.player.set_max_speed(1)

            # Luck
            config.player.set_luck(5)
            config.player.set_max_luck(5)

            # Hp
            config.player.set_hp(25)
            config.player.set_max_hp(25)

            config.player.set_class("guardian")
            break

        else:
            talk("Wolf, Bear, or Fox?", "\n")

    while True:
        if config.player.get_class() == config.player.hunterId:
            print()
            talk("Ah, I could tell your spirit animal was the wolf when I saw you.")
            talk("The wolves are very formidable in battle.")
            talk("They hit hard and can take hits well too.")
            print()
            break

        if config.player.get_class() == config.player.guardianId:
            print()
            talk("Yes, the Bear. Bears are our front-line defense.")
            talk("They can take quite a beating before they're defeated.")
            print()
            break
        if config.player.get_class() == config.player.scoutId:
            print()
            talk("Hm, yes a fox. My spirit animal is the fox as well.")
            talk("We are well known for our ability to move quickly and silently.")
            talk("Foxes make up most of our scouting force.")
            print()
            break

    cataracta_battle()
    config.current_room_id = "c_portal_room"
    return "reload"


def cataracta_battle():
    print("You head further into the courtyard to see the king of Cataracta, Kimious, walk out of the Cataractan keep.")
    print("He speaks out to the druids in the courtyard as you make your way to the front to get a good view.\n")

    talk("My friends! The time to fight is drawing near!")
    talk("Our people are under constant threat of an Agromanian invasion.")
    talk("The attack on Oceandale was far too close to Cataracta.")
    talk("We can no longer rely on our hidden passages and mountainess terrain to defend us.")
    talk("We must take the fight to them!", "\n")

    print("The crowd roars in agreement.\n")
    talk("Your undying loyalty to our home speaks volumes an-", "\n")

    print("Kimious is interrupted by a blinding flash of light, followed by a cascade of darkness.")
    print("The sky turns blood red as a dark portal forms at the entrance of the keep.")
    print("A man donned in a dark hooded robe, holding a gray wooden staff walks out of the portal.")
    print("From behind the man floods dozens of what brutish warriors.\n")

    print("Destros shouts out to you.\n")

    talk("Agromanians! They've found us! But how?!", "\n")

    print("Guards rush to protect Kimious, but they're quickly outmatched by the Agromanians sheer numbers")
    print("The hooded man points his staff to Kimious and blasts him with a bolt of dark energy.")
    print("Kimious falls to the floor, lifelessly.\n")

    print("The Druids in the courtyard shout in horror and charge in to fight the oncoming Agromanians")
    print("The hooded man points his staff toward you and unleashes another bolt of energy.")
    print("Before you can react, Dentros shoves you out of the line of fire and takes the hit.")
    print("As you stumble over, an Agromanian confronts you.")

    # Always set stats for enemy before combat!!!
    config.enemy.set_stats(name="Agromanian Grunt",
                           atk=5,
                           hp=15,
                           speed=10)
    config.enemy.set_text("The " + config.enemy.get_name() + " lays his mace into the side of your head.")
    config.combat.start_combat()

    print("\nYou quickly dispatch the Agromanian and reassess the area around you.")
    print("Destros is lying on the floor and an Agromanian is charging toward him.")
    print("You swiftly position yourself in-between Destros and the Agromanian.")

    config.enemy.set_stats(name="Agromanian Warrior",
                           atk=6,
                           hp=18,
                           speed=8)
    config.enemy.set_text("The " + config.enemy.get_name() + "'s sword pierces your chest.")
    config.combat.start_combat()

    print("Another Agromanian falls to their death.")
    print("You turn to help Destros, but it seems your efforts were in vain.")
    print("By the time you managed to get to his side, he had already passed.\n")

    print("Filled with rage, you turn to find another target,")
    print("but you quickly realize that all of the fighting has come to a stand still.\n")

    print("Countless Cataractan lie dead on the ground in pools of their own blood.")
    print("Any survivors are being held hostage by Agromanians around you.\n")

    print("It is in everyone's best interest if you stand still.\n")

    print("From out of the crowd of Agromanians surrounding you, the hooded man comes.")
    print("He walks forward and is only a few feet in-front of you.")
    print("He removes his hood.")
    print("The man has a scar running across his left eye that continues to his chin.")
    print("He speaks to you in a deep, raspy voice.\n")

    talk("Listen to me, and listen carefully.")
    print("He places the tip of his staff to your head.")
    print("You can hear and feel the energy resonating from it.\n")

    talk("I have a message for you to deliver.")
    talk("Tell King Kaefden IV of the horrors his ignorance has brought.")
    talk("Tell him that Cataracta and its king have fallen.")
    talk("Tell him that so long as he holds his unearned claim on this land...", "\n")

    talk("I will not stop.")
    print()
    print("Vashirr turns and with a snap, the Agromanians execute every Druid in their captivity.")
    print("You can only watch in horror as countless people are mercilessly massacred.")
    print("Vashirr returns through the dark portal and before you can do anything to stop the onslaught,")
    print("an Agromanian bashes your head in with his axe, knocking you out cold.")

    # TODO
    print("\n\nNEED TO IMPLEMENT\n\n")

    print()
    print("With another foe slain, you look around you to find the next target.")
    print("But you quickly realize that all of the fighting has come to a stand still.\n")

    print("You gaze upon the countless dead Cataractan lying on the ground in pools of blood.")
    print("Your people have swiftly become outmatched by the Agromanian's sheer numbers.")
    print("Completely surrounded, you know that there is nothing you can do to stop the onslaught that has occured,")
    print("But you will die fighting.\n")

    print("Just as the hundreds of Agromanian begin to charge toward you, Vashirr calls for them to hault.")
    print("The Agromanian stop like well-trained pets and await their orders.\n")

    talk("You there.")
    print("Vashirr levitates up into the air to get past the barbarians surrounding you and places "
          "himself opposite you.")
    print("Just as he walks in close proximity to you, you attempt to jump at him.")
    print("Unfortunately, you only get a short distance before he blast you with his staff, causing you "
          "to be paralyzed.\n")

    talk("Compose yourself, druid. Today, you live.")
    talk("I do, however, have a task for you.")
    talk("I want you to bring a message to the King Kaefden IV.")
    talk("Tell him that the Legions of Cataracta have fallen and that King Kimious has shared his people's fate.")
    talk("Tell him of the horrors his ignorance have brought to your people.")
    talk("Tell him that I am coming.", "\n")

    print("Vashirr turns around and gestures at his men before walking through his portal.")
    print("They all roar and turn towards all the homes and buildings in Cataracta.")
    print("Cataractan bodies are thrown into the Varatho River.")
    print("Houses are burned to the ground")
    print("The keep is being destroyed and defiled.")
    print("You are powerless to stop it.\n")

    print("One of the Agromanian trudges to you and smashes your head with the hilt of his axe.")
    print("You are knocked out cold.")
    print("------------------------------------------------------------------------------------------------\n\n\n")

    print("Time passes and you awaken alone in the same place you were before.")
    print("You stumble up off the ground and immediately smell burning fires. ")
    print("You look to the Cataractan castle. Now in flames and rubble.")
    print("The entire city is in ashes.\n")

    print("You feel a rush of despair and anger.")
    print("Without a soul in sight, you start walking, mostly out of instinct.")
    print("You head from the courtyard into the ruined gates of the once beautiful Cataractan Castle.")
    print("The blue crystals that line the hallway, called Anula, are completely shattered and in disrepair.")
    print("You make it to the throne room and find King Kimious dead on the floor, surrounded by his "
          "most trusted guards.\n")

    talk("What hope is there against a force such as this? You think to yourself.", "\n")
    print("You pass a room that emanates a faint glow.")
    print("As you walk into the room, you are greeted with a large stone circle with runes on the ground.")
    print("At the center is a silver ring with the same runes, perpendicular to the ground.")
    print("You realise that this is one of the teleporters that were made by the Mages when the people "
          "of Avasia united long ago.")
    print("Called 'Rings of Malkos', these portals were installed in every major city to allow easy and quick "
          "access from place to place.\n")

    print("On the ground near the center of the ring is a golden staff")
    print("This staff is the key to activating the portal.")
    print("It appears as though the Agromanians had removed it from its holding place to stop forces from "
          "Aylova from coming to help.\n")

    print("Realizing that even though you'd be doing what Vashirr wants, you must warn the people of Kaefden "
          "before they succumb to the same fate.")
    print("You quickly grab the staff and slam it down into its holding place.")
    print("All of the runes lining the ground and Ring of Malkos burst to life with a radiant glow.\n")

    print("With your home destroyed and your people slain, you enter the portal.\n")

    print("Hopefully, King Kaefden will know what to do.")
    print("Your journey starts here.\n")


courtyard = Room(name="Courtyard", des="", id="courtyard", directions="", on_enter=courtyard_logic)
