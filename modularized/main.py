from api_utils import get_bird_data
from html_generator import generate_html_page

birds_api_url = 'https://aves.ninjas.cl/api/birds'

bird_data = get_bird_data(birds_api_url)

if bird_data:
    html = generate_html_page(bird_data)

    with open("aves_chile.html", "w") as html_file:
        html_file.write(html)

    print("Archivo HTML actualizado/creado > aves_chile.html")
else:
    print("Error fetching bird data.")
