from string import Template

def generate_image_html(bird):
    img_template = Template('<p>$name</p><img src="$url" alt="$name">')
    url = bird['images']['main']
    name = bird['name']['spanish'] + ' - ' + bird['name']['english']
    return img_template.substitute(url=url, name=name)

def generate_html_page(birds):

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

    images = [generate_image_html(bird) for bird in birds]
    html = html_template.substitute(body='\n'.join(images))
    return html 
