import pygame

pygame.init()
# Use OGG em vez de MP3
pygame.mixer.music.load("ex05mp.mp3")  
pygame.mixer.music.play()

# Mantém rodando
while pygame.mixer.music.get_busy():
    pygame.time.wait(1000)