import time
import requests

print("downloading with requests")
url = 'https://www.baidu.com'
r = requests.get(url)
name=time.strftime("%Y%m%d%H%M")+".exe"
with open(name, "wb") as code:
    code.write(r.content)
