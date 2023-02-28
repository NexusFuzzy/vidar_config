import requests
from datetime import date, datetime
import collections
import random

c2 = ["http://65.109.9.93", "2.8", "44695974b686fb6a0820a41ad955f8f2", "0"]

def log(message):
    today = datetime.now()
    print("[" + today.strftime("%d/%m/%Y %H:%M:%S") + "] " + message)
    return
	
def random_string(length):
    return ''.join(random.choice('0123456789ABCDEF') for i in range(length)).lower()
    
    
session = requests.Session()

user_agent = ""

if c2[1] == "2.4":
    log("Setting User-Agent for version 2.4")
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
elif c2[1] == "2.5":
    log("Setting User-Agent for version 2.5")
    user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36"
elif c2[1] == "2.6":
    log("Setting User-Agent for version 2.6")
    user_agent = "Mozilla/5.0 (X11; CrOS x86_64 14685.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4992.0 Safari/537.36"
elif c2[1] == "2.7":
    log("Setting User-Agent for version 2.7")
    user_agent = "Mozilla/5.0 (X11; CrOS x86_64 14685.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4992.0 Safari/537.36"
elif c2[1] == "2.8":
    log("Setting User-Agent for version 2.8")
    user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Mobile/15E148 Snapchat/10.77.0.54 (like Safari/604.1)"
else:
    log("Quitting since no botnet version was specified")
    exit()
            
session.headers = collections.OrderedDict()
session.headers['X-Id'] = c2[2]
session.headers['User-Agent'] = user_agent        
hwid = random_string(21) + "-" + random_string(8) + "-" + random_string(4) + "-" + random_string(4) + "-" + random_string(4) + "-" + random_string(4) + "-" + random_string(12)

log("Firing against botnet " + c2[2] + " through " + c2[0])
answer = session.get(c2[0] + "/", timeout=60)
log("Received status code: " + str(answer.status_code))
log("Config received from C2 server: " + str(answer.text))
