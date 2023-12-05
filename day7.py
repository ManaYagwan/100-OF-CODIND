#def greet (name,location):
 #   print(f"hey {name}")
  #  print(f"how are you {name} what is it like in {location}")
    #print("today")
#name = input("whats ur name ? ")
#location = input(f"{name} so where do you stay ? ")
#greet(name,location)

import math

#def paint_cal (height,width,cover):
 ##   num_of_can1 =round( (height * width) /cover)
   # num_of_can =math.ceil((height * width)/cover)
    #print(f"u need this {num_of_can1} amont of can")
    #print(f"u need this {num_of_can} amont of can")
#test_h = int(input())
#test_w = int(input())
#coverage = 5
#paint_cal(height=test_h,width=test_w,cover=coverage)
#def prime_check (number):
    

#n = int(input())
#prime_check(number=n)
alphabet = [ " ",'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s'
           ,'t','u','w','x','y','z'," ",'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s'
           ,'t','u','w','x','y','z']
number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

sign = ['@', '<', '>', '?', '#', '&', '$', '£', '!']




def caeser (type_text,shift_num,order):
   meg = ""
   if direction == "decode":
      shift_num *= -1
   for char in text:
      if char in alphabet:
        position = alphabet.index(char)
        nw_position = position + shift_num
        new_latter = alphabet[nw_position]
        meg += new_latter
      else :
        meg += char
   print(f"the {direction} message is {meg}")

condition = True
while condition:
  direction=input("type 'encode' to encrypt and 'decode' to decrypt : ")
  text = input(f"whats the message you would {direction} : ").lower()
  shift = int(input("whats the shift number ? "))
  shift = shift % 26

  caeser(type_text=text,shift_num=shift,order=direction)
  ask = input("type yes if you want to go again else no : ").lower()
  if ask == "no":
     condition = False
     print("goodbye")
# def encrypt (type_text,shift_num) :
#     msg = ""
#     for latter in text:
#         position = alphabet.index(latter)
#         nw_position = position + shift_num
#         new_latter = alphabet[nw_position]
#         msg += new_latter
#     print(f"the encode message is {msg}")

# def decrypt (type_text,shift_num) :
#     msge = ""
#     for latter in text:
#         position = alphabet.index(latter)
#         nw_position = position - shift_num
#         new_latter = alphabet[nw_position]
#         msge += new_latter
#     print(f"the {direction} message is {msge}")
    
# if direction == "encode" :
#   encrypt(type_text=text,shift_num=shift)
# elif direction == "decode" :
#   decrypt(type_text=text,shift_num=shift)