# Day 24 – Mail Merge
# This script automates the creation of personalized letters
# by replacing a placeholder name in a template letter.

# TODO:
# - Read a starting letter template
# - Read a list of invited names
# - Replace the [name] placeholder with each actual name
# - Save each personalized letter into the ReadyToSend folder

with open("./Input/Letters/starting_letter.txt") as letter:
    # Read the entire content of the template letter
    letter_content = letter.read()

with open("./Input/Names/invited_names.txt") as names:
    # Read all names into a list (each line is one name)
    invited_names = names.readlines()

    # Loop through each name to generate a personalized letter
    for name in invited_names:
        # Remove newline characters and extra spaces
        format_name = name.strip()

        # Create a new file for each recipient
        with open(
            f"./Output/ReadyToSend/letter_for_{format_name}",
            mode="w"
        ) as invite_letter:

            # Replace the placeholder with the actual name
            format_letter = letter_content.replace("[name]", format_name)

            # Write the personalized letter to a new file
            invite_letter.write(format_letter)
