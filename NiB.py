# Nativity in Bits 0.1.4
# Copyright 2008, 2009 Meadow Hill Software
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from random import randrange

character = {}

def diceRoll(number, die):
	rolls = []
	num = 0
	die += 1
	while num < number:
		roll = randrange(1, die)
		rolls.append(roll)
		num += 1
	result = 0
	for result in rolls:
		result += result
	return result

def neutrality(morals):
	global character
	if morals == "Neutral":
		character["Alignment"] = "True " + morals
	else:
		character["Alignment"] = "Neutral " + morals
        
def humanCommunity():
    number = randrange(1, 101)
    global character
    if number < 6:
        character["Community"] = "Small Tribe"
    elif number < 11:
        character["Community"] = "Religious, Arcane, Monastic, or Military Compound"
    elif number < 21:
        character["Community"] = "Frontier Homestead"
    elif number < 36:
        character["Community"] = "Thorp"
    elif number < 56:
        character["Community"] = "Hamlet"
    elif number < 76:
        character["Community"] = "Village"
    elif number < 81:
        character["Community"] = "Small Town"
    elif number < 86:
        character["Community"] = "Large Town"
    elif number < 91:
        character["Community"] = "Small City"
    elif number < 96:
        character["Community"] = "Large City"
    else:
        character["Community"] = "Metropolis"

def dwarvenCommunity():
    number = randrange(1, 91)
    global character
    if number < 11:
        character["Community"] = "Single-Family Redoubt"
    elif number < 21:
        character["Community"] = "Prospecting Camp"
    elif number < 31:
        character["Community"] = "Small Mine"
    elif number < 46:
        character["Community"] = "Large Mine"
    elif number < 66:
        character["Community"] = "Delve"
    else:
        character["Community"] = "Large Delve"

def elvenCommunity():
    number = randrange(1, 96)
    global character
    if number < 51:
        character["Community"] = "Encampment"
    elif number < 86:
        character["Community"] = "Village"
    else:
        character["Community"] = "City"

def ethics(morals):
	global character
	number = randrange(1, 7)
	if number < 3:
		character["Alignment"] = "Lawful " + morals
	elif number < 5:
		neutrality(morals)
	else:
		character["Alignment"] = "Chaotic " + morals

def nonlawfulEthics(morals):
	global character
	number = randrange(1, 5)
	if number < 3:
		character["Alignment"] = "Chaotic " + morals
	else:
		neutrality(morals)
		
def dwarvenEthics(morals):
	global character
	number = randrange(1, 97)
	if number < 66:
		character["Alignment"] = "Lawful " + morals
	elif number < 86:
		neutrality(morals)
	else:
		character["Alignment"] = "Chaotic " + morals

def nonlawfulDwarf(morals):
	global character
	number = randrange(1, 37)
	if number < 26:
		neutrality(morals)
	else:
		character["Alignment"] = "Chaotic " + morals

def elvenEthics(morals):
	global character
	number = randrange(1, 97)
	if number < 66:
		character["Alignment"] = "Chaotic " + morals
	elif number < 86:
		neutrality(morals)
	else:
		character["Alignment"] = "Lawful " + morals

def nonlawfulElf(morals):
	global character
	number = randrange(1, 86)
	if number < 66:
		character["Alignment"] = "Chaotic " + morals
	else:
		neutrality(morals)

def hinEthics(morals):
	global character
	number = randrange(1, 101)
	if number < 61:
		neutrality(morals)
	elif number < 81:
		character["Alignment"] = "Chaotic " + morals
	else:
		character["Alignment"] = "Lawful " + morals

def nonlawfulHin(morals):
	global character
	number = randrange(1, 81)
	if number < 61:
		neutrality(morals)
	else:
		character["Alignment"] = "Chaotic " + morals

def specialist():
	global character
	align = character["Alignment"]
	number = randrange(1, 101)
	if align == "Lawful Good":
		if number < 52:
			character["Class"] = "Abjurer"
		elif number < 54:
			character["Class"] = "Conjurer"
		elif number < 69:
			character["Class"] = "Diviner"
		elif number < 73:
			character["Class"] = "Enchanter"
		elif number < 85:
			character["Class"] = "Evoker"
		elif number < 89:
			character["Class"] = "Illusionist"
		elif number < 97:
			character["Class"] = "Necromancer"
		else:
			character["Class"] = "Transmuter"
	elif align == "Lawful Neutral":
		if number < 18:
			character["Class"] = "Abjurer"
		elif number < 23:
			character["Class"] = "Conjurer"
		elif number < 71:
			character["Class"] = "Diviner"
		elif number < 75:
			character["Class"] = "Enchanter"
		elif number < 89:
			character["Class"] = "Evoker"
		elif number < 93:
			character["Class"] = "Illusionist"
		elif number < 97:
			character["Class"] = "Necromancer"
		else:
			character["Class"] = "Transmuter"
	elif align == "Lawful Evil":
		if number < 12:
			character["Class"] = "Abjurer"
		elif number < 18:
			character["Class"] = "Conjurer"
		elif number < 38:
			character["Class"] = "Diviner"
		elif number < 43:
			character["Class"] = "Enchanter"
		elif number < 59:
			character["Class"] = "Evoker"
		elif number < 64:
			character["Class"] = "Illusionist"
		elif number < 96:
			character["Class"] = "Necromancer"
		else:
			character["Class"] = "Transmuter"
	elif align == "Neutral Good":
		if number < 24:
			character["Class"] = "Abjurer"
		elif number < 31:
			character["Class"] = "Conjurer"
		elif number < 38:
			character["Class"] = "Diviner"
		elif number < 49:
			character["Class"] = "Enchanter"
		elif number < 67:
			character["Class"] = "Evoker"
		elif number < 78:
			character["Class"] = "Illusionist"
		elif number < 90:
			character["Class"] = "Necromancer"
		else:
			character["Class"] = "Transmuter"
	elif align == "True Neutral":
		if number < 8:
			character["Class"] = "Abjurer"
		elif number < 22:
			character["Class"] = "Conjurer"
		elif number < 42:
			character["Class"] = "Diviner"
		elif number < 54:
			character["Class"] = "Enchanter"
		elif number < 73:
			character["Class"] = "Evoker"
		elif number < 84:
			character["Class"] = "Illusionist"
		elif number < 90:
			character["Class"] = "Necromancer"
		else:
			character["Class"] = "Transmuter"
	elif align == "Neutral Evil":
		if number < 4:
			character["Class"] = "Abjurer"
		elif number < 16:
			character["Class"] = "Conjurer"
		elif number < 22:
			character["Class"] = "Diviner"
		elif number < 32:
			character["Class"] = "Enchanter"
		elif number < 48:
			character["Class"] = "Evoker"
		elif number < 58:
			character["Class"] = "Illusionist"
		elif number < 91:
			character["Class"] = "Necromancer"
		else:
			character["Class"] = "Transmuter"
	elif align == "Chaotic Good":
		if number < 8:
			character["Class"] = "Abjurer"
		elif number < 20:
			character["Class"] = "Conjurer"
		elif number < 22:
			character["Class"] = "Diviner"
		elif number < 43:
			character["Class"] = "Enchanter"
		elif number < 53:
			character["Class"] = "Evoker"
		elif number < 74:
			character["Class"] = "Illusionist"
		elif number < 80:
			character["Class"] = "Necromancer"
		else:
			character["Class"] = "Transmuter"
	elif align == "Chaotic Neutral":
		if number < 3:
			character["Class"] = "Abjurer"
		elif number < 26:
			character["Class"] = "Conjurer"
		elif number < 32:
			character["Class"] = "Diviner"
		elif number < 51:
			character["Class"] = "Enchanter"
		elif number < 60:
			character["Class"] = "Evoker"
		elif number < 79:
			character["Class"] = "Illusionist"
		elif number < 82:
			character["Class"] = "Necromancer"
		else:
			character["Class"] = "Transmuter"
	else:
		if number < 2:
			character["Class"] = "Abjurer"
		elif number < 23:
			character["Class"] = "Conjurer"
		elif number < 25:
			character["Class"] = "Diviner"
		elif number < 42:
			character["Class"] = "Enchanter"
		elif number < 50:
			character["Class"] = "Evoker"
		elif number < 67:
			character["Class"] = "Illusionist"
		elif number < 84:
			character["Class"] = "Necromancer"
		else:
			character["Class"] = "Transmuter"

