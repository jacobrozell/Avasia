from Avasia.Combat.Hunter_Combat import hunter_combat
from Avasia.Combat.Guardian_Combat import guardian_combat
from Avasia.Combat.Scout_Combat import scout_combat
import Avasia.Logic.config as config


def combat():
    if config.player.class_id == "hunter":
        hunter_combat()

    elif config.player.class_id == "scout":
        scout_combat()

    else:
        guardian_combat()
