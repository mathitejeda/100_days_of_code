invited_names = []
with open("Input/Names/invited_names.txt") as names:
    invited_names = names.read().splitlines()
print(invited_names)

for name in invited_names:
    with open("Input/Letters/starting_letter.txt") as starting_letter:
        with open(f"Output/ReadyToSend/{name}_letter.txt", mode='w') as final_letter:
            text = starting_letter.read()
            text = text.replace("[name]",name)
            final_letter.write(text)
