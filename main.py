# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

print("Welcome to our basic Anagram detector!!!\n\n")
print("The detecore can handle single word-and-anagram pairs like; below:elbow, study:dusty")
print("And multiple word pairs like; Bad credit:Debit card.")
print(" It also has the functionality to process words of different cases.\n\n")
print("Though the program does not have the capability to check the inputted words against a dictionary. This will be included in future versions")

is_running = True

while is_running:
    # Get the word and its anagram as input from the user
    input_word = input("Please input your word here: ")
    input_anagram = input("Input the anagram of the above inputted word here: ")


    def find_anagram(word, anagram):
        # [assignment] Add your code here
    
        # Make the word and anagram all lower case and remove all the spaces
        lower_word = word.lower()
        lower_anagram = anagram.lower()
        

        clean_word = lower_word.strip()
        stripped_anagram = lower_anagram.strip()

        plain_word = clean_word.replace(" ", "")
        plain_anagram = stripped_anagram.replace(" ", "")


        sorted_word = ''.join(sorted(plain_word))  
        sorted_anagram = ''.join(sorted(plain_anagram))
    

        if sorted_word == sorted_anagram:
            return True
        else:
            return False

    try:
        print(find_anagram(input_word, input_anagram))

    except:
        print("Wrong input entered")
        is_running = False


    choice = input("Would uou like to try again? \n [y/n]:")

    if choice == "y":
        pass

    elif choice == "n":
        print("Thanks for using our anagram detector")
        is_running = False
