# add your code here
user_sentence = input("Please enter a sentance: ")
user_sentence = user_sentence.lower()

encrypted_sentence = ''

abc_dict = {
    "a": "f", "b": "g", "c": "h", "d": "i", "e": "j",
    "f": "k", "g": "l", "h": "m", "i": "n", "j": "o",
    "k": "p", "l": "q", "m": "r", "n": "s", "o": "t",
    "p": "u", "q": "v", "r": "w", "s": "x", "t": "y",
    "u": "z", "v": "a", "w": "b", "x": "c", "y": "d", "z": "e",
}
for letter in user_sentence:
    if letter in abc_dict:
        lower_ch = letter.lower()
        encrypted_sentence += abc_dict[lower_ch]
    else:
        encrypted_sentence += letter
print("The encrypted sentence is: ", encrypted_sentence)