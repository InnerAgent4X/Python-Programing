


result = ""  
    
print("Welcome")

# asks the user if they want to encode, decode, or quit
while True:
    print("=" * 20)
    user_command = input("Would you like to Encode or Decode or Quit? Please enter E or D or Q :")
    #formats the user input to be uppercase to make it a little harder to mess up.
    Command = user_command.upper()
        
    if Command == "E":
        text = input("Enter the text to be encrypted. : ")
        while True:
            try:
                shift = int(input("Enter the shift value. : "))
                    
                #takes each charater in the string and adds the shift value to its ordinal number
                for char in text:
                    if char.isalpha():
                        base = ord('A') if char.isupper() else ord('a')
                        result += chr((ord(char) - base + shift) % 26 + base)
                    else:
                        result += char
                    
                print(f"The encoded message is : {result}")
                result = ""
                break
            
            #input validation            
            except ValueError:
                    print("please enter the shift value as an Integer.")
                
                
    elif Command == "D":
        text = input("Enter the text to be decrypted. : ")
        while True:
            try:
                shift = int(input("Enter the shift value. : "))
                
                #takes each charater in the string and subtracts the shift value to its ordinal number    
                for char in text:
                    if char.isalpha():
                        base = ord('A') if char.isupper() else ord('a')
                        result += chr((ord(char) - base - shift) % 26 + base)
                    else:
                        result += char
                    
                print(f"The decoded message is : {result}")
                result = ""
                break
                        
            except ValueError:
                    print("please enter the shift value as an Integer.")
            
    #closes the loop and leaves the program    
    elif Command == "Q":
        print("Good Bye!")
        break
            
    else:
        print("Invalid Command.")


