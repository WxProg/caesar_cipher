#Importing modules needed in program
import art
from replit import clear

# Introduction of program
print(art.logo)
print("Hello General! The camp has been inflitrated.")
print("Use this cipher to communicate with our allies.")

restart_program = True

while restart_program: 
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x','y', 
     'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    condition = True
    list_of_decision = ["encrypt", "decrypt"]
    e = "encryption"
    while condition:
        #Informs the user if input is invalid
        decision = input("\nWould you like to 'encrypt' or 'decrypt'?\n")   
        if decision in list_of_decision:
            text = input("\nType your message:\n").lower()
            shift = int(input("\nType the shift number:\n"))
            condition = False
        else:
            print("Invalid input. Try again!")
        #Defining the function    
        def caesar(text, shift, decision):
            clear()
            final_text = " "
            if decision == "decrypt":
                shift *= -1
            for char in text:
                if char not in alphabet:
                    final_text += char
                else:
                    current_postion = alphabet.index(char)
                    new_position = current_postion + shift    
                    final_text += alphabet[new_position]
            print(f"The {decision}ed text is:{final_text}\n")
            # Informs the user whether encrypted word is weak or strong.
            if decision == "encrypt":
                if len(final_text) <= 6:
                    print(f"Weak {decision}ion. Message maybe easily intercepted.\n")
                else:
                    print(f"Strong {decision}ion. Message will be hard to intercept.\n")
            
    caesar(text, shift, decision)

    #Prompts the user if the program should run again.
    if input("Would you like to restart cipher? 'Yes' or 'No' \n").lower() == "yes":
        restart_program = True
    else:
        restart_program = False
        print("Program terminated. Good Bye. ")
 
