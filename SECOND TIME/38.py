message = input("> ")
words = message.split(' ')
emojis = {
    ":)": "SMILE",
    ":(": "SAD"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print (output)