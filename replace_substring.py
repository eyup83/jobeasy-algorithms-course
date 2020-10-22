str1 = input("Enter a string : ")
ch = input("Enter a character : ")
newchar = input("Enter a new character : ")

str2 = ''
for i in range(len(str1)):
    if str1[i] == ch:
        str2 = str2 + newchar
    else:
        str2 = str2 + str1[i]

print("Original String :  ", str1)
print("New String :  ", str2)
