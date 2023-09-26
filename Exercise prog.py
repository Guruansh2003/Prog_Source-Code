# firstWord  = "7"
# secondWord = "8"
# print(firstWord + secondWord)

# Examples using string . format() 
#phrase = "Welco0me to the jungle, {0}. We've got fun and {1}. my fave number is {2:, .2f} dollars."
phrase = "Welcome to the jungle, {0: .2f}. We've got fun and {1}"
name = input("Please enter your name: ")
noun = input("Enter a noun: ")
thirdWord = "yoyo"
#print(phrase, name "puppy" , "kitty") 
# #Concatenating using multiple arguments in the print command, separated by commas
myNumber = (-34534577.10, 2)
#Example using string.format()
print(phrase.format(name, noun, myNumber))

