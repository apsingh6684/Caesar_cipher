from art import logo
print(logo)
print("Developed by Anubhav\n")

rerun = True
while rerun == True:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction == "encode":
        text = input("Enter your message which is need to be encrypt.\n").lower()
    elif direction == "decode":
        text = input("Enter message which is need to be decrypt.\n").lower()
    else:
        print("Invalid input entered.\nStart again.")
        import sys
        sys.exit()

    shift = int(input("Type the shift number:\n"))
    while shift > 25:
        shift -= 26
        
    # encoding seprate function
    '''def encrypt(txt, sft, alpha):
        cipher_text = ""
        for letter in txt:
            is_letter_prsnt = letter in alpha
            if is_letter_prsnt == False:
                cipher_text += letter
            else:
                ind_in_alpha = alpha.index(letter)
                shift_ind = ind_in_alpha + shift
                if shift_ind > 25:
                    shift_ind -= 26
                cipher_text += alpha[shift_ind]
        print(cipher_text)'''

    # decoding seprate function
    '''def decrypt(txt, sft, alpha):
        og_message = ""
        for letter in txt:
            is_letter_prsnt = letter in alpha
            if is_letter_prsnt == False:
                og_message += letter
            else:
                ind_in_alpha = alpha.index(letter)
                shifted_ind = ind_in_alpha - sft
                if shifted_ind < 0:
                    shifted_ind += 26
                og_message += alpha[shifted_ind]
        print(og_message)'''

    # combined encoding and decoding function.
    def caesar(txt, sft, alpha, direct):
        final_text = ""
        for letter in txt:
            is_letter_prsnt = letter in alpha
            if is_letter_prsnt == False:
                final_text += letter
            else:
                ind_in_alpha = alpha.index(letter)
                if direct == "encode":
                    shifted_ind = ind_in_alpha + sft
                    if shifted_ind > 25:
                        shifted_ind -= 26
                elif direct == "decode":
                    shifted_ind = ind_in_alpha - sft
                    if shifted_ind < 0:
                        shifted_ind += 26
                final_text += alpha[shifted_ind]
        print(f"Output is in next line\n{final_text}")
        
    caesar(text, shift, alphabet, direction)
    ask_rerun = input("Do you want to re-start it. ('Yes' or 'No')\n").lower()
    if ask_rerun == "yes":
      rerun = True
    elif ask_rerun == "no":
      rerun = False
      print("Thank you for using this tool.\nGood Bye.")
    else:
      rerun = False
      print("Invalid input entered.")
      print("Thank you for using this tool.\nGood Bye.")