def write_file():
	stats = file("adventurer.txt", "w")
	stats.write("Generated by Nativity in Bits 0.1.4\nSee the Hero Builder's Guidebook (pg. 38) and Player's Handbook II (pg. 136) for more information about some of these terms.\n\nAdventurer Statistics\n")
	stats.write("-----------------------------------\n")
	stats.write("Class = " + character["Class"] + "\n")
	stats.write("Race = " + character["Race"] + "\n")
	stats.write("Alignment = " + character["Alignment"] + "\n")
	stats.write("Age = " + character["Age"] + "\n")
	stats.write("Gender = " + character["Gender"] + "\n")
	stats.write("Height = " + character["Height"] + "\n")
	stats.write("Temperature Zone = " + character["Temperature Zone"] + "\n")
	stats.write("Terrain = " + character["Terrain"] + "\n")
	stats.write("Community = " + character["Community"] + "\n")
	stats.write("Family Economic Status = " + character["Family Economic Status"] + "\n")
	stats.write("Family Social Standing = " + character["Family Social Standing"] + "\n")
	stats.write("Family Defense Readiness = " + character["Family Defense Readiness"] + "\n")
	stats.write("Family Private Ethics = " + character["Family Private Ethics"] + "\n")
	stats.write("Family Public Ethics = " + character["Family Public Ethics"] + "\n")
	stats.write("Family Religious Commitment = " + character["Family Religious Commitment"] + "\n")
	stats.write("Family Reputation = " + character["Family Reputation"] + "\n")
	stats.write("Family Political Views = " + character["Family Political Views"] + "\n")
	stats.write("Family Power Structure = " + character["Family Power Structure"] + "\n")
	stats.write("Ancestors of Note = " + character["Ancestors of Note"] + "\n")
	stats.write("Early Childhood Instruction = " + character["Early Childhood Instruction"] + "\n")
	stats.write("Formal Education = " + character["Formal Education"] + "\n")
	stats.write("Learning a Trade = " + character["Learning a Trade"] + "\n")
	stats.write("Early Childhood Events = " + character["Early Childhood Events"] + "\n")
	stats.write("Youth Events = " + character["Youth Events"] + "\n")
	stats.write("Pivotal Events = " + character["Pivotal Events"] + "\n")
	stats.write("Parents = " + character["Parents"] + "\n")
	stats.write("Siblings = " + character["Siblings"] + "\n")
	stats.write("Grandparents = " + character["Grandparents"] + "\n")
	stats.write("Extended Family = " + character["Extended Family"] + "\n")
	stats.write("Friends = " + character["Friends"] + "\n")
	stats.write("Enemies = " + character["Enemies"] + "\n")
	stats.write("Instructors = " + character["Instructors"] + "\n")
	stats.write("Personality Archetype = " + character["Archetype"] + "\n")
	stats.write("Personality Traits = " + character["Traits"] + "\n")
	stats.close()

number = randrange(1, 101)
if number < 51:
	character["Alignment"] = "Good"
elif number < 91:
	character["Alignment"] = "Neutral"
else:
	character["Alignment"] = "Evil"

number = randrange(1, 101)
if character["Alignment"] == "Good":
	if number < 6:
		character["Class"] = "Barbarian"
	elif number < 11:
		character["Class"] = "Bard"
	elif number < 31:
		character["Class"] = "Cleric"
	elif number < 36:
		character["Class"] = "Druid"
	elif number < 46:
		character["Class"] = "Fighter"
	elif number < 51:
		character["Class"] = "Monk"
	elif number < 56:
		character["Class"] = "Paladin"
	elif number < 66:
		character["Class"] = "Ranger"
	elif number < 76:
		character["Class"] = "Rogue"
	elif number < 81:
		character["Class"] = "Sorcerer"
	else:
		character["Class"] = "Wizard"
elif character["Alignment"] == "Neutral":
	if number < 6:
		character["Class"] = "Barbarian"
	elif number < 11:
		character["Class"] = "Bard"
	elif number < 16:
		character["Class"] = "Cleric"
	elif number < 26:
		character["Class"] = "Druid"
	elif number < 46:
		character["Class"] = "Fighter"
	elif number < 51:
		character["Class"] = "Monk"
	elif number < 56:
		character["Class"] = "Ranger"
	elif number < 76:
		character["Class"] = "Rogue"
	elif number < 81:
		character["Class"] = "Sorcerer"
	else:
		character["Class"] = "Wizard"
else:
	if number < 11:
		character["Class"] = "Barbarian"
	elif number < 16:
		character["Class"] = "Bard"
	elif number < 36:
		character["Class"] = "Cleric"
	elif number < 41:
		character["Class"] = "Druid"
	elif number < 51:
		character["Class"] = "Fighter"
	elif number < 56:
		character["Class"] = "Monk"
	elif number < 61:
		character["Class"] = "Ranger"
	elif number < 81:
		character["Class"] = "Rogue"
	elif number < 86:
		character["Class"] = "Sorcerer"
	else:
		character["Class"] = "Wizard"
	
