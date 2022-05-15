"""
    This project simulates the automatic sending of customized emails using Python
"""

PLACE_HOLDER = "[name]"

# First lets open the names file
with open(r"Input\Names\invited_names.txt", mode="r") as invited_names:
    names = invited_names.readlines()


# Now for the name in the names list lets create a new letter replacing the [name] flag
for name in names:
    # Remove newlines from the name
    stripped_name = name.strip()
    # Now lets connect read the letter too
    with open("Input/Letters/starting_letter.txt", mode="r") as starting_letter:
        content_of_letter = starting_letter.readlines()
    with open(f"Output/ReadyToSend/letter_for_{stripped_name}", mode="w") as customer_letter:
        # Select the name flag from the contents and replace that with the name
        content_of_letter[0] = content_of_letter[0].replace(PLACE_HOLDER, f"{stripped_name}")
        customer_letter.write(" ".join(content_of_letter))
