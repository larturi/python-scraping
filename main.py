import os
from titles import *
from transcript import *

FOLDER_PATH_OUTPUT = 'transcripts'

# Creo la carpeta de los transcripts
os.mkdir(FOLDER_PATH_OUTPUT)

# Recorro las paginas 1 a 10
for page_id in range(1, 11):
    # Obtengo las urls de cada pelicula
    links = get_titles(page_id)
    # Obtengo el texto de cada pelicula
    for link in links:
        get_transcript(link)