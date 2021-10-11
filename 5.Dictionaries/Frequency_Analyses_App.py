from collections import Counter

#Dictionaries Challenge 224: Frequency Analysis App

print("Welcome to the Frequency Analysis App")

non_letters = ['1','2','3','4','5','6','7','8','9','0',' ',
'.','?','!',',','"',"'",':',';','(',')','%','$','&','#','\n','\t']
# getting key_phrase_1
key_phrase_1 = input("Enter a phrase:")

number_letters = len(key_phrase_1)
for n in range(1,number_letters):
    new_change = key_phrase_1.replace(" ","",n)

for m in new_change:
    if m in non_letters:
        new_change = new_change.replace(m, "",n)

total_occurrences = len(new_change)
letter_count =  Counter(new_change)

sum_up = sum(letter_count.values())

print("\n\nHere is the frequency analysis from key phrase 1: ")
print("\n\t Letter \t\tOccurrence \t\t Percentege: ")
for x, y in sorted(letter_count.items()):
    ret1 = round(float(y / sum_up * 100), 2)
    print("\t\t" + str(x)+"\t\t"+str(y) + "\t\t\t\t"+str(ret1)+"%")
print("Letters ordered from highest occurence to lowest: ")
order_letter_count = letter_count.most_common()
g = dict(order_letter_count)
key_phrase_1_ordered_letters = []
for x in g.keys():
    print(x,end=";")

key_phrase_2 = input("\nEnter a phrase:")

number_letters = len(key_phrase_2)
for n in range(1,number_letters):
    new_change = key_phrase_2.replace(" ","",n)
for m in new_change:
    if m in non_letters:
        new_change = new_change.replace(m, "",n)
total_occurrences = len(new_change)
letter_count =  Counter(new_change)
sum_up = sum(letter_count.values())
print("\n\nHere is the frequency analysis from key phrase 2: ")
print("\n\t\t Letter \t\t\tOccurrence \t\t\t Percentege: ")
for x, y in sorted(letter_count.items()):
    ret1 = round(float(y / sum_up * 100), 2)
    print("\t\t\t" + str(x)+"\t\t\t\t\t"+str(y) + "\t\t\t\t\t\t"+str(ret1)+"%")
print("Letters ordered from highest occurence to lowest: ")
order_letter_count = letter_count.most_common()
g = dict(order_letter_count)
key_phrase_2_ordered_letters = []
for x in g.keys():
    print(x,end=";")