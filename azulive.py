import requests
import argparse

contact="""
Developer:
https://github.com/rdkalopsia
https://mebroccoli.blogspot.com
"""
Banner="""
   _____                  .____     .__                
  /  _  \  ________ __ __ |    |    |__|___  __  ____  
 /  /_\  \ \___   /|  |  \|    |    |  |\  \/ /_/ __ \ 
/    |    \ /    / |  |  /|    |___ |  | \   / \  ___/ 
\____|__  //_____ \|____/ |_______ \|__|  \_/   \___  >
        \/       \/               \/                \/                              
"""
print(Banner)
print(contact)
print("Scanning in progress:")
# ANSI escape codes
RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"

abc = argparse.ArgumentParser(description="AzuLive, A tool to filter active domains")
abc.add_argument("-l", "--list", help="Path to the file containing the list of domains", required=True)
abc.add_argument("-o", "--output", help="Output file for the active domains", required=True)
abc.add_argument("-i", "--include", type=int, default=[200, 301, 302, 403, 500], help="Status codes considered as active [-i 200 300 XXX]. (default 200 301 302 403 500)", nargs="+")

bcd = abc.parse_args()

subdomain = open(bcd.list, "r")
aktifdomain = open(bcd.output, "a+")

for baris in subdomain:
    baris = baris.strip("\n")
    baris = baris.strip()
    if not (baris.startswith("http://") or baris.startswith("https://")):
        baris = "http://" + baris
    try: 
            statuskode = requests.get(baris,timeout=6)
            if  statuskode.status_code in bcd.include:
                print(baris, GREEN,statuskode.status_code,RESET,"->", GREEN+"added to the output file"+RESET)
                aktifdomain.write(baris + "\n")
            else:
                print(baris, RED,statuskode.status_code,RESET)

    except Exception:
            print(baris,RED,"cannot accessed",RESET)
            continue
    except KeyboardInterrupt:
            print("KeyboardInterrupt, program has stopped")
            break
subdomain.close()
aktifdomain.close()
