#Domain to ip converter

import socket
import pyfiglet
from termcolor import colored

banner = colored(pyfiglet.figlet_format("Domain To IP"), "cyan")
print(f"{banner}")
print(colored("coded by 0xF0tRes", "light_red"))
print("\n\n")

try:
    domain_name = input("Enter domain name (eg: google.com): ")

    #Get domain name from ip address
    ip = socket.gethostbyname(domain_name)

    print(f"The IP Address is: {ip}")
except:
    print( colored("Invalid domain name or domain is not found!!", "red"))  # If the domain name is invalid, print an error message