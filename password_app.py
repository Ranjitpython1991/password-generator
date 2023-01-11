# eight digit password with a fixed count
import re
import random  
import string

def get_string(letters_count, digits_count,punctuation_count):
    letters = ''.join((random.choice(string.ascii_letters) for i in range(letters_count)))
    digits = ''.join((random.choice(string.digits) for i in range(digits_count)))
    punctuation = ''.join((random.choice('!@#$%^&*') for i in range(punctuation_count)))
    
    # Convert resultant string to list and shuffle it to mix letters and digits
    sample_list = list(letters + digits+punctuation)
    random.shuffle(sample_list)
    # convert list to string
    password = ''.join(sample_list)
    if len(password) < 8 :     # check the length
        return "length_error" 
    elif re.search(r"\d", password) is None :  # searching for digits
        return "digit_error"
    elif re.search(r"[A-Z]", password) is None : # searching for uppercase
        return "uppercase_error"
    elif re.search(r"[a-z]", password) is None : # searching for lowercase
        return  "lowercase_error"
    else :
        #return password
        print(password)

get_string(6,1,1)