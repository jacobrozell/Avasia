import pickle
import Logic.config as config
import os


def is_non_zero_file(fpath):
    return os.path.isfile(fpath) and os.path.getsize(fpath) > 0

all_stats = {}
saveGameFound = False


def saveParameters():
    global all_stats
    global saveGameFound
    all_stats = config.player.getAllStats()
    print(str(all_stats))

    pickle_out = open("savefile.pickle", "wb")
    pickle.dump(all_stats, pickle_out)
    pickle_out.close()
    saveGameFound = True


def loadParameters():
    global saveGameFound
    global all_stats

    pickle_in = open("savefile.pickle", "rb")
    all_stats = pickle.load(pickle_in)

    # Set all of these parameters in config.
    config.player.setName(all_stats["name"])

    config.player.addGold(all_stats["gold"])

    config.player.setAtk(all_stats["atk"])
    config.player.setMaxAtk(all_stats["maxAtk"])

    config.player.setDef(all_stats["def"])
    config.player.setMaxDef(all_stats["maxDef"])

    config.player.setSpeed(all_stats["speed"])
    config.player.setMaxSpeed(all_stats["maxSpeed"])

    config.player.setLuck(all_stats["luck"])
    config.player.setMaxLuck(all_stats["maxLuck"])

    config.player.setHp(all_stats["hp"])
    config.player.setMaxHp(all_stats["maxHp"])

    config.player.setExp(all_stats["exp"])

    config.player.setLevel(all_stats["level"])

    config.player.setClass(all_stats["class"])

    config.player.printInventory = all_stats["printInventory"]
    # config.player.inventory = all_stats["inventory"]

    # ---------------Config Variables---------------

    config.current_room_id = all_stats["currentRoom"]
    config.fountain = all_stats["fountain"]
    config.ulric = all_stats["ulric"]
    config.doran = all_stats["doran"]
    config.varrustysword = all_stats["rustySword"]
    config.varbrokenaxe = all_stats["brokenAxe"]
    config.courtyard = all_stats["courtyard"]
    config.returnfish = all_stats["returnFish"]
    config.portalRoom = all_stats["portalRoom"]

    return True
