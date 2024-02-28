from app.service.posts.post import obtener_posts, crear_post, actualizar_post, eliminar_post
from app.service.photos.photo import obtener_photos
from string import Template

def app():
    
    #Ejemplo photos.........
    
    mis_photos = obtener_photos(cantidad=5)
    #print(mis_photos)
    
    
    img_template = Template('<img src="$url" />')
    # imagen = img_template.substitute(url = "hola mundo")
    html_template = Template('''
                             <!DOCTYPE html>
                                <html lang="en">
                                <head>
                                    <meta charset="UTF-8">
                                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                                    <title>Document</title>
                                </head>
                                <body>
                                    <h1>Asociación de Amantes de los pájaros de Chile</h1>
                                    $body
                                </body>
                                </html>
                             ''')
    
    #print([photo["url"] for photo in mis_photos])
    lista_urls = [photo["url"] for photo in mis_photos]
    texto_img = ""
    for url in lista_urls:
        texto_img += img_template.substitute(url = url) + "\n"
    
    #print(texto_img)
    html = html_template.substitute(body = texto_img)
    print(html)