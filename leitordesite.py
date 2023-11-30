from gtts import gTTS
import pygame
import requests
from bs4 import BeautifulSoup
import os

def reproduzir_audio(texto):
    tts = gTTS(text=texto, lang='pt-br')
    tts.save("temp.mp3")
    pygame.mixer.init()

    pygame.mixer.music.load("temp.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    os.remove("temp.mp3")

url = 'https://www.poder360.com.br/internacional/lula-recebera-brasileiros-que-estavam-na-faixa-de-gaza/'

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

texto_web = soup.get_text()

if texto_web.strip():
    print(texto_web)

    reproduzir_audio(texto_web)
