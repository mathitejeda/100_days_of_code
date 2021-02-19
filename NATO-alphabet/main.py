import pandas

NATO_df = pandas.read_csv("nato_phonetic_alphabet.csv")
NATO_alphabet = {row.letter: row.code for (index, row) in NATO_df.iterrows()}


word = input("Write a name to create your phonetic code words list: ").upper()

PCW = [NATO_alphabet[letter] for letter in word]
print(PCW)