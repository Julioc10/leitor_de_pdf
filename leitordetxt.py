from gtts import gTTS
import pygame
import os

def reproduzir_audio(texto):
    tts = gTTS(text=texto, lang='pt-br')
    tts.save("temp_sem_pontos.mp3")

    pygame.mixer.init()
    pygame.mixer.music.load("temp_sem_pontos.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    os.remove("temp_sem_pontos.mp3")

txt_file_path = '/home/julio/Downloads/ohomem.txt'

with open(txt_file_path, 'r', encoding='utf-8') as file:
    texto = file.read()

    if texto.strip():
        print(texto)
        reproduzir_audio(texto)
