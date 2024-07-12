import random

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceaser(text, shift):
    encrypted_text = [] # make a list for the encrypted text
    for char in text: # for each character in text 

        if char in alphabet: # if char is in alphabet
            index = alphabet.index(char) # then we assign index to the index for the char
        if direction == "decode":
            new_index = (index - shift) % 26 # we get a new index by using index and adding shift 
        elif direction == "encode":
            new_index = (index + shift) % 26  

        encrypted_text.append(alphabet[new_index]) # then we append the alphabet at new index to the encrypted list and the we join it and print it

    print(''.join(encrypted_text))

ceaser(text, shift)











