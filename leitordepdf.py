from gtts import gTTS
import pygame
import fitz
import os
import string

def reproduzir_audio(texto):
    tts = gTTS(text=texto, lang='pt-br')

    texto_sem_pontos = texto.translate(str.maketrans('', '', string.punctuation))

    tts.save("temp_sem_pontos.mp3")

    pygame.mixer.init()
    pygame.mixer.music.load("temp_sem_pontos.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    os.remove("temp_sem_pontos.mp3")

livro = open('/home/julio/Downloads/ohomem.txt', 'rb')
pdf = fitz.open(livro)
paginas = pdf.page_count

print(f'Total de páginas: {paginas}')

for pagina_atual in range(paginas):
    pagina = pdf[pagina_atual]
    texto = pagina.get_text()

    if texto.strip():
        print(texto)
        reproduzir_audio(texto)

pdf.close()
