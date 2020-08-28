import urllib
import requests

print("downloading with requests")
url = 'http://download.redis.io/releases/redis-5.0.5.tar.gz'
r = requests.get(url)
with open("exec.exe", "wb") as code:
    code.write(r.content)
