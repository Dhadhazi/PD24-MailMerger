with open("Input/Names/invited_names.txt") as names:
    name_list = names.readlines()

with open("Input/Letters/starting_letter.docx") as file:
    letter_text = file.read()
    for name in name_list:
        letter = letter_text.replace("[name]", name.strip())
        with open(f"Output/ReadyToSend/{name}.docx", mode="w") as wfile:
            wfile.write(letter)


#TODO: Create a letter using starting_letter.docx
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp