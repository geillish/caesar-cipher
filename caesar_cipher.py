def decyptor(offset_remainder,user_message):
  decrypted_message = ""
  for letter in range(len(user_message)):
    new_message = user_message[letter:letter+1]
    unicode = ord(new_message)
    if unicode == 32:
      unicode = chr(unicode)
      decrypted_message = decrypted_message + unicode
    else:
      unicode = unicode - offset_remainder
      if unicode < 65:
        unicode = unicode + 26
        unicode = chr(unicode)
        decrypted_message = decrypted_message + unicode
      else:
        unicode = chr(unicode)
        decrypted_message = decrypted_message + unicode
  return decrypted_message

user_message = "placeholder"

while user_message != "":
  print()

  user_message = input("Please enter a message to decrypt?\n")
  
  print() 
  
  offset = int(input("Please enter an offset?\n"))
  
  offset_remainder = offset%26
  
  print()
  print(decyptor(offset_remainder,user_message))