if character["Alignment"] == "Good":
	if character["Class"] == "Barbarian":
		#table figures multiplied by 75.  Assuming one-third of 1% of good barbarians are gnomes, this yields 25 good gnome barbarians.
		number = randrange(1, 7376)
		if number < 151:
			character["Race"] = "Dwarf"
		elif number < 2551:
			character["Race"] = "Elf"
		elif number < 2576:
			character["Race"] = "Gnome"
		elif number < 2651:
			character["Race"] = "Half-Elf"
		elif number < 2726:
			character["Race"] = "Halfling"
		elif number < 4601:
			character["Race"] = "Half-Orc"
		else:
			character["Race"] = "Human"
	elif character["Class"] == "Bard":
		#table figures multiplied by 3.  This yields 18 good gnome bards.
		number = randrange(1, 319)
		if number < 16:
			character["Race"] = "Dwarf"
		elif number < 112:
			character["Race"] = "Elf"
		elif number < 130:
			character["Race"] = "Gnome"
		elif number < 157:
			character["Race"] = "Half-Elf"
		elif number < 166:
			character["Race"] = "Halfling"
		elif number < 169:
			character["Race"] = "Half-Orc"
		else:
			character["Race"] = "Human"
	elif character["Class"] == "Cleric":
		#table figures multiplied by 5.  This yields 50 good gnome clerics.
		number = randrange(1, 471)
		if number < 116:
			character["Race"] = "Dwarf"
		elif number < 201:
			character["Race"] = "Elf"
		elif number < 251:
			character["Race"] = "Gnome"
		elif number < 276:
			character["Race"] = "Half-Elf"
		elif number < 341:
			character["Race"] = "Halfling"
		elif number < 346:
			character["Race"] = "Half-Orc"
		else:
			character["Race"] = "Human"
	elif character["Class"] == "Druid":
		#table figures multiplied by 36.  Assuming one-third of 1% of good druids are dwarves, this yields 12 good dwarf druids.
		number = randrange(1, 3577)
		if number < 13:
			character["Race"] = "Dwarf"
		elif number < 1129:
			character["Race"] = "Elf"
		elif number < 1345:
			character["Race"] = "Gnome"
		elif number < 1669:
			character["Race"] = "Half-Elf"
		elif number < 1741:
			character["Race"] = "Halfling"
		elif number < 1777:
			character["Race"] = "Half-Orc"
		else:
			character["Race"] = "Human"
	elif character["Class"] == "Fighter":
		#table figures multiplied by 25.  This yields 25 good gnome fighters.
		number = randrange(1, 2426)
		if number < 1026:
			character["Race"] = "Dwarf"
		elif number < 1176:
			character["Race"] = "Elf"
		elif number < 1201:
			character["Race"] = "Gnome"
		elif number < 1251:
			character["Race"] = "Half-Elf"
		elif number < 1301:
			character["Race"] = "Halfling"
		elif number < 1426:
			character["Race"] = "Half-Orc"
		else:
			character["Race"] = "Human"
	elif character["Class"] == "Monk":
		#table figures multiplied by 75.  Assuming one-third of 1% of good monks are gnomes, this yields 25 good gnome monks.
		number = randrange(1, 7151)
		if number < 76:
			character["Race"] = "Dwarf"
		elif number < 826:
			character["Race"] = "Elf"
		elif number < 851:
			character["Race"] = "Gnome"
		elif number < 1226:
			character["Race"] = "Half-Elf"
		elif number < 1376:
			character["Race"] = "Halfling"
		elif number < 1751:
			character["Race"] = "Half-Orc"
		else:
			character["Race"] = "Human"
	elif character["Class"] == "Paladin":
		#table figures multiplied by 3.  Assuming one-third of 1% of paladins are elves, this yields 1 elf paladin.
		number = randrange(1, 263)
		if number < 34:
			character["Race"] = "Dwarf"
		elif number < 35:
			character["Race"] = "Elf"
		elif number < 38:
			character["Race"] = "Gnome"
		elif number < 53:
			character["Race"] = "Half-Elf"
		elif number < 59:
			character["Race"] = "Halfling"
		elif number < 62:
			character["Race"] = "Half-Orc"
		else:
			character["Race"] = "Human"
	elif character["Class"] == "Ranger":
		#table figures multiplied by 9.  This yields 45 good dwarf rangers.
		number = randrange(1, 874)
		if number < 46:
			character["Race"] = "Dwarf"
		elif number < 325:
			character["Race"] = "Elf"
		elif number < 379:
			character["Race"] = "Gnome"
		elif number < 514:
			character["Race"] = "Half-Elf"
		elif number < 532:
			character["Race"] = "Halfling"
		elif number < 577:
			character["Race"] = "Half-Orc"
		else:
			character["Race"] = "Human"
	elif character["Class"] == "Rogue":
		#table figures multiplied by 5.  This yields 30 good gnome rogues.
		number = randrange(1, 481)
		if number < 31:
			character["Race"] = "Dwarf"
		elif number < 96:
			character["Race"] = "Elf"
		elif number < 126:
			character["Race"] = "Gnome"
		elif number < 176:
			character["Race"] = "Half-Elf"
		elif number < 361:
			character["Race"] = "Halfling"
		elif number < 386:
			character["Race"] = "Half-Orc"
		else:
			character["Race"] = "Human"
	elif character["Class"] == "Sorcerer":
		#table figures multiplied by 9.  This yields 36 good dwarf sorcerers.
		number = randrange(1, 838)
		if number < 37:
			character["Race"] = "Dwarf"
		elif number < 316:
			character["Race"] = "Elf"
		elif number < 343:
			character["Race"] = "Gnome"
		elif number < 388:
			character["Race"] = "Half-Elf"
		elif number < 487:
			character["Race"] = "Halfling"
		elif number < 505:
			character["Race"] = "Half-Orc"
		else:
			character["Race"] = "Human"
	elif character["Class"] == "Wizard":
		#table figures multiplied by 12.  This yields 12 good dwarf wizards.
		number = randrange(1, 1141)
		if number < 13:
			character["Race"] = "Dwarf"
		elif number < 493:
			character["Race"] = "Elf"
		elif number < 565:
			character["Race"] = "Gnome"
		elif number < 685:
			character["Race"] = "Half-Elf"
		elif number < 793:
			character["Race"] = "Halfling"
		elif number < 805:
			character["Race"] = "Half-Orc"
		else:
			character["Race"] = "Human"
