letter_contents=None
names=None



with open("Input/Names/names_to_invite.txt") as flip:
    contents=flip.readlines()
    names=contents



with open("Input/Letters/letter.txt") as filp:
    contents=filp.read()
    letter_contents=contents
    for name in names:
        stripped_name=name.strip()
        new_letter=letter_contents.replace("[name]",stripped_name)
        with open(f"Output/Ready_To_send/letter_for_{stripped_name}.txt", "w") as filp:
            filp.write(new_letter)





