# main module
import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)

def caesar(text_, shift_, direction_):
    text_2 = ""
    if shift_ > len(alphabet):
        shift_ = shift_ % (len(alphabet))
    if direction_ == "decode":
        shift_ *= -1
    for letter in text_:
        if letter in alphabet:
            position = alphabet.index(letter)
            if position < (len(alphabet) - shift_):
                 new_position = position + shift_
            else:
                x = len(alphabet) - position
                for n in range(1, shift_+1):
                    if x == n:
                        new_position = shift_ - n
            text_2 += alphabet[new_position]
        else: 
            text_2 += letter 
            
    print(f"Here's the {direction_}d text:\n{text_2}")

end_of_loop = False
while end_of_loop == False:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text_=text, shift_=shift, direction_=direction)
    check = input("Do you want to restart the cipher program?(yes/no): ")
    if check != "yes":
        end_of_loop = True
        print("Have a nice day.")


