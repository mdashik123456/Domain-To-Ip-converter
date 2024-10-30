# Domain to IP Converter

A simple Python tool to convert a domain name to its IP address. This tool uses Python's `socket` library and enhances the output with text styling for better readability.

## Features

- Converts a domain name to its corresponding IP address.
- Stylish output using the `pyfiglet` and `termcolor` libraries.
- Handles invalid domain names gracefully with an error message.

## Installation

1. **Clone this repository:**

   ```bash
   git clone https://github.com/mdashik123456/Domain-To-Ip-converter.git
   cd domain-to-ip-converter

2. **Installing Packages**

         pip3 install -r requirements.txt
   
## Usage
      python3 main.py

## Output

```plaintext
 ____                        _         _____       ___ ____  
|  _ \  ___  _ __ ___   __ _(_)_ __   |_   _|__   |_ _|  _ \ 
| | | |/ _ \| '_ ` _ \ / _` | | '_ \    | |/ _ \   | || |_) |
| |_| | (_) | | | | | | (_| | | | | |   | | (_) |  | ||  __/ 
|____/ \___/|_| |_| |_|\__,_|_|_| |_|   |_|\___/  |___|_|    
                                                             

coded by 0xF0tRes



Enter domain name (eg: google.com): google.com
The IP Address is: <google ip>`
```

## Error Handling
If an invalid domain is entered, the tool will display:
```plaintext
Invalid domain name or domain is not found!!
```
