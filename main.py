import json
import pyautogui

# Functions
# Formats AC or HP, returning an array of the two text fields (value and desc)
# Also removes ()
# Currently just removes italics formating
def formatACorHP(text):
    text = text.replace('(', '')
    text = text.replace(')', '')
    text = text.replace('_', '')
    text = text.split(" ", 1)
    return text


def writeInfo(attr, text):
    if (attr == 'otherArmorDesc' or attr == 'hpText'):
        infoSplit = formatACorHP(text)
        pyautogui.write(infoSplit[0])
        pyautogui.press('tab')
        pyautogui.write(infoSplit[1])
        pyautogui.press('tab')
    else:
        pyautogui.write(text)
        pyautogui.press('tab')


# Constants
ATTR_IN_ORDER = [
    'name',
    'type',
    'otherArmorDesc',  # Need more for AC vs description
    'hpText',  # Need for for HP vs formula
    'speed',  # Need more for other speed types
    'strPoints',
    'dexPoints',
    'conPoints',
    'intPoints',
    'wisPoints',
    'chaPoints',
    'sthrows',  # Need more for each dif saving throw
    'skills',  # Need more for each dif skill (tab if no prof/expertise)
    'specialdamage',  # Need more to check resistance vulnerability, also check if this is correct
    'conditions',  # Need more
    'darkvision',  # All the sense, don't display if there is none, display in one line otherwise
    'tremorsense',
    'truesight',
    'telepathy',
    'languages',  # Need more
    'cr',
    'customCr',  # Need more (for just xp or if empty)
    'customProf'
    'size',  # Need more to convert from word to number (for token size)
    'abilities', # Need more to check if spellcasting present, and if so to do more
    'bonusActions',  # Just need check if empty, and do dif later in order
    'reactions', # Same as bonusActions
    'legendaries',  # Very similar to bonusActions/reactions
    'mythics',  # Very similar to bonusActions/reactions
    # Will then need to click on + buttons for actions/reactions/etc

]

# Gets the info from the file stats.monster
statsFile = open('stats.monster')
stats = json.loads(statsFile.read())

print(stats['name'])

# Acutally writes the info to roll20
pyautogui.hotkey('alt', 'tab')
for i in range(11):
    attr = ATTR_IN_ORDER[i]
    info = stats[attr]
    writeInfo(attr, info)

# Closees the open file
statsFile.close()