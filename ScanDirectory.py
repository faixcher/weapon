import requests
import sys

if len(sys.argv) < 2 :
    print("usage <ip> <wordlists>")
    sys.exit(1)

sub_list = open(sys.argv[2]).read()
print("path wordlists :",sys.argv[2])
directories = sub_list.splitlines()

for dir in directories :
    dir_enum = f"http://{sys.argv[1]}/{dir}.html"
    print(dir_enum)
    r = requests.get(dir_enum)
    if r.status_code==404:
        pass
    else:
        print("Valid Directory:",dir_enum)
