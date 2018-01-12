from Avasia.Logic.Attack_Storage import *
from Avasia.Combat.Hunter_Combat import *
from Avasia.Combat.Guardian_Combat import *
from Avasia.Combat.Scout_Combat import *
import Avasia.Logic.config as config


def combat():
    if config.player.class_id == "hunter":
        hunter_combat()
    elif config.player.class_id == "scout":
        scout_combat()
    else:
        guardian_combat()
