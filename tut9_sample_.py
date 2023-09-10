from tut9_dice import rolll_dice
import requests
def guess_number(num):
    result=rolll_dice()
    if result==num:
        return "You won!"
    
    else:
        return "You lost!"
    
def grt_ip():
    url = 'https://api.ipify.org?format=json'
    responce=requests.get(url)
    if responce.status_code==200:
        return responce.json()["ip"]
