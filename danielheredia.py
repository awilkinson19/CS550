def userloop():
  print("Please enter a molecular formula. (Eg. H2O for water)")
  userget = input('>>> ')
  for i in userget:
    # Method from StackOverflow - https://stackoverflow.com/questions/15558392/how-to-check-if-character-in-string-is-a-letter-python
    if i.isalpha() == 1:
      print(i + " is an element!")
    elif i.isdigit() == 1:
      print(i + " is a quantity!")
    elif "(" in i:
      print("Charge notation detected!")
    elif ")" in i:
      print("Charge notation finished!")
    else:
      print(i + " is neither an element nor a quantity!")
  print(userget[userget.find("(")+1 : userget.find(")")])
  userloop()

userloop()