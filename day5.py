letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","s","T","U","V","W"
           ,"X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s"
           ,"t","u","w","x","y","z"]

number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

sign = ['@', '<', '>', '?', '#', '&', '$', '£', '!']

import random
ask = input("would you like us to suggest a password for you : ")
if ask == "yes" :
    num_letter = random.randint(6, 9)
    num_number = random.randint(3,5)
    num_sign = random.randint(2,8)

    password = []

    for char in range(1 , num_letter+1) :
        password+=random.choice(letters)

    for char in  range(1, num_number+1) :
        password+=random.choice(number)

    for char in range(1, num_sign+1) :
        password+=random.choice(sign)

    random.shuffle(password)

    passwrd = ""
    for char in password :
        passwrd+=char

    print(passwrd)
else :
    print("ok")