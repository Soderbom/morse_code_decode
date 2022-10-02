from bs4 import BeautifulSoup as bs
import requests
import sys
import json

# Dot 183
# Dash 8722
# Trash space 32 8202

url = "https://en.wikipedia.org/wiki/Morse_code"
morse_page = requests.get(url)

if morse_page.status_code != 200: sys.exit(1)

soup = bs(morse_page.content, 'html.parser')
bolds = list(soup.find_all("td"))

alpha_to_morse = {}
morse_to_alpha = {}

for i, bold in enumerate(bolds):
    if "Letters" in bold.get_text():
        alpha = bolds[i+1].get_text()[0]
        morse = bolds[i+2].find('b').get_text().replace(chr(183), '.').replace(chr(8722), '-').replace(chr(32), '').replace(chr(8202), '')

        alpha_to_morse[alpha] = morse
        morse_to_alpha[morse] = alpha

with open("alpha_to_morse.json", 'w') as f:
    json.dump(alpha_to_morse, f)


with open("morse_to_alpha.json", 'w') as f:
    json.dump(morse_to_alpha, f)
