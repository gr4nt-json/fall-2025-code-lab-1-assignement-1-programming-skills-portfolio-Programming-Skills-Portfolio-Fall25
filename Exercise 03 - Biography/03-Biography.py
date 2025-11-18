Biography = {
  "Name": input("Enter your name: "),#Asks for the users name
  "Hometown": input("Enter your hometown: "),#Asks for the users hometown
  "Age": input("Enter your age: ")#Asks for the users age
}
print(*Biography.items(), sep="\n")

'''Explanation for print(*Biography.items(), sep="\n")

 .items() = gives you all the "key:value" pairs in the dictionary
 * = "unpacks" all the pairs in the dictionary
 sep="\n" = changes the default separator (" ") to "\n" (tells python to "go to the next line")
'''