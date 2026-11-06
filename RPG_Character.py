'''
User Requirements for Character Creation System
===============================================

The user must enter a character name.

The character name must be a text value (string).

The character name cannot be empty.

The character name should not exceed 10 characters.

The character name should not contain spaces.

The user must provide values for Strength, Intelligence, and Charisma.

All stat values must be whole numbers (integers).

Each stat must have a minimum value of 1.

Each stat must have a maximum value of 4.

The total points allocated to Strength, Intelligence, and Charisma must equal exactly 7.

If any requirement is violated, the system should display an appropriate error message.

If all requirements are satisfied, the system should create the character successfully.

The system should display the character name.

The system should visually represent Strength using filled and empty dots.

The system should visually represent Intelligence using filled and empty dots.

The system should visually represent Charisma using filled and empty dots.

The character sheet should be displayed in a readable format containing the name and all three stats.

'''

full_dot = '●'
empty_dot = '○'

def create_character(character_name,strength,intelligence,charisma):

# First checked the condition for the name of the character which include is that 'string',
# has more than 10 characters, is it empty or have space in the name
    if type(character_name) != str:
        return "The character name should be a string"
    if character_name == "":
        return 'The character should have a name'
    if len(character_name) > 10:
        return 'The character name is too long'
    if " " in character_name:
        return "The character name should not contain spaces"
# Now checks is the stats follows the nesaccary condition
    if not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int):
        return "All stats should be integers"
    if strength < 1 or intelligence < 1 or charisma < 1 :
        return "All stats should be no less than 1"
    if strength > 4 or intelligence > 4 or charisma > 4 :
        return "All stats should be no more than 4"
    if strength + intelligence + charisma != 7:
        return 'The character should start with 7 points'
# Then it has to returns the character name and stats if they follows all the criterias
    return (
        character_name + "\n" +
        "STR " + full_dot * strength + empty_dot * (10 - strength) + "\n" +
        "INT " + full_dot * intelligence + empty_dot * (10 - intelligence) + "\n" +
        "CHA " + full_dot * charisma + empty_dot * (10 - charisma)
        )
print(create_character("rex",2,4,1))