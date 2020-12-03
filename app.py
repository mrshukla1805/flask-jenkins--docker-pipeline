from flask import Flask

import random
import array

app = Flask(__name__)

@app.route('/')
def hello():
    
    max_len = 20

    dig = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    lcase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',  
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 
                     'z']

    ucase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',  
                     'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 
                     'Z']

    sym = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',  
           '*', '(', ')']

    comb = dig + lcase + ucase

    rand_digit = random.choice(dig)
    rand_upper = random.choice(ucase)
    rand_lower = random.choice(lcase)
    rand_symbol = random.choice(sym)

    tpass = rand_digit + rand_upper + rand_lower + rand_symbol 

    for x in range(max_len-4):
        tpass = tpass + random.choice(comb)


    tpass2 = list(tpass)
    random.shuffle(tpass2)

    password = ''.join(tpass2)

    print(password)

    return password



if __name__ == '__main__':
    app.run()

