import random
import pyautogui as pg

PAUSA_VERIFICACAO = 0.5
ATK_SPELLS = ['9', '8', '9', '0']  # HOTKEYS das magias de ataque
EXETA = ['7']
UTITO = ['4']
ATK_COOLDOWNS = [random.uniform(2, 2.4) for _ in ATK_SPELLS]

FOLDER_NAME = 'Feyrist'

MINIMAP = (1753,26,108,112)

PIXEL_MANA = (979, 33)
COR_MANA = (34, 34, 35)

PIXEL_LIFE = (699, 30)
COR_LIFE = (39, 39, 39)

PIXEL_EXURA = (952, 34)
COR_EXURA = (36, 36, 36)

#0 - exori mas
#9 - exori
#8 - exori gran
#7 - exeta res
#6 - exori amp kor
#4 - utito tempo ou utamo