import requests
import json
from string import Template

def request_get(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


birds_api_url = 'https://aves.ninjas.cl/api/birds'
response = request_get(birds_api_url)

if response: 
    html_template = Template('''<!DOCTYPE html>
    <html>
    <head>
    <title>Aves de Chile</title>
    </head>
    <body>
    <h1>Aves de Chile</h1>
    $body
    </body>
    </html>
    ''')

    img_template = Template('<p>$name</p><img src="$url" alt="$name">') 

    images = []
    for bird in response:
        url = bird['images']['main']
        name = bird['name']['spanish'] + ' - ' + bird['name']['english']
        images.append(img_template.substitute(url=url, name=name))

    html = html_template.substitute(body='\n'.join(images))
    print(html)
else:
    print("Error fetching bird data.")

with open("aves_chile.html", "w") as html_file:
    html_file.write(html)

print("Archivo HTML actualizado/creado > aves_chile.html")

