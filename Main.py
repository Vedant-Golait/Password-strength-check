import string
# ---------------Creating a password store file----------

password = "password.txt"
password_input = input("Enter your password: ")

with open (password, "w") as f:
    f.write(password_input)


# Count no. of upper_case, lower_case, special characters & digits

upper_case = sum(1 for c in password_input if c in string.ascii_uppercase)
lower_case = sum(1 for c in password_input if c in string.ascii_lowercase)
special = sum(1 for c in password_input if c in string.punctuation)
digits = sum(1 for c in password_input if c in string.digits)

# Store the count in list
Capital = [upper_case]
Small = [lower_case]
Symbol = [special]
number = [digits]
length = len(password_input)


# Initial Score
score = 0

# checks password in the common password list
with open (r"common_pass_list.txt", "r", encoding=  "utf-8") as f:
    common = f.read().splitlines()
if password_input in common:
    print("Password was found in common password directory, can be cracked easily using a dictionary attack \n password score = 0")
    exit()



# Length Points
if length > 7:
    score += 1
if length > 12:
    score += 1


# Capital Letters  Points
if sum (Capital) > 1:
    score += 1
if sum(Capital)>2:
    score += 1

# Small Letters  Points
if sum (Small) > 1:
    score += 1
if sum(Small)>2:
    score += 1

# Digits
if sum (number) > 1:
    score += 1
if sum(number)>2:
    score += 1

# Special characters
if sum (Symbol) > 1:
    score += 1
if sum(Symbol)>2:
    score += 1


# Final result print
print (f"Your password has length of {len(password_input)} and has {str (sum(Capital))} capital  letters, {str (sum(Small))} Small letters, {str (sum(Symbol))} Symbols & {str (sum(number))} digits ")
if score  < 5:
    print (" Its a week pasword , can be cracked easily using a Bruteforce attack. \n Your score =", score, " /10")

elif score >= 5 and score  < 7:
    print ("It is a medium password , can be cracked using a customized Bruteforce attack. \n Your score =", score, " /10")
elif score > 7:
    print ("It is a strong password. \n Your score =", score, " /10")
