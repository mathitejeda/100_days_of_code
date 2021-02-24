import pandas

NATO_df = pandas.read_csv("nato_phonetic_alphabet.csv")
NATO_alphabet = {row.letter: row.code for (index, row) in NATO_df.iterrows()}

def generate_phonetic():
    word = input("Write a name to create your phonetic code words list: ").upper()
    try:
        PCW = [NATO_alphabet[letter] for letter in word]
    except KeyError:
        print("Sorry, you can only type letters")
        generate_phonetic()
    else:
        print(PCW)

generate_phonetic()