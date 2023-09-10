import random
import time
import requests
def random_sum():#side effect
    a=random.randint(1,10)
    b=random.randint(1,7)
    return a+b

def silly():#multiple mock patch
    params={"timestamp":time.time(),
            "number":random.randint(1,6)
            }
    
    responce=requests.get("https://httpbin.org/get",params)
    if responce.status_code==200:
        return responce.json()['args']

    