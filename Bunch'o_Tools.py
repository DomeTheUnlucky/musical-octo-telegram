import random
import pyfiglet

#Variables 
phone_number1 = ["385+ ", "950+ "]

number_of_phone1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

number_of_phone2 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

number_of_phone3 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

number_of_phone4 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

number_of_phone5 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

number_of_phone6 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

number_of_phone7 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

number_of_phone8 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

number_of_phone9 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

rand_phone_number1 = random.choice(phone_number1)

rand_number_of_phone1 = random.choice(number_of_phone1)

rand_number_of_phone2 = random.choice(number_of_phone2)

rand_number_of_phone3 = random.choice(number_of_phone3)

rand_number_of_phone4 = random.choice(number_of_phone4)

rand_number_of_phone5 = random.choice(number_of_phone5)

rand_number_of_phone6 = random.choice(number_of_phone6)

rand_number_of_phone7 = random.choice(number_of_phone7)

rand_number_of_phone8 = random.choice(number_of_phone8)

rand_number_of_phone9 = random.choice(number_of_phone9)

names = ["David", "Anthony", "John", "Dominik"]

scnd_names = [" Boca", " Smith", " James"]

rand_names = random.choice(names)

rand_scnd_names = random.choice(scnd_names)


print ("This is an Concept Version Of 'The Bunch of tools pack'")

ascii_text = pyfiglet.figlet_format("Bunch Of Tools 0.2")
print(ascii_text)


print ("Fake Credentials = 1")
print ("Fake Phone Number = 2")
selection = input("Select an tool: ")

if selection is "2":
	print(rand_phone_number1 + rand_number_of_phone1 + rand_number_of_phone2 + rand_number_of_phone3 + rand_number_of_phone4 + rand_number_of_phone5 + rand_number_of_phone6 + rand_number_of_phone7 + rand_number_of_phone8 + rand_number_of_phone9)
	


if selection is "1":
	print(rand_names + rand_scnd_names)


	

	


    

  

        





