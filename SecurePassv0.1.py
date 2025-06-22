# Password_Strength_Tester
def Password_Strength_Tester():
    user_password= input("Enter your current Password: ")
        
    def check_length():
        if len(user_password) >= 8:
            return True
        elif len(user_password) < 8:
            return False
    # # ✅ Contains lowercase
    def check_lowercase():
        has_lowercase = any(char.islower() for char in user_password)
        if has_lowercase:
            return True
        else:
            return False
    # ✅ Contains uppercase
    def check_uppercase():
        has_uppercase= any(char.isupper() for char in user_password)
        if has_uppercase:
            return True
        else:
            return False
    # ✅ Contains digits
    def check_digit():
        has_digit = any(char.isdigit() for char in user_password)
        if has_digit:
            return True
        else:
            return False
    # ✅ Contains symbols
    def check_symbols():
        has_symbols = any(not char.isalnum() for char in user_password)
        if has_symbols:
            return True
        else:
            return False

    if check_length() == True :
        print("Your Password have More than 8 chars✅")
    else:
        print("Your Password do not have more than 8 characters❌")
    if check_lowercase() == True:
        print("Your Password have Lowercase letter✅")
    else:
        print("Your Password do not have any Lowercase letter❌")
    if check_uppercase() == True:
        print("Your Password have Uppercase letter✅")
    else:
        print("Your Password do not have any Uppercase letter❌")
    if check_digit() == True:
        print("Your Password have Digit✅")
    else:
        print("Your Password do not have any Digit❌")
    if check_symbols() == True:
        print("Your Password have Symbols✅")
    else:
        print("Your Password do not have any Symbols❌")
    
    score = sum([check_length(),check_lowercase(),check_uppercase(),check_digit(),check_symbols()])
    if score == 5:
       print("\n🟢 Strong Password")
    elif score >= 3:
        print("\n🟡 Moderate Password")
    else:
     print("\n🔴 Weak Password")

def Password_Generator():
#✅ 2. Password Generator
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")
    # Ask user Length of password (8–20):
    type_of_password= input("What Type of Password you want Type E for Easy and Type S for Strong: ").lower()
    nr_letters= int(input("How many letters would you like in your password?\n")) 
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n")) 
    # Easy or Strong (Easy = only letters, Strong = letters+numbers+symbols)
    if type_of_password == "e":
    # Generate and display password.
        password = ""
        #loop to itrate from the list of letters OK?
        for char in range(1, nr_letters+1):
            password+=random.choice(letters)
        for char in range(1, nr_symbols+1):
            password+=random.choice(symbols)
        for char in range(1, nr_numbers+1):
            password+=random.choice(numbers)
        print(password)

    elif type_of_password == "s":
        password_list = []
        for char in range(1, nr_letters+1):
            password_list.append(random.choice(letters))
        for char in range(1, nr_symbols+1):
            password_list.append(random.choice(symbols))
        for char in range(1, nr_numbers+1):
            password_list.append(random.choice(numbers))
        random.shuffle(password_list)
        strong_password=""
        for char in password_list:
            strong_password+= char
        print(f"Your password: {strong_password} ")
    else:
        print("Invalid input")

#Main UI
# Welcome to SecurePass v0.1
print("Welcome to SecurePass v0.1")
while True:
    option = int(input("Choose an option: \n 1. Check Password Strength\n 2. Generate Password \n 3. Exit\n > "))

    if option == 1 :
        Password_Strength_Tester()
    elif option == 2:
        Password_Generator()
    elif option == 3:
         print("Exiting the Script.....")
         break
    else:
        print("Invalid input")
print("----------------")
print("Thanks for Using")




