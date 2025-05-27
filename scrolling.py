# archivo: motor_juego.py

import pygame as py
import os
import math

from Constantes import *  # Asegúrate de que este archivo exista y contenga ASSETS_PATH

def moving():
    py.init()
    clock = py.time.Clock()

    ANCHURA_PANTALLA = 1280
    ALTURA_PANTALLA = 720

    py.display.set_caption("Dezplazmiento de pantalla")
    pantalla = py.display.set_mode((ANCHURA_PANTALLA, ALTURA_PANTALLA))

    # Cargar la imagen de fondo correctamente
    BACKGROUND_IMAGE_PATH = os.path.join(ASSETS_PATH, "Font", "Fondo1.png")
    bg = py.image.load(BACKGROUND_IMAGE_PATH).convert()

    dezplasamiento = 0
    scroll = 0

    tiles = math.ceil(ANCHURA_PANTALLA / bg.get_width()) + 1

    # MAIN LOOP
    while True:
        clock.tick(33)

        i = 0
        while i < tiles:
            pantalla.blit(bg, (bg.get_width() * i + scroll, 0))
            i += 1

        scroll -= 6

        if abs(scroll) > bg.get_width():
            scroll = 0

        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                exit()

        py.display.update()
