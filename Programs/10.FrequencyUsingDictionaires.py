#Frequency using dictionaries
frequencies={}
text=input("Enter a text: ")
for i in text:
    if i!=" ":
        frequencies[i]=frequencies.get(i,0)+1
print("Character frequencies:")
for character, count in frequencies.items():
    print(character, ":", count)