elif character["Alignment"] == "Neutral":
	if character["Class"] == "Barbarian":
		#gnomes drop by a factor of 5.  This yields 5 neutral gnome barbarians.
		number = randrange(1, 6531)
		if number < 151:
			character["Race"] = "Dwarf"
		elif number < 1051:
			character["Race"] = "Elf"
		elif number < 1056:
			character["Race"] = "Gnome"
		elif number < 1206:
			character["Race"] = "Half-Elf"
		elif number < 1431:
			character["Race"] = "Halfling"
		elif number < 4356:
			character["Race"] = "Half-Orc"
		else:
			character["Race"] = "Human"
	elif character["Class"] == "Bard":
		#gnomes drop by a factor of 3.  This yields 6 neutral gnome bards.
		number = randrange(1, 268)
		if number < 10:
			character["Race"] = "Dwarf"
		elif number < 64:
			character["Race"] = "Elf"
		elif number < 70:
			character["Race"] = "Gnome"
		elif number < 100:
			character["Race"] = "Half-Elf"
		elif number < 115:
			character["Race"] = "Halfling"
		elif number < 121:
			character["Race"] = "Half-Orc"
		else:
			character["Race"] = "Human"
	elif character["Class"] == "Cleric":
		#gnomes drop by a factor of 10.  This yields 5 neutral gnome clerics.
		number = randrange(1, 451)
		if number < 131:
			character["Race"] = "Dwarf"
		elif number < 191:
			character["Race"] = "Elf"
		elif number < 196:
			character["Race"] = "Gnome"
		elif number < 241:
			character["Race"] = "Half-Elf"
		elif number < 301:
			character["Race"] = "Halfling"
		elif number < 311:
			character["Race"] = "Half-Orc"
		else:
			character["Race"] = "Human"
	elif character["Class"] == "Druid":
		#dwarves drop by one-third.  This yields 8 neutral dwarf druids.
		number = randrange(1, 3177)
		if number < 9:
			character["Race"] = "Dwarf"
		elif number < 1125:
			character["Race"] = "Elf"
		elif number < 1161:
			character["Race"] = "Gnome"
		elif number < 1341:
			character["Race"] = "Half-Elf"
		elif number < 1413:
			character["Race"] = "Halfling"
		elif number < 1449:
			character["Race"] = "Half-Orc"
		else:
			character["Race"] = "Human"
	elif character["Class"] == "Fighter":
		#gnomes drop by a factor of 5.  This yields 5 neutral gnome fighters.
		number = randrange(1, 2406)
		if number < 851:
			character["Race"] = "Dwarf"
		elif number < 1026:
			character["Race"] = "Elf"
		elif number < 1031:
			character["Race"] = "Gnome"
		elif number < 1156:
			character["Race"] = "Half-Elf"
		elif number < 1206:
			character["Race"] = "Halfling"
		elif number < 1456:
			character["Race"] = "Half-Orc"
		else:
			character["Race"] = "Human"
	elif character["Class"] == "Monk":
		#gnomes drop by a factor of 5.  This yields 5 neutral gnome monks.
		number = randrange(1, 7556)
		if number < 51:
			character["Race"] = "Dwarf"
		elif number < 276:
			character["Race"] = "Elf"
		elif number < 281:
			character["Race"] = "Gnome"
		elif number < 1031:
			character["Race"] = "Half-Elf"
		elif number < 1181:
			character["Race"] = "Halfling"
		elif number < 1931:
			character["Race"] = "Half-Orc"
		else:
			character["Race"] = "Human"
	elif character["Class"] == "Ranger":
		#dwarves drop by a factor of 5.  This yields 9 neutral dwarf rangers.
		number = randrange(1, 865)
		if number < 10:
			character["Race"] = "Dwarf"
		elif number < 325:
			character["Race"] = "Elf"
		elif number < 343:
			character["Race"] = "Gnome"
		elif number < 496:
			character["Race"] = "Half-Elf"
		elif number < 514:
			character["Race"] = "Halfling"
		elif number < 604:
			character["Race"] = "Half-Orc"
		else:
			character["Race"] = "Human"
	elif character["Class"] == "Rogue":
		#gnomes drop by a factor of 6.  This yields 5 neutral gnome rogues.
		number = randrange(1, 486)
		if number < 21:
			character["Race"] = "Dwarf"
		elif number < 46:
			character["Race"] = "Elf"
		elif number < 51:
			character["Race"] = "Gnome"
		elif number < 126:
			character["Race"] = "Half-Elf"
		elif number < 316:
			character["Race"] = "Halfling"
		elif number < 366:
			character["Race"] = "Half-Orc"
		else:
			character["Race"] = "Human"
	elif character["Class"] == "Sorcerer":
		#dwarves drop by a factor of 4.  This yields 9 neutral dwarf sorcerers.
		number = randrange(1, 856)
		if number < 10:
			character["Race"] = "Dwarf"
		elif number < 136:
			character["Race"] = "Elf"
		elif number < 145:
			character["Race"] = "Gnome"
		elif number < 280:
			character["Race"] = "Half-Elf"
		elif number < 388:
			character["Race"] = "Halfling"
		elif number < 433:
			character["Race"] = "Half-Orc"
		else:
			character["Race"] = "Human"
	elif character["Class"] == "Wizard":
		#dwarves drop by one-third.  This yields 8 neutral dwarf wizards.
		number = randrange(1, 1173)
		if number < 9:
			character["Race"] = "Dwarf"
		elif number < 345:
			character["Race"] = "Elf"
		elif number < 357:
			character["Race"] = "Gnome"
		elif number < 537:
			character["Race"] = "Half-Elf"
		elif number < 597:
			character["Race"] = "Halfling"
		elif number < 609:
			character["Race"] = "Half-Orc"
		else:
			character["Race"] = "Human"
else:
	if character["Class"] == "Barbarian":
		#gnomes drop by another factor of 5.  This yields 1 evil gnome barbarian.
		number - randrange(1, 2944)
		if number < 18:
			character["Race"] = "Dwarf"
		elif number < 243:
			character["Race"] = "Elf"
		elif number < 244:
			character["Race"] = "Gnome"
		elif number < 319:
			character["Race"] = "Half-Elf"
		elif number < 469:
			character["Race"] = "Halfling"
		elif number < 2194:
			character["Race"] = "Half-Orc"
		else:
			character["Race"] = "Human"
	elif character["Class"] == "Bard":
		#gnomes drop by a factor of 5.  This yields 1 evil gnome bard.
		number = randrange(1, 120)
		if number < 2:
			character["Race"] = "Dwarf"
		elif number < 11:
			character["Race"] = "Elf"
		elif number < 12:
			character["Race"] = "Gnome"
		elif number < 15:
			character["Race"] = "Half-Elf"
		elif number < 21:
			character["Race"] = "Halfling"
		elif number < 90:
			character["Race"] = "Half-Orc"
		else:
			character["Race"] = "Human"
	elif character["Class"] == "Cleric":
		#gnomes drop by a factor of 5.  This yields 1 evil gnome cleric.
		number = randrange(1, 282)
		if number < 16:
			character["Race"] = "Dwarf"
		elif number < 41:
			character["Race"] = "Elf"
		elif number < 42:
			character["Race"] = "Gnome"
		elif number < 92:
			character["Race"] = "Half-Elf"
		elif number < 112:
			character["Race"] = "Halfling"
		elif number < 127:
			character["Race"] = "Half-Orc"
		else:
			character["Race"] = "Human"
	elif character["Class"] == "Druid":
		#dwarves drop by a factor of 9.  This yields 1 evil dwarf druid.
		number = randrange(1, 2025)
		if number < 2:
			character["Race"] = "Dwarf"
		elif number < 73:
			character["Race"] = "Elf"
		elif number < 81:
			character["Race"] = "Gnome"
		elif number < 117:
			character["Race"] = "Half-Elf"
		elif number < 153:
			character["Race"] = "Halfling"
		elif number < 225:
			character["Race"] = "Half-Orc"
		else:
			character["Race"] = "Human"
	elif character["Class"] == "Fighter":
		#gnomes drop by another factor of 5.  This yields 1 evil gnome fighter.
		number = randrange(1, 1327)
		if number < 101:
			character["Race"] = "Dwarf"
		elif number < 176:
			character["Race"] = "Elf"
		elif number < 177:
			character["Race"] = "Gnome"
		elif number < 302:
			character["Race"] = "Half-Elf"
		elif number < 352:
			character["Race"] = "Halfling"
		elif number < 577:
			character["Race"] = "Half-Orc"
		else:
			character["Race"] = "Human"
	elif character["Class"] == "Monk":
		#gnomes drop by another factor of 5.  This yields 1 evil gnome monk.
		number = randrange(1, 6889)
		if number < 7:
			character["Race"] = "Dwarf"
		elif number < 63:
			character["Race"] = "Elf"
		elif number < 64:
			character["Race"] = "Gnome"
		elif number < 814:
			character["Race"] = "Half-Elf"
		elif number < 889:
			character["Race"] = "Halfling"
		elif number < 1639:
			character["Race"] = "Half-Orc"
		else:
			character["Race"] = "Human"
	elif character["Class"] == "Ranger":
		#dwarves drop by a factor of 9.  This yields 1 evil dwarf ranger.
		number = randrange(1, 627)
		if number < 2:
			character["Race"] = "Dwarf"
		elif number < 101:
			character["Race"] = "Elf"
		elif number < 105:
			character["Race"] = "Gnome"
		elif number < 258:
			character["Race"] = "Half-Elf"
		elif number < 276:
			character["Race"] = "Halfling"
		elif number < 357:
			character["Race"] = "Half-Orc"
		else:
			character["Race"] = "Human"
	elif character["Class"] == "Rogue":
		#gnomes drop by a factor of 5.  This yields 1 evil gnome rogue.
		number = randrange(1, 352)
		if number < 6:
			character["Race"] = "Dwarf"
		elif number < 16:
			character["Race"] = "Elf"
		elif number < 17:
			character["Race"] = "Gnome"
		elif number < 92:
			character["Race"] = "Half-Elf"
		elif number < 202:
			character["Race"] = "Halfling"
		elif number < 252:
			character["Race"] = "Half-Orc"
		else:
			character["Race"] = "Human"
	elif character["Class"] == "Sorcerer":
		#dwarves drop by a factor of 9.  This yields 1 evil dwarf sorcerer.
		number = randrange(1, 616)
		if number < 2:
			character["Race"] = "Dwarf"
		elif number < 11:
			character["Race"] = "Elf"
		elif number < 13:
			character["Race"] = "Gnome"
		elif number < 148:
			character["Race"] = "Half-Elf"
		elif number < 211:
			character["Race"] = "Halfling"
		elif number < 256:
			character["Race"] = "Half-Orc"
		else:
			character["Race"] = "Human"
	elif character["Class"] == "Wizard":
		#dwarves drop by a factor of 9.  This yields 1 evil dwarf wizard.
		number = randrange(1, 944)
		if number < 2:
			character["Race"] = "Dwarf"
		elif number < 134:
			character["Race"] = "Elf"
		elif number < 136:
			character["Race"] = "Gnome"
		elif number < 316:
			character["Race"] = "Half-Elf"
		elif number < 340:
			character["Race"] = "Halfling"
		elif number < 344:
			character["Race"] = "Half-Orc"
		else:
			character["Race"] = "Human"

