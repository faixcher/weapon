import requests
import sys # for use sys.argv[0]
'''
if len(sys.argv) < 2:
    print("Usage: python script.py <base_domain>")
    sys.exit(1)
'''

sub_list = open("/home/fais/Downloads/wordlist2.txt").read()
subdoms = sub_list.splitlines() #splitlines() get line to array 

# base_domain = sys.argv[1]
base_domain = sys.argv[1] if len(sys.argv) > 1 else "example.com"
for sub in subdoms:
	sub_domains = f"http://{sub}.{base_domain}"

	try:
		requests.get(sub_domains)
		 

	except requests.ConnectionError:
         pass
        
	else: # if not error of exception 
		print("valid domain: ",sub_domains)
