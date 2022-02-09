#Work By APascoa
#https://github.com/apascoa/

# ---- Main Imports
import sys
import subprocess
import time
import os

# ---- Colored Text
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# ---- Functions 
def clearConsole():
    command = 'cls' if os.name in ('nt', 'dos')  else "clear"
    os.system(command)  
 
def test_import(packge,packge_install=""):
    packge_install = packge if packge_install == "" else packge_install
    try:
        __import__(packge)
    except Exception:
        print(bcolors.WARNING+"Python Module '%s' Not Instaled"%(packge)+bcolors.ENDC)
        subprocess.check_call([sys.executable, "-m", "pip", "install", packge_install])
    globals()[packge] = __import__(packge)
    if packge not in sys.modules:
        print(bcolors.WARNING+"Python Module '%s' Failed to Import"%(packge)+bcolors.ENDC)
        print(bcolors.WARNING+"Exiting"+bcolors.ENDC)
        quit()
    else:        
        print(bcolors.OKCYAN+"Python Module '%s' Imported Successfully"%(packge)+bcolors.ENDC)

#getting a file from a GitHub URL
def file_import(url,location="./"):
    url_reverse = url[::-1]
    filename_reverse = url_reverse.split("/")[0]
    filename = filename_reverse[::-1]
    filename = filename.split("?")[0]
    r = requests.get(url)
    Temp = open("%s%s" %(location,filename), 'wb')
    Temp.write(r.content)
    Temp.close()
    return filename

# ---- Clear Console
clearConsole()
print("               AAA               PPPPPPPPPPPPPPPPP        AAA                  SSSSSSSSSSSSSSS         CCCCCCCCCCCCC     OOOOOOOOO                   AAA\n              A:::A              P::::::::::::::::P      A:::A               SS:::::::::::::::S     CCC::::::::::::C   OO:::::::::OO                A:::A\n             A:::::A             P::::::PPPPPP:::::P    A:::::A             S:::::SSSSSS::::::S   CC:::::::::::::::C OO:::::::::::::OO             A:::::A\n            A:::::::A            PP:::::P     P:::::P  A:::::::A            S:::::S     SSSSSSS  C:::::CCCCCCCC::::CO:::::::OOO:::::::O           A:::::::A\n           A:::::::::A             P::::P     P:::::P A:::::::::A           S:::::S             C:::::C       CCCCCCO::::::O   O::::::O          A:::::::::A\n          A:::::A:::::A            P::::P     P:::::PA:::::A:::::A          S:::::S            C:::::C              O:::::O     O:::::O         A:::::A:::::A\n         A:::::A A:::::A           P::::PPPPPP:::::PA:::::A A:::::A          S::::SSSS         C:::::C              O:::::O     O:::::O        A:::::A A:::::A\n        A:::::A   A:::::A          P:::::::::::::PPA:::::A   A:::::A          SS::::::SSSSS    C:::::C              O:::::O     O:::::O       A:::::A   A:::::A\n       A:::::A     A:::::A         P::::PPPPPPPPP A:::::A     A:::::A           SSS::::::::SS  C:::::C              O:::::O     O:::::O      A:::::A     A:::::A\n      A:::::AAAAAAAAA:::::A        P::::P        A:::::AAAAAAAAA:::::A             SSSSSS::::S C:::::C              O:::::O     O:::::O     A:::::AAAAAAAAA:::::A\n     A:::::::::::::::::::::A       P::::P       A:::::::::::::::::::::A                 S:::::SC:::::C              O:::::O     O:::::O    A:::::::::::::::::::::A\n    A:::::AAAAAAAAAAAAA:::::A      P::::P      A:::::AAAAAAAAAAAAA:::::A                S:::::S C:::::C       CCCCCCO::::::O   O::::::O   A:::::AAAAAAAAAAAAA:::::A\n   A:::::A             A:::::A   PP::::::PP   A:::::A             A:::::A   SSSSSSS     S:::::S  C:::::CCCCCCCC::::CO:::::::OOO:::::::O  A:::::A             A:::::A\n  A:::::A               A:::::A  P::::::::P  A:::::A               A:::::A  S::::::SSSSSS:::::S   CC:::::::::::::::C OO:::::::::::::OO  A:::::A               A:::::A\n A:::::A                 A:::::A P::::::::P A:::::A                 A:::::A S:::::::::::::::SS      CCC::::::::::::C   OO:::::::::OO   A:::::A                 A:::::A\nAAAAAAA                   AAAAAAAPPPPPPPPPPAAAAAAA                   AAAAAAA SSSSSSSSSSSSSSS           CCCCCCCCCCCCC     OOOOOOOOO    AAAAAAA                   AAAAAAA\n")

# ---- Extra Imports
test_import("yaml","pyyaml")
test_import("requests")

# ---- Base Config File
config_base = [
    {
        'Amount' : '1',
        'URL_0': "",
    }
]

# ---- Create Config File
if not os.path.isfile('./config.yaml'):
    print(bcolors.WARNING+"Config File Does Not Exist"+bcolors.ENDC)
    with open("config.yaml", 'w') as yamlfile:
        data = yaml.dump(config_base, yamlfile, sort_keys = True)
        print(bcolors.OKCYAN+"Config File Created Successfully"+bcolors.ENDC)

# ---- Create Main Code Folder
if not os.path.isdir('./Code'):
    os.system("mkdir Code")

with open("config.yaml", "r") as yamlfile:
    config_data = yaml.load(yamlfile, Loader=yaml.FullLoader)
    config_data = dict(config_data[0])
    if config_data["URL_0"] == "":
        print(bcolors.WARNING+"Config File Does Not Have The URL's"+bcolors.ENDC)
        quit()
    else:
        print(bcolors.OKGREEN+"Config File Loaded Successfully"+bcolors.ENDC)

filename =file_import(config_data["URL_0"],"./Code/")
main_filename = filename.split(".")[0]

for i in range(1,int(config_data["Amount"])):
    file_import(config_data["URL_"+str(i)],"./Code/")

print("\n\n\n")

sys.path.insert(1, './Code')
time.sleep(1)

__import__(main_filename)