job = character["Class"]
morals = character["Alignment"]
race = character["Race"]
if job == "Bard" or job == "Barbarian":
	if race == "Dwarf":
		nonlawfulDwarf(morals)
	elif race == "Halfling":
		nonlawfulHin(morals)
	elif race == "Gnome" or race == "Human":
		nonlawfulEthics(morals)
	else:
		nonlawfulElf(morals)
elif job == "Druid":
	if morals != "Neutral":
		character["Alignment"] = "Neutral " + morals
	else:
		if race == "Dwarf":
			dwarvenEthics(morals)
		elif race == "Halfling":
			hinEthics(morals)
		elif race == "Gnome" or race == "Human":
			ethics(morals)
		else:
			elvenEthics(morals)
elif job == "Monk":
	character["Alignment"] = "Lawful " + morals
elif job == "Paladin":
	character["Alignment"] = "Lawful Good"
else:
	if race == "Dwarf":
		dwarvenEthics(morals)
	elif race == "Halfling":
		hinEthics(morals)
	elif race == "Gnome" or race == "Human":
		ethics(morals)
	else:
		elvenEthics(morals)

if job == "Wizard":
	number = randrange(1, 86)
	if race == "Gnome":
		if number < 66:
			character["Class"] = "Illusionist"
		else:
			number = randrange(1, 86)
			if number > 65:
				specialist()
	else:
		if number > 65:
			specialist()

number = randrange(1, 101)
if number < 16:
    character["Temperature Zone"] = "Cold"
elif number > 65:
    character["Temperature Zone"] = "Warm"
else:
    character["Temperature Zone"] = "Temperate"

number = randrange(1, 101)
if number < 11:
    character["Terrain"] = "Desert"
elif number < 31:
    character["Terrain"] = "Plains"
elif number < 46:
    character["Terrain"] = "Forest"
elif number < 61:
    character["Terrain"] = "Hills"
elif number < 71:
    character["Terrain"] = "Mountains"
elif number < 81:
    character["Terrain"] = "Marsh"
elif number < 86:
    character["Terrain"] = "Aquatic"
elif number < 91:
    character["Terrain"] = "Underground"
else:
    character["Terrain"] = "Nomadic"

if character["Race"] == "Dwarf":
    number = randrange(1, 101)
    if number < 11:
        character["Community"] = "Single-Family Redoubt"
    elif number < 21:
        character["Community"] = "Prospecting Camp"
    elif number < 31:
        character["Community"] = "Small Mine"
    elif number < 46:
        character["Community"] = "Large Mine"
    elif number < 66:
        character["Community"] = "Delve"
    elif number < 91:
        character["Community"] = "Large Delve"
    else:
        humanCommunity()
        value = character["Community"]
        value = "Human Area: " + value
        character["Community"] = value
elif character["Race"] == "Elf":
    number = randrange(1, 101)
    if number < 51:
        character["Community"] = "Encampment"
    elif number < 86:
        character["Community"] = "Village"
    elif number < 96:
        character["Community"] = "City"
    else:
        humanCommunity()
        value = character["Community"]
        value = "Human Area: " + value
        character["Community"] = value
elif character["Race"] == "Gnome":
    number = randrange(1, 101)
    if number < 11:
        character["Community"] = "Solitary Family"
    elif number < 41:
        character["Community"] = "Cluster"
    elif number < 71:
        character["Community"] = "Gathering"
    elif number < 81:
        humanCommunity()
        value = character["Community"]
        value = "Human Area: " + value
        character["Community"] = value
    elif number < 91:
        dwarvenCommunity()
        value = character["Community"]
        value = "Dwarven Area: " + value
        character["Community"] = value
    else:
        elvenCommunity()
        value = character["Community"]
        value = "Elven Area: " + value
        character["Community"] = value
elif character["Race"] == "Half-Elf":
    number = randrange(1, 101)
    if number < 21:
        character["Community"] = "Fringe Community"
    elif number < 86:
        humanCommunity()
        value = character["Community"]
        value = "Human Area: " + value
        character["Community"] = value
    else:
        elvenCommunity()
        value = character["Community"]
        value = "Elven Area: " + value
        character["Community"] = value
elif character["Race"] == "Halfling":
    number = randrange(1, 101)
    if number < 31:
        character["Community"] = "Clan"
    elif number < 66:
        character["Community"] = "Troupe"
    elif number < 81:
        character["Community"] = "Shire"
    elif number < 91:
        character["Community"] = "Town"
    elif number < 96:
        character["Community"] = "County"
    else:
        humanCommunity()
        value = character["Community"]
        value = "Human Area: " + value
        character["Community"] = value
elif character["Race"] == "Half-Orc":
    number = randrange(1, 101)
    if number < 21:
        character["Community"] = "Fringe Community"
    elif number < 86:
        humanCommunity()
        value = character["Community"]
        value = "Human Area: " + value
        character["Community"] = value
    else:
        character["Community"] = "Orc-Dominated Area"
elif character["Race"] == "Human":
    humanCommunity()

number = randrange(1, 101)
if number < 6:
    character["Family Economic Status"] = "Orphan"
elif number < 16:
    character["Family Economic Status"] = "Refugee"
elif number < 41:
    character["Family Economic Status"] = "Poor"
elif number < 61:
    character["Family Economic Status"] = "Moderate"
elif number < 76:
    character["Family Economic Status"] = "Wealthy"
elif number < 81:
    character["Family Economic Status"] = "Religious Order"
elif number < 86:
    character["Family Economic Status"] = "Arcane Order"
elif number < 91:
    character["Family Economic Status"] = "Monastic Order"
elif number < 96:
    character["Family Economic Status"] = "Wealth Unimportant"
else:
    character["Family Economic Status"] = "Military Support"

number = randrange(1, 101)
if number < 11:
    character["Family Social Standing"] = "Newcomer"
elif number < 16:
    character["Family Social Standing"] = "Criminal"
elif number < 21:
    character["Family Social Standing"] = "Slave"
elif number < 46:
    character["Family Social Standing"] = "Lower Class"
elif number < 66:
    character["Family Social Standing"] = "Skilled Trade or Merchant Family"
elif number < 76:
    character["Family Social Standing"] = "Positive Religious, Arcane, Monastic, or Military Affiliation"
elif number < 86:
    character["Family Social Standing"] = "Negative Religious, Arcane, Monastic, or Military Affiliation"
elif number < 96:
    character["Family Social Standing"] = "Upper Class"
else:
    character["Family Social Standing"] = "Noble"

number = randrange(1, 101)
if number < 11:
    character["Family Defense Readiness"] = "None"
elif number < 21:
    character["Family Defense Readiness"] = "Low"
elif number < 41:
    character["Family Defense Readiness"] = "Rudimentary"
elif number < 56:
    character["Family Defense Readiness"] = "Medium"
elif number < 71:
    character["Family Defense Readiness"] = "High"
elif number < 81:
    character["Family Defense Readiness"] = "Outstanding"
elif number < 91:
    character["Family Defense Readiness"] = "Hired"
elif number < 96:
    character["Family Defense Readiness"] = "Magical"
else:
    character["Family Defense Readiness"] = "Mixed"

number = randrange(1, 101)
if number < 26:
    character["Family Private Ethics"] = "Neutral"
elif number < 51:
    character["Family Private Ethics"] = "Fair"
elif number < 76:
    character["Family Private Ethics"] = "Good"
elif number < 91:
    character["Family Private Ethics"] = "Untrustworthy"
else:
    character["Family Private Ethics"] = "Evil"

number = randrange(1, 101)
if number < 61:
    character["Family Public Ethics"] = "Normal"
elif number < 76:
    character["Family Public Ethics"] = "Undeserved"
elif number < 91:
    character["Family Public Ethics"] = "Recent Change"
else:
    character["Family Public Ethics"] = "Beyond Reproach/Beyond Contempt"

number = randrange(1, 101)
if number < 21:
    character["Family Religious Commitment"] = "Neutral/Uninterested"
elif number < 41:
    character["Family Religious Commitment"] = "Strong"
elif number < 61:
    character["Family Religious Commitment"] = "Historical"
elif number < 71:
    character["Family Religious Commitment"] = "Enmity"
elif number < 81:
    character["Family Religious Commitment"] = "Participatory"
elif number < 86:
    character["Family Religious Commitment"] = "Open Heretics"
elif number < 91:
    character["Family Religious Commitment"] = "Hidden Heretics"
else:
    character["Family Religious Commitment"] = "Mixed"

number = randrange(1, 101)
if number < 41:
    character["Family Reputation"] = "Unknown"
elif number < 56:
    character["Family Reputation"] = "Good"
elif number < 66:
    character["Family Reputation"] = "Outstanding"
elif number < 76:
    character["Family Reputation"] = "A Black Sheep or Two"
elif number < 91:
    character["Family Reputation"] = "Mostly Bad"
else:
    character["Family Reputation"] = "Bad"

number = randrange(1, 101)
if number < 16:
    character["Family Political Views"] = "Apolitical"
elif number < 31:
    character["Family Political Views"] = "Supportive"
elif number < 41:
    character["Family Political Views"] = "Enfranchised"
elif number < 46:
    character["Family Political Views"] = "Enfranchised Progressive"
elif number < 51:
    character["Family Political Views"] = "Enfranchised Radical"
elif number < 66:
    character["Family Political Views"] = "Loyal Opposition"
elif number < 76:
    character["Family Political Views"] = "Dissatisfied"
elif number < 86:
    character["Family Political Views"] = "Dissident"
elif number < 91:
    character["Family Political Views"] = "Radical"
else:
    character["Family Political Views"] = "Mixed"

number = randrange(1, 101)
if number < 11:
    character["Family Power Structure"] = "Unorganized"
elif number < 31:
    character["Family Power Structure"] = "Elders"
elif number < 41:
    character["Family Power Structure"] = "Patriarchy"
elif number < 51:
    character["Family Power Structure"] = "Matriarchy"
elif number < 61:
    character["Family Power Structure"] = "Oligarchy"
elif number < 71:
    character["Family Power Structure"] = "Meritocracy"
elif number < 91:
    character["Family Power Structure"] = "Divided"
elif number < 96:
    character["Family Power Structure"] = "External"
else:
    character["Family Power Structure"] = "Domination"

number = randrange(1, 101)
if number < 50:
    character["Ancestors of Note"] = "None"
elif number < 56:
    character["Ancestors of Note"] = "Forgotten"
elif number < 61:
    character["Ancestors of Note"] = "Immigrant"
elif number < 64:
    character["Ancestors of Note"] = "Master Artisan"
elif number < 67:
    character["Ancestors of Note"] = "Successful Merchant"
elif number < 70:
    character["Ancestors of Note"] = "Unsuccessful Merchant"
elif number < 73:
    character["Ancestors of Note"] = "Cleric"
elif number < 76:
    character["Ancestors of Note"] = "Arcanist"
elif number < 78:
    character["Ancestors of Note"] = "Magic Item"
elif number == 78:
    character["Ancestors of Note"] = "Spell Creator"
elif number == 79:
    character["Ancestors of Note"] = "Item Creator"
elif number < 82:
    character["Ancestors of Note"] = "Victorious Hero"
elif number < 84:
    character["Ancestors of Note"] = "Defeated Hero"
elif number == 84:
    character["Ancestors of Note"] = "Successful Founder"
elif number == 85:
    character["Ancestors of Note"] = "Unsuccessful Founder"
elif number == 86:
    character["Ancestors of Note"] = "Successful Leader"
elif number == 87:
    character["Ancestors of Note"] = "Unsuccessful Leader"
elif number < 91:
    character["Ancestors of Note"] = "Successful Hero"
elif number == 91:
    character["Ancestors of Note"] = "Disbelieved Hero"
elif number == 92:
    character["Ancestors of Note"] = "False Hero"
elif number == 93:
    character["Ancestors of Note"] = "Exile"
elif number == 94:
    character["Ancestors of Note"] = "Failed Rebel"
elif number == 95:
    character["Ancestors of Note"] = "Traitor"
elif number == 96:
    character["Ancestors of Note"] = "Cultist"
elif number == 97:
    character["Ancestors of Note"] = "Villain"
elif number == 98:
    character["Ancestors of Note"] = "Prophecy"
elif number == 99:
    character["Ancestors of Note"] = "God-Touched"
elif number == 100:
    character["Ancestors of Note"] = "Otherworldly"

number = randrange(1, 101)
if number < 21:
    character["Early Childhood Instruction"] = "Outdoors"
elif number < 41:
    character["Early Childhood Instruction"] = "Book Learning"
elif number < 56:
    character["Early Childhood Instruction"] = "Religious"
elif number < 66:
    character["Early Childhood Instruction"] = "Language"
elif number < 76:
    character["Early Childhood Instruction"] = "Arts"
elif number < 86:
    character["Early Childhood Instruction"] = "Multicultural"
elif number < 96:
    character["Early Childhood Instruction"] = "Business/Politics"
else:
    character["Early Childhood Instruction"] = "Magic"

number = randrange(1, 101)
if number < 26:
    character["Formal Education"] = "Agriculture"
elif number < 31:
    character["Formal Education"] = "History"
elif number < 36:
    character["Formal Education"] = "Politics"
elif number < 41:
    character["Formal Education"] = "Religion"
elif number < 46:
    character["Formal Education"] = "Natural History"
elif number < 51:
    character["Formal Education"] = "Multicultural"
elif number < 56:
    character["Formal Education"] = "Arts"
elif number < 61:
    character["Formal Education"] = "Literature"
elif number < 66:
    character["Formal Education"] = "Math"
elif number < 71:
    character["Formal Education"] = "Advanced Math"
elif number < 76:
    character["Formal Education"] = "Astronomy"
elif number < 86:
    character["Formal Education"] = "Finishing School"
