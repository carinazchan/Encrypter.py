'''
FUNCTIONS
'''
#Function START: Makes encryption dictionary from mapping file.
#Parameters: file name.
def build_dictionary(mapping_file):
    mapping_file = open(mapping_file,"r") #Open mapping_file, read mode.
    encryption_dict = dict() #Initialize encryption_dict with empty dictionary.
    org_list = [] #Initialize org_list with empty list.
    new_list = [] #Initialize new_list with empty list.
    char_num = 0 #Initialize char_num with 0.

    #For-loop: loops through each line in mapping_file.
    for line in mapping_file:
        current_line_list = line.split() #Converts each line into a list of
                                        #letters, white space not included.
        for letter in current_line_list: #For-loop: loops through each letter in
                                        #the list, current_line_list.
            char_num += 1 #Incrementing char_num by 1 -> keep track of the
                            #letter in the current iteration.
            if char_num%2 != 0: #If char_num is an odd number -> if iteration is
                                #on first letter in list.
                org_list += letter #Adding on the current letter to org_list.
            else: #If char_num is an even number -> if iteration is on second
                    #letter in list.
                new_list += letter #Adding on the current letter to new_list.

    index_num = 0 #Initialize index_num with 0.
    #For-loop: loops through letters in org_list.
    for letter in org_list:
        encryption_dict[letter] = new_list[index_num] #Adding on key-value pair
                                                    #to encryption_dict.
        index_num += 1 #Incrementing index_num by 1 -> move to the next letter
                        #in new_list.
    mapping_file.close()
    return(encryption_dict)
#Function STOP.

#Function START: Encrypts text from a file and tranfers to a new file.
#Parameters: file name, dictionary.
def encrypt(user_file, encryption_dict):
    user_file = open(user_file,"r") #Open user_file, read mode.
    encrypted_file = open("Encrypted.txt","w") #Open encrypted_file, write mode.

    #For-loop: loops through each line in user_file.
    for line in user_file:
        num_char = len(line) #Initialize num_char with length of line.
        current_char_num = -1 #Initialize current_char_num with -1.

        #For-loop: loops through each character in the line.
        for char in line:
            current_char_num += 1 #Incrementing current_char_num by 1 -> keep
                                #track of the character in the current iteration.
            if current_char_num != num_char: #If it hasn't iterated through all
                                            #the characters in the line yet.
                if char.isalpha(): #If the character is a letter.
                    print(encryption_dict[char], end="", file=encrypted_file)
                    #^Writes the corresponding letter from encryption_dict
                    #to encrypted_file, ending on the same line.
                else: #If the character is NOT a letter.
                    print(char, end="", file=encrypted_file)
                    #^Writes the character to encrypted_file, ending on the same
                    #line.
    user_file.close()
    encrypted_file.close()
#Function STOP.

#Function START: Decrypts text from the encrypted file and transfers to a new
#file.
#Parameters: file name, dictionary.
def decrypt(encrypted_file, encryption_dict):
    encrypted_file = open(encrypted_file,"r") #Open encrypted_file, read mode.
    unencrypted_file = open("Unencrypted.txt","w") #Open unencrypted_file, write
                                                    #mode.

    #For-loop: loops through each line in encrypted_file.
    for line in encrypted_file:
        num_char = len(line) #Initialize num_char with length of line.
        current_char_num = -1 #Initialize current_char_num with -1.

        #For-loop: loops through each character in the line.
        for char in line:
            current_char_num += 1 #Incrementing current_char_num by 1 -> keep
                                #track of the character in the current iteration.
            if current_char_num != num_char: #If it hasn't iterated through all
                                            #the characters in the line yet.
                if char.isalpha(): #If the character is a letter.

                    #For-loop: loops through each key in encryption_dict.
                    for key in encryption_dict:
                        if char == encryption_dict[key]: #If the character is
                                                        #same as the value.
                            print(key, end="", file=unencrypted_file)
                            #^Writes the key to unencrypted_file, ending on the
                            #same line.
                else: #If the character is NOT a letter.
                    print(char, end="", file=unencrypted_file)
                    #^Writes the character to unencrypted_file, ending on the
                    #same line.
    encrypted_file.close()
    unencrypted_file.close()
#Function STOP.

'''
MAIN PROGRAM
'''
#Asks for user input for file name.
user_file = input("Please input a file name: ")

encryption_dict = build_dictionary("Replace.txt") #encryption_dict assigned with
                                                #output from build_dictionary.
encrypt(user_file, encryption_dict) #Execute encrypt function.
decrypt("Encrypted.txt", encryption_dict) #Execute decrypt function.

print("The program is finished running! :D")
