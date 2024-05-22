import os
import requests
from bs4 import BeautifulSoup

def get_imgs_from_page(url):
        try:
        # * realizar la peticion GET a la url.
                initial_response = requests.get(url);

        # * Extraer el contenido de la pagina en un html.
                html_page = BeautifulSoup(initial_response.text, features="html.parser")

        # * obtener todas las etiquetas <a>
                etiquetas_img = html_page.find_all('img', src=True)

        # * Crear la carpeta para guardar las imagenes
                if not os.path.exists("imgs"):
                        os.mkdir("imgs")

        # * Obtener los src de las etiquetas img y verificar que tengan el formato adecuado.
                for img in etiquetas_img:
                        if img["src"].startswith("http") and img["src"].endswith(".jpg") or img["src"].endswith(".png") or img["src"].endswith(".webp"):
                                # * Descargar las imagenes dandoles un nombre unico
                                imagen = requests.get(img["src"]).content

                                # * Crear la ruta completa para guardar la imagen en la carpeta "imgs"
                                img_name = img["src"].split('/')[-1]
                                img_path = os.path.join("imgs", img_name)
                                with open(img_path, 'wb') as handler:
	                                handler.write(imagen)

        except Exception as e:
                print(f"Ocurrió un error: {e}")
        
# * URL de prueba
url = "https://www.mercadolibre.com.ar/c/autossryksrudrrhejetjetjethg-motos-y-otros#menu=categories"

# * llamdo a la funcion
get_imgs_from_page(url)