elif number < 96:
    character["Formal Education"] = "School of Hard Knocks"
else:
    character["Formal Education"] = "Magic"

number = randrange(1, 101)
if number < 21:
    character["Learning a Trade"] = "Farmer"
elif number < 31:
    character["Learning a Trade"] = "Hunter/Trapper"
elif number < 41:
    character["Learning a Trade"] = "Craft"
elif number < 51:
    character["Learning a Trade"] = "Religious"
elif number < 61:
    character["Learning a Trade"] = "Politics"
elif number < 71:
    character["Learning a Trade"] = "Healing"
elif number < 76:
    character["Learning a Trade"] = "Specialized"
elif number < 86:
    character["Learning a Trade"] = "Military Training"
elif number < 91:
    character["Learning a Trade"] = "Special Military Training"
elif number < 96:
    character["Learning a Trade"] = "Monastery/Knightly Order"
else:
    character["Learning a Trade"] = "Arcanist"

number = randrange(1, 101)
if number < 16:
    character["Early Childhood Events"] = "Survived Childhood Danger"
elif number < 31:
    character["Early Childhood Events"] = "Survived Major Danger to Community"
elif number < 46:
    character["Early Childhood Events"] = "Undertook a Long Journey"
elif number < 56:
    character["Early Childhood Events"] = "Witness"
elif number < 61:
    character["Early Childhood Events"] = "Astronomical Event"
elif number < 66:
    character["Early Childhood Events"] = "Personal Epiphany"
elif number < 76:
    character["Early Childhood Events"] = "Became a Refugee"
elif number < 86:
    character["Early Childhood Events"] = "Death in the Family"
elif number < 96:
    character["Early Childhood Events"] = "Illness"
else:
    character["Early Childhood Events"] = "Injury or Physical Defect"

number = randrange(1, 101)
if number < 16:
    character["Youth Events"] = "Battle"
elif number < 26:
    character["Youth Events"] = "Adventure"
elif number < 36:
    character["Youth Events"] = "Politics"
elif number < 51:
    character["Youth Events"] = "Great Romance"
elif number < 61:
    character["Youth Events"] = "Religion"
elif number < 71:
    character["Youth Events"] = "Arcane"
elif number < 81:
    character["Youth Events"] = "Healing"
elif number < 96:
    character["Youth Events"] = "Crime"
else:
    character["Youth Events"] = "Discovery"

number = randrange(1, 101)
if number < 56:
    character["Pivotal Events"] = "No Pivotal Events"
elif number < 66:
    character["Pivotal Events"] = "Refugee"
elif number < 71:
    character["Pivotal Events"] = "Cultural Shift"
elif number < 76:
    character["Pivotal Events"] = "Under Siege"
elif number < 81:
    character["Pivotal Events"] = "Climactic Battle"
elif number < 86:
    character["Pivotal Events"] = "All-Out War"
elif number < 96:
    character["Pivotal Events"] = "Community Crisis"
else:
    character["Pivotal Events"] = "Religious Awakening"

number = randrange(1, 101)
if number < 56:
    character["Parents"] = "Two Living Parents"
elif number < 66:
    character["Parents"] = "One Living Parent"
elif number < 71:
    character["Parents"] = "Both Parents Dead"
elif number < 81:
    character["Parents"] = "One Ill"
elif number < 86:
    character["Parents"] = "Both Ill"
elif number < 96:
    character["Parents"] = "Parents Lost or Unknown"
else:
    character["Parents"] = "Adoptive or Foster Parents"

number = randrange(1, 101)
if number < 26:
    character["Siblings"] = "No Siblings"
elif number < 46:
    sibs = randrange(1, 5)
    character["Siblings"] = "Oldest (Younger Siblings: %d)" % sibs
elif number < 76:
    sibs1 = randrange(1, 4)
    sibs2 = randrange(1, 4)
    character["Siblings"] = "Middle (Younger Siblings: %d, Older Siblings: %d)" % (sibs1, sibs2)
elif number < 96:
    sibs = randrange(1, 5)
    character["Siblings"] = "Youngest (Older Siblings: %d)" % sibs
else:
    character["Siblings"] = "Twin"

number = randrange(1, 101)
if number < 21:
    character["Grandparents"] = "No Grandparents"
elif number < 31:
    character["Grandparents"] = "Mother's Parents Alive"
elif number < 41:
    character["Grandparents"] = "Father's Parents Alive"
elif number < 61:
    character["Grandparents"] = "One Grandparent on Each Side"
elif number < 71:
    character["Grandparents"] = "Three Grandparents Alive"
elif number < 81:
    character["Grandparents"] = "Great-Grandparent Alive"
else:
    character["Grandparents"] = "Grandparents Unknown"

number = randrange(1, 101)
if number < 11:
    character["Extended Family"] = "None"
elif number < 21:
    character["Extended Family"] = "No Known Relatives"
elif number < 56:
    relatives = randrange(1, 11)
    character["Extended Family"] = "%d Living Relatives" % relatives
elif number < 91:
    relatives = randrange(1, 13)
    relatives = relatives + randrange(1, 13)
    character["Extended Family"] = "%d Living Relatives" % relatives
else:
    character["Extended Family"] = "Huge Extended Family"

number = randrange(1, 101)
if number < 16:
    character["Friends"] = "No Friends"
elif number < 31:
    character["Friends"] = "Lost"
elif number < 51:
    character["Friends"] = "Few"
elif number < 81:
    character["Friends"] = "Some"
else:
    character["Friends"] = "Many"

number = randrange(1, 101)
if number < 16:
    character["Enemies"] = "No Enemies.  Yet..."
elif number < 26:
    character["Enemies"] = "Minor Childhood Enemy"
elif number < 31:
    character["Enemies"] = "Jilted Lover"
elif number < 36:
    character["Enemies"] = "Jilted Lover's Friend or Relative"
elif number < 41:
    character["Enemies"] = "Romantic Rival"
elif number < 51:
    character["Enemies"] = "Enemy of the Family"
elif number < 56:
    character["Enemies"] = "The Enemy of My Friend Is My Enemy"
elif number < 61:
    character["Enemies"] = "Social Rival"
elif number < 66:
    character["Enemies"] = "Villain"
elif number < 71:
    character["Enemies"] = "Monster"
elif number < 76:
    character["Enemies"] = "Alignment Enemy"
elif number < 81:
    character["Enemies"] = "Political Enemy"
elif number < 86:
    character["Enemies"] = "Arcane Rival"
elif number < 91:
    character["Enemies"] = "Diabolic Enemy"
elif number < 96:
    character["Enemies"] = "Enemy Within"
else:
    character["Enemies"] = "Imaginary Foe"

number = randrange(1, 101)
if number < 16:
    character["Instructors"] = "No Instructors of Note"
elif number < 41:
    character["Instructors"] = "Basic"
elif number < 51:
    character["Instructors"] = "Advanced"
elif number < 56:
    character["Instructors"] = "Angry"
elif number < 61:
    character["Instructors"] = "Vanished"
elif number < 66:
    character["Instructors"] = "Favor"
elif number < 81:
    character["Instructors"] = "Unrelated"
elif number < 91:
    character["Instructors"] = "Lower Class"
elif number < 96:
    character["Instructors"] = "Other Race"
else:
    character["Instructors"] = "Exotic"

number = randrange(1, 24)
if number == 1:
	character["Archetype"] = "Agent"
elif number == 2:
	character["Archetype"] = "Challenger"
elif number == 3:
	character["Archetype"] = "Companion"
elif number == 4:
	character["Archetype"] = "Crusader"
elif number == 5:
	character["Archetype"] = "Daredevil"
elif number == 6:
	character["Archetype"] = "Explorer"
elif number == 7:
	character["Archetype"] = "Innocent"
elif number == 8:
	character["Archetype"] = "Leader"
elif number == 9:
	character["Archetype"] = "Martyr"
elif number == 10:
	character["Archetype"] = "Mercentary"
elif number == 11:
	character["Archetype"] = "Orphan"
elif number == 12:
	character["Archetype"] = "Prophet"
elif number == 13:
	character["Archetype"] = "Rebel"
elif number == 14:
	character["Archetype"] = "Renegade"
elif number == 15:
	character["Archetype"] = "Royalty"
elif number == 16:
	character["Archetype"] = "Sage"
elif number == 17:
	character["Archetype"] = "Savage"
elif number == 18:
	character["Archetype"] = "Seeker"
elif number == 19:
	character["Archetype"] = "Simple Soul"
elif number == 20:
	character["Archetype"] = "Strategist"
elif number == 21:
	character["Archetype"] = "Theorist"
elif number == 22:
	character["Archetype"] = "Trickster"
else:
	character["Archetype"] = "Wanderer"

personalityTraits = []
traitNumber = randrange(2, 5)
traits = ["Ambitious", "Angry", "Boastful", "Bold", "Brutal", "Calm", "Carefree", "Charming", "Connected", "Conservative", "Disciplined", "Driven", "Energetic", "Erudite", "Exotic", "Fatalistic", "Flamboyant", "Funny", "Greedy", "Kind", "Loyal", "Merciful", "Naive", "Patriotic", "Peaceful", "Reformed", "Religious", "Serious", "Skilled", "Vengeful"]
while traitNumber > 0:
	number = randrange(0, len(traits))
	trait = traits[number]
	personalityTraits.append(trait)
	traits.remove(trait)
	traitNumber -= 1
personalityTraits.sort()
number = len(personalityTraits)
string = ""
while number > 0:
	trait = personalityTraits[0]
	if number > 1:
		string = string + trait + ", "
	else:
		string = string + trait
	personalityTraits.remove(trait)
	number -= 1
character["Traits"] = string

number = randrange(1, 5)
if number < 3:
    character["Gender"] = "Male"
else:
    character["Gender"] = "Female"

age_dic = {"Human": 15, "Dwarf": 40, "Elf": 110, "Gnome": 40, "Half-Elf": 20, "Halfling": 20, "Half-Orc": 14}
if job in ["Barbarian", "Rogue", "Sorcerer"]:
	if race in ["Human", "Half-Orc"]:
		number = 1
		die = 4
	elif race == "Dwarf":
		number = 3
		die = 6
	elif race in ["Elf", "Gnome"]:
		number = 4
		die = 6
	elif race == "Half-Elf":
		number = 1
		die = 6
	else:
		number = 2
		die = 4
elif job in ["Bard", "Fighter", "Paladin", "Ranger"]:
	if race in ["Human", "Half-Orc"]:
		number = 1
		die = 6
	elif race == "Dwarf":
		number = 5
		die = 6
	elif race in ["Elf", "Gnome"]:
		number = 6
		die = 6
	elif race == "Half-Elf":
		number = 2
		die = 6
	else:
		number = 3
		die = 6
else:
	if race in ["Human", "Half-Orc"]:
		number = 2
		die = 6
	elif race == "Dwarf":
		number = 7
		die = 6
	elif race == "Elf":
		number = 10
		die = 6
	elif race == "Gnome":
		number = 9
		die = 6
	elif race == "Half-Elf":
		number = 3
		die = 6
	else:
		number = 4
		die = 6
result = diceRoll(number, die)
age = age_dic[race] + result
character["Age"] = str(age)
gender = character["Gender"]

result = 0
if race == "Human":
	if gender == "Male":
		base = 58
	else:
		base = 53
	result = diceRoll(2, 10)
elif race == "Dwarf":
	if gender == "Male":
		base = 45
	else:
		base = 43
	result = diceRoll(2, 4)
elif race == "Elf":
	if gender == "Male":
		base = 53
	else:
		base = 53
	result = diceRoll(2, 6)
elif race == "Gnome":
	if gender == "Male":
		base = 36
	else:
		base = 34
	result = diceRoll(2, 4)
elif race == "Half-Elf":
	if gender == "Male":
		base = 55
	else:
		base = 53
	result = diceRoll(2, 8)
elif race == "Half-Orc":
	if gender == "Male":
		base = 58
	else:
		base = 53
	result = diceRoll(2, 12)
else:
	if gender == "Male":
		base = 32
	else:
		base = 30
	result = diceRoll(2, 4)

inches = base + result
quotient = inches / 12
multiple = quotient * 12
difference = inches - multiple
height = "%s ft. %s in." % (quotient, difference)
character["Height"] = height

print "Generated by Nativity in Bits 0.1.4\nSee the Hero Builder's Guidebook (pg. 38) for more information about some of these terms.\n\nAdventurer Statistics"
print "-----------------------------------"
print "Class = " + character["Class"] + ""
print "Race = " + character["Race"] + ""
print "Alignment = " + character["Alignment"] + ""
print "Age = " + character["Age"] + ""
print "Gender = " + character["Gender"] + ""
print "Height = " + character["Height"] + ""
print "Temperature Zone = " + character["Temperature Zone"] + ""
print "Terrain = " + character["Terrain"] + ""
print "Community = " + character["Community"] + ""
print "Family Economic Status = " + character["Family Economic Status"] + ""
print "Family Social Standing = " + character["Family Social Standing"] + ""
print "Family Defense Readiness = " + character["Family Defense Readiness"] + ""
print "Family Private Ethics = " + character["Family Private Ethics"] + ""
print "Family Public Ethics = " + character["Family Public Ethics"] + ""
print "Family Religious Commitment = " + character["Family Religious Commitment"] + ""
print "Family Reputation = " + character["Family Reputation"] + ""
print "Family Political Views = " + character["Family Political Views"] + ""
print "Family Power Structure = " + character["Family Power Structure"] + ""
print "Ancestors of Note = " + character["Ancestors of Note"] + ""
print "Early Childhood Instruction = " + character["Early Childhood Instruction"] + ""
print "Formal Education = " + character["Formal Education"] + ""
print "Learning a Trade = " + character["Learning a Trade"] + ""
print "Early Childhood Events = " + character["Early Childhood Events"] + ""
print "Youth Events = " + character["Youth Events"] + ""
print "Pivotal Events = " + character["Pivotal Events"] + ""
print "Parents = " + character["Parents"] + ""
print "Siblings = " + character["Siblings"] + ""
print "Grandparents = " + character["Grandparents"] + ""
print "Extended Family = " + character["Extended Family"] + ""
print "Friends = " + character["Friends"] + ""
print "Enemies = " + character["Enemies"] + ""
print "Instructors = " + character["Instructors"] + ""
print "Personality Archetype = " + character["Archetype"] + ""
print "Personality Traits = " + character["Traits"] + ""


loop = 1
while loop == 1:
	print "\n\n\nDo you want to save this data?"
	print "\n--Options--"
	print "1. Yes"
	print "2. No\n"
	try:
		selection = input("Make a selection: ")
	except (NameError, SyntaxError):
		print "\nInvalid Selection"
	else:
		if selection is 1 or selection is 2:
			loop = 0
			if selection is 1:
				write_file()
				print '\nData saved in file "adventurer.txt"'
			print "\nShutting down..."
		else:
			print "\nInvalid Selection"
