import sys
import subprocess
import time
import os

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    import requests
except Exception:
    install("requests")

import requests

def progressbar(it, prefix="", size=60, file=sys.stdout):
    count = len(it)
    def show(j):
        x = int(size*j/count)
        file.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "."*(size-x), j, count))
        file.flush()        
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    file.write("\n")
    file.flush()

#for i in progressbar(range(15), "Computing: ", 40):


#getting a file from a GitHub URL
os.system("mkdir Code")
url = "https://raw.githubusercontent.com/apascoa/PY_Tools/main/main.py"
url_reverse = url[::-1]
filename_reverse = url_reverse.split("/")[0]
filename = filename_reverse[::-1]
r = requests.get(url)
Temp = open("./Code/%s" %(filename), 'wb')
Temp.write(r.content)
Temp.close()
input()

main_filename = filename.split(".")[0]

sys.path.insert(1, './Code')
time.sleep(1)
main = __import__(main_filename)
main.test()

input()