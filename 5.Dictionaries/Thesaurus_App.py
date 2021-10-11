import random
from collections import Counter
#Dictionaries Challenge 21: Thesaurus App

thesaurus = {
    'hot':['balmy','summery','tropical','boiling','scorching'],
    'cold':['chilly','cool','freezing','frigid','polar'],
    'happy':['content','cheery','merry','jovial','jocular'],
    'sad':['unhappy','downcast','miserable','glum','melnacholy']

}
print("Welcome to the Thesaurus App")

print("\n\n Choose a word from the thesaurus and I will give you a synonym.")
print("\nHere are the words in the thesaurus: ")
for key in thesaurus.keys():
    print("\t-"+key)
word = input("What word would you like a synonym for: ").lower()

value1 = thesaurus[word]
random_value = random.choice(value1)
print("A synonym for "+str(word)+" is "+str(random_value))

whole_dict = input("Would you like to see the whole thesaurus (yes/no): ").lower()
if whole_dict == "yes":
    for key,value in thesaurus.items():
        print("\n"+str(key).title()+" synonyms are: ")
        print("\t-"+str(value))
        for x in value:
            print("\t- "+str(x))
elif whole_dict=="no":
    print("\nI hope you enjoyed the program. Thank you!")
else:
    print("You've type sth wrong man... Let's bail bustard!")