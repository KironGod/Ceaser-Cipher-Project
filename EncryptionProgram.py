# Python Proram that can encrypt, decrypt, and brute-force using Caesar's cipher
# Authors: Trenton Jones & Darran Clifford
 
import sys

#Function that performs the Caesar cipher encyrption
# Takes in the message and uses the key to encryt
def encrypt(message, key):
    result = ""
    for char in message: # Goes through each character the is in the message provided
        if char.isalpha(): #checks to see if the characters are part of the alphabet
            shift = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift + key) % 26 + shift) #encryption 
        else:
            result += char #keeps any non-alphabetic characters intact
    return result # returns the encrypted results


# decryption function that decrypts using the negative key of the encrypt function.
def decrypt(ciphertext, key):
    return encrypt(ciphertext, -key)

#Brute force function that takes the ciphertext and threshold
def brute_force_crack(ciphertext, threshold):
    #takes in the words from the dictionary file and converts them to lowercase
    dictionary = set(word.strip().lower() for word in open("C:/Users/rosha/OneDrive/Desktop/dictionary.txt"))

     #Goes through all possible keys for the Caesar cipher (26 for the whole alphabet
    for possible_key in range(25):
        decrypted_text = decrypt(ciphertext.lower(), possible_key) #decrypts the ciphertext using possible keys
        decrypted_words = decrypted_text.split() #converts the text into words

        valid_word_count = sum(1 for word in decrypted_words if word in dictionary) # finds the number of valid words in the text
 

        accuracy = valid_word_count / len(decrypted_words)
        #print("Accuracy:", str(accuracy))

         # prints the results of the Brute Forcing
        if accuracy >= threshold:
            print(f"Cracked Text: {decrypted_text}")
            print(f"Used Key: {possible_key}")
            print(f"Accuracy: {accuracy * 100:.2f}%\n")
        else:
            print(f"\nMost likely not the key \nUsed Key: {possible_key}\nText: {decrypted_text}")
            print(f"Accuracy: {accuracy * 100:.2f}%\n")
 

# Fucntion that displays the options for the user
def Welcome():
    print("Options:")
    print("0. Create file")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Brute Force Crack")
    print("4. Exit Program")




#Main method that runs the above methods based on the input from the user
def main():
    Welcome() #prints options for user
    print("\nIf you do not have a file premade to manipulate please use option 0 to create a file.\n")
    choice = input("Enter the option number: ")
    while True:
        if choice == "0": # if user enters "0" a new file will be created where the user can enter contents into the file
            file_path = input("Enter the path of the file to be created: ")
            text_of_file = input("Please enter the contents of the file: ")
            with open(file_path, "w") as fileN: 
                fileN.write(text_of_file)
            with open(file_path, "r") as fileNewR: 
                plaintext = fileNewR.read()
            print("File contents:", plaintext)

        elif choice == "1": # if the user enters "1" it allows for the encryption method to be called.
            input_file = input("Enter the path of the file to be encrypted: ")
            while True: 
                try: 
                    key = int(input("Enter the encryption key (an integer): ")) 
                    break  # Break the loop if the input is a valid integer 
                except ValueError: 
                    print("Invalid input. Please enter an integer for the encryption key.") 
            output_file = input("Enter the path of the output file: ")
            flag = True
            while flag:
                try:
                    with open(input_file, "r") as file: 
                        plaintext = file.read() 
                        ciphertext = encrypt(plaintext, key)
                    flag = False
                except FileNotFoundError:
                    print("File is not found")
                    input_file = input("Enter the path of the file to be encrypted: ")

 

            print("Encrypted Text:", ciphertext)

            with open(output_file, "w") as file:
                file.write(ciphertext) 


  

        elif choice == "2": 
            # Takes in a file as input
            input_file = input("Enter the path of the file to be decrypted: ") 

            while True: 
  
                try: 
                    key = int(input("Enter the encryption key (an integer): ")) 
                    break  # Break the loop if the input is a valid integer 
                except ValueError: 
                    print("Invalid input. Please enter an integer for the encryption key.") 
  
            output_file = input("Enter the path of the output file: ") 
  
            flag = True # flag created in order to continuously reprompt the user and check for exceptions
            while flag: 
                try:
                    with open(input_file, "r") as file: 
                        ciphertext = file.read() 
                        decrypted_text = decrypt(ciphertext, key)
                    flag = False # flag is false if the program successfully locates the file else it reprompts the user
                except FileNotFoundError:
                    
                    print("File is not found")
                    input_file = input("Enter the path of the file to be decrypted: ")


            print("Decrypted Text:", decrypted_text) 

  

            with open(output_file, "w") as file: 

                file.write(decrypted_text) 

  

        elif choice == "3": 

            input_file = input("Enter the path of the file to be cracked: ")

            while True: 
  
                try:
                    threshold = float(input("Enter the accuracy threshold (0 to 1): "))
                    if threshold > 0 and threshold <= 1:
                        break  # Break the loop if the input is a valid integer else remprompt the user
                    else:
                        print("That is not a number between 0 and 1. Please try again")  
                except ValueError: 
                    print("Invalid input. Please enter a float for the encryption key.") 

            flag = True
            while flag:
                try:
                    with open(input_file, "r") as file:
                        ciphertext = file.read()
                    flag = False # flag is false if the program successfully locates the file else it reprompts the user
                except FileNotFoundError:
                    print("File is not found")
                    input_file = input("Enter the path of the file to be cracked: ")

           


            result = brute_force_crack(ciphertext,threshold) 
            
            print(result)

        elif choice == "4":
            print("Thank you for using my program!")
            sys.exit()
        else: 
            # Catches if user doesnt enter a number between 0-4
            print("Invalid option. Please choose 0, 1, 2, 3, or 4.")  

        print()          
        Welcome()
        choice = input("Enter the option number: ") 
        
    

         

        

if __name__ == "__main__": 

    main() 
