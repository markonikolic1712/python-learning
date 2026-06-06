#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names = []
with open("./Input/Names/invited_names.txt") as f:
    n = f.readlines()
    for name in n:
        names.append(name.strip()) # strip() se koristi da bi se uklonio \n (novi red)

for name in names:
    with open("./Input/Letters/starting_letter.txt") as f:
        text = f.read().replace("[name]", name)

    print(f"Kreira se fajl za: {name}")
    with open(f"./Output/ReadyToSend/letter_for_{name}", mode="w") as w:
        w.write(text)
