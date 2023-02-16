#Password Generator Project
import random
#Making the lists of the letters, numbers, symbols i will use
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

#Inputing the number of letters, symbols and numbers i want to use in my random password
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
#Taking a random char (as i want) from each list 
letters_i_will_use = random.choices(letters, k=nr_letters)
symbols_i_will_use = random.choices(symbols, k=nr_symbols)
numbers_i_will_use = random.choices(numbers, k=nr_numbers)
#I got the number of all thing in this line of code 
numbers_of_all_letters = nr_letters + nr_symbols + nr_numbers
#I got the password without without randomness here
password_list = letters_i_will_use + symbols_i_will_use + numbers_i_will_use
#Here I put a String variable to use it on the loop and make the password as one word
password = ""
#This loop will make the password in one word without randomness as i said
for password_loop in password_list: 
    password += " " + password_loop
#The password without randomness as is ready but with spaces and u will know why in the next comment
password_without_randomistion = password  
#Now the password is almost ready but its on list 
password_letters_list = password_without_randomistion.split()
#Here i do something like shuffle for all char to random the password in every thing
final_password_in_list = random.choices(password_letters_list, k=numbers_of_all_letters)
#Here I put a String variable to use it on the loop and make the password as one word (same to old password)
final_password = ""
#I put the random letters on this variable
for letter in final_password_in_list:
    final_password += letter
#And yeah the password is ready 
print(final_password)

#IDK if this is the best way to make a random password but put this in ur mind 
#i programmed this cute programe in 1 hour and just in 6 days of learning python
#u can use my code when u want and as u need not matter with me but
#Program Developed buy Brimo Battaro :O

