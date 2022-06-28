from pakuri import Pakuri
import gettext
import os

localedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'locale')
translate = gettext.translation('pakudex', localedir, fallback=True)
_ = translate.gettext


__author__ = "Jaxton \"Collected-em-all\" Willman"

# Goal is to get a valid menu option out of this
def menu_handler():
	# Main menu
	while True:
		menu_string_en = _(
			"\nPakudex Main Menu\n"
			"-----------------\n"
			"1. List Pakuri\n"
			"2. Show Pakuri\n"
			"3. Add Pakuri\n"
			"4. Remove Pakuri\n"
			"5. Change Pakuri Level\n"
			"6. Exit\n"
		)

		print(menu_string_en)

		menu_selection = input(_("What would you like to do? "))
		print("")

		# Check menu
		match menu_selection:
			case "1" | "2" | "3" | "4" | "5" | "6" | "Change Language" | "69":
				return menu_selection
			case _:
				print(_("Unrecognized menu selection!"))


def find_pakuri(pakudex, pakuri_name):
	# Check Pakuri existence
	for idx, pakuri in enumerate(pakudex):
		if pakuri.name == pakuri_name:
			return idx
	return -1


# Option 1
def list_pakuri(pakudex):
	# Check if Pakudex is empty
	if len(pakudex) == 0:
		print(_("No Pakuri in Pakudex yet!"))
		return -1 # Return to menu

	# List Pakuri in Pakudex
	print(_("Pakuri in Pakudex:"))
	for idx, pakuri in enumerate(pakudex):
		print(_("{}. {} ({}, level {})").format(idx+1, pakuri.name, pakuri.species, pakuri.level))


# Option 2
def show_pakuri(pakudex):
	# Ask which Pakuri
	pakuri_name = input(_("Enter the name of the Pakuri to display: "))

	# If pakuri doesn't exist return to the main menu
	pakuri_idx = find_pakuri(pakudex, pakuri_name)
	if pakuri_idx == -1:
		print(_("Error: No such Pakuri!"))
		return -1 # Return to menu
	
	pakuri = pakudex[pakuri_idx]
	print(_("\nName:"), pakuri.name)
	print(_("Species:"), pakuri.species)
	print(_("Level:"), pakuri.level)
	print(_("CP:"), pakuri.cp)
	print(_("HP:"), pakuri.hp)


# Option 3
def add_pakuri(pakudex):
	print(_("Pakuri Information\n------------------"))

	name = input(_("Name: "))

	# Check if Pakuri already exists in Pakudex
	if find_pakuri(pakudex, name) != -1:
		print(_("Error: Pakudex already contains this Pakuri!"))
		return -1 # Return to menu

	# Pakudex doesn't contain this new Pakuri, let's get the rest of the details
	species = input(_("Species: "))

	# Keep asking for level if you give bad answers
	while True:
		level = input(_("Level: "))

		# Pakuri level Error handling
		try:
			level = int(level)
		except:
			print(_("Invalid level!"))
			continue
		
		if level < 0:
			print(_("Level cannot be negative."))
		elif level > 50:
			print(_("Maximum level for Pakuri is 50."))
		else:
			break

	# Create and add Pakuri
	pakuri = Pakuri(name, species, level)
	pakudex.append(pakuri)
	pakudex.sort()

	print(_("\nPakuri {} ({}, level {}) added!").format(pakuri.name, pakuri.species, pakuri.level))


# Option 4
def remove_pakuri(pakudex):
	pakuri_name = input(_("Enter the name of the Pakuri to remove: "))

	# If pakuri doesn't exist return to the main menu
	pakuri_idx = find_pakuri(pakudex, pakuri_name)
	if pakuri_idx == -1:
		print(_("Error: No such Pakuri!"))
		return -1 # Return to menu
	
	# Remove Pakuri
	pakudex.pop(pakuri_idx)
	print(_("Pakuri {} removed.").format(pakuri_name))


# Option 5
def change_pakuri_level(pakudex):
	# Ask which Pakuri
	pakuri_name = input(_("Enter the name of the Pakuri to change: "))

	# If pakuri doesn't exist return to the main menu
	pakuri_idx = find_pakuri(pakudex, pakuri_name)
	if pakuri_idx == -1:
		print(_("Error: No such Pakuri!"))
		return -1 # Return to menu
	
	pakuri = pakudex[pakuri_idx]

	# Keep asking for level if you give bad answers
	while True:
		# We found the Pakuri! Ask what level to set it to
		new_level = input(_("Enter the new level for the Pakuri: "))

		# Error handling
		try:
			new_level = int(new_level)
		except:
			print(_("Invalid level!"))
			continue
		
		if new_level < 0:
			print(_("Level cannot be negative."))
		elif new_level > 50:
			print(_("Maximum level for Pakuri is 50."))
		else:
			pakuri.level = new_level
			break


# Option 6
def pakudex_quit():
	print(_("Thanks for using Pakudex: Let's Go! Bye!"))


# Option "Change Language"
def pakudex_change_language():
	print(_("Available languages:"))
	print(
		"1. English\n"
		"2. 日本国\n"
		"3. Pig Latin\n"
		"4. Klingon\n"
		"5. Xhosa\n"
		"6. Austrailian\n"
	)

	language_selection = input(_("Please select a language: "))

	# Check selection
	match language_selection:
		case "1" | "English":
			language_selection = "English"

		case "2" | "日本国":
			language_selection = "日本国"

		case "3" | "Pig Latin":
			language_selection = "Pig Latin"

		case "4" | "Klingon":
			language_selection = "Klingon"

		case "5" | "Xhosa":
			language_selection = "Xhosa"

		case "6" | "Austrailian":
			language_selection = "Austrailian"
		case _:
			print(_("\nUnrecognized language selection!\n"))
	
	return language_selection


def main():
	# Initialize Pakudex
	language = "English"
	pakudex = []

	print(_("Welcome to Pakudex: Let's Go!"))

	menu_selection = 0

	while True:
		menu_selection = menu_handler()

		match menu_selection:
			case "1":
				list_pakuri(pakudex)

			case "2":
				show_pakuri(pakudex)

			case "3":
				add_pakuri(pakudex)

			case "4":
				remove_pakuri(pakudex)

			case "5":
				change_pakuri_level(pakudex)

			case "6":
				pakudex_quit() # Display quit message
				break # Breaks the while loop to quite the program

			case "Change Language":
				language = pakudex_change_language() # We need to be mindful of international audiences

			case "69":
				print("Nice!")





if __name__ == "__main__":
	main() # Call main function