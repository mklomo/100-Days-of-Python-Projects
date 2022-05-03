# """
#     This Python Program implements Caesar's Cipher Encryption
# """

# Importing relevant modules

import string

import art_work

print(art_work.logo)

print("\n")

alphabet = list(string.ascii_lowercase)


# # Creating a function called encrypt that takes 'text' and 'shift' as inputs

# def encrypt(text, shift):
    
#     # Shift each letter of text forwards in the alphabet list by the shift amount and print the encrypted text
    
    
#     encrypted_list = ""

#     # Check the index of the first letter in the text
#     for each_char in text:
#         # Check the position of the letter in alphabet
#         position = alphabet.index(each_char)

#         # Add the shift to the position
#         encrypted_position = shift + position
        
#         # If the encrypted position > 26
#         if encrypted_position > 25:
#             encrypted_position = encrypted_position - 26
        
#         # Append the encrypted_list with the encrypted_letter
#         encrypted_list += alphabet[encrypted_position]

#     # Lets transform the encrypted list to a string
#     encrypted_message = "".join(encrypted_list)

#     return(encrypted_message)


# def decrypt(text, shift):

#     # Reverse the shift applied to the text

#     # Initialize the decrypted text
#     decrypted_text = "" 

#     # Loop through the encrypted text and reverse it
#     for each_char in text:
#         # Determine the index of each_char in alphabets
#         position = alphabet.index(each_char)

#         # Reversing the position index with the shift
#         decrypted_position = position - shift  

#         # If the decrypted_position is < 0 , then shft to 25
#         if decrypted_position < 0:
#             decrypted_position = decrypted_position + 26       

#         # The decrypted text
#         decrypted_text += alphabet[decrypted_position]

#     return(decrypted_text)

# # Determining the direction of the code
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

# if direction == "encode":
#     text = (input("Type the message you want to encrypt:\n"))

#     shift = int(input("Type the shift number:\n"))

#     enc_message = encrypt(text=text, shift=shift)
#     print(f"The encrypted message is {enc_message}")

# elif direction == "decode":
#     text = (input("Type the message you want to encrypt:\n"))

#     shift = int(input("Type the shift number:\n"))

#     dec_message = decrypt(text=text, shift=shift)

#     print(f"The decrypted message is {dec_message}")



def caesar(text, shift, direction):
    encrypted_text = ""
    
    # What if shift > 26
    if shift > 26:
        shift %= 26

    # Direction of shift

    if direction == "decode":
        shift *= -1
    
    # Check the index of the first letter in the text
    for each_char in text:

        # Check if it is a each_char is a letter
        if each_char in alphabet:
        
            # Check the position of the letter in alphabet
            position = alphabet.index(each_char)
        
            new_position = shift + position

            # If the encrypted position > 26
            if new_position > 25:
                new_position = new_position - 26
        
            elif new_position < 0:
                new_position = new_position + 26

               
            # Concatenate the encrypted message with the encrypted_letter
            encrypted_text += alphabet[new_position]
        
        else:
            encrypted_text += each_char 

    return(encrypted_text)



# While Condition trigger
should_continue = "yes"

while should_continue == "yes":
    text_in = (input("Type your message here:\n"))

    shift_in = int(input("Type the shift number:\n"))

    direction_in = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    
    message = caesar(text=text_in, shift=shift_in, direction=direction_in)

    print(message)

    should_continue = input("Do you want to restart the cipher program? Yes or No \n").lower()

    if should_continue != "yes":
        print("Goodbye")
