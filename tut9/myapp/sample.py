from  tut9.myapp.dics import roll_dics
import requests


def guess_number(num):
    result=roll_dics()
    if result==num:
        return "You won!"
    else:
        return "You lost!"
    
def get_ip():
    responce=requests.get("https.get://httpbin.org/ip")
    if responce.status_code==200:
        return responce.json()['origin']