



# what is the Rot 13 encryption algorithem 
#  is letter substitution cipher algorithem 
# for each letter in the alphabet has a numeric position (1- 26 )
# for exemple A has position 1 and Z has position 26 


#replaces each word with the 13 th letter after is 
# After p greater than 26 letters reset tp p-26 



#for Decrytion 
# you can subtract 13 from the an alphabet postion 
# if the value is negative then subtract absolute value of it from 26 
# and this is done this is the right value of the text 

import string
def rot13_translator() -> dict:

    lowercase : str = string.ascii_lowercase
    uppercase : str = string.ascii_uppercase 
 
    shift = 13 

    shift_lowercase : str = lowercase[shift:] + lowercase[:shift]
    shift_uppercase : str = uppercase[shift:] + uppercase[:shift]


    translator : dict = str.maketrans(lowercase + uppercase , shift_lowercase + shift_uppercase )
    return translator 

    print(shift_lowercase)
    

def rot13(message : str ) -> str :
    table : dict = rot13_translator()
    return message.translate(table)



def main() -> None : 
    user_input : str = input ("Your message :")

    encrypted_message : str = rot13(user_input)
    print(f'Encrypted Message : {encrypted_message}')

   
if __name__ == '__main__': 
    
    x = rot13_translator()
    print(len(x))
    print(x)

    main()


