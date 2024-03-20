from PIL import Image
import os

def thumbnail_generator(imagen_path, tamano=(50,50), salida_path=None):
    imagen = Image.open(imagen_path)
    imagen.thumbnail(tamano)
    if salida_path:
        imagen.save(salida_path)
    return imagen

ruta_absoluta = os.path.abspath("test\imagen.jpg")
miniatura = thumbnail_generator(ruta_absoluta, salida_path="miniatura_output.jpg")