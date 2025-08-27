# -*- coding: utf-8 -*-
# Cristian Iglesias Vera
# Misión del módulo python
import pygame
import time
import os, pygame
import random

def load_image(name):
    path = os.path.join('', name)
    return pygame.image.load(path).convert()

pygame.init()

icono = pygame.image.load("snake-icon.png")
pygame.display.set_icon(icono)


Blanco = (255, 255, 255)
Negro = (0, 0, 0)
Rojo = (255, 0, 0)
Azul = (0, 0, 255)
Verde = (0, 128, 0)
Lila = (108, 70, 117)

ancho = 1080
altura = 720


superficie = pygame.display.set_mode((ancho,altura))
pygame.display.set_caption('Serpiente')


background = load_image('01.jpg')

superficie.blit(background, [0, 0])


reloj = pygame.time.Clock()

serp_tamano = 20
CPS = 10


font = pygame.font.SysFont("arial.ttf", 40)
      

def pausa():
    pausado = True
   
    while pausado:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    pausado = False

                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        background = load_image('02.jpg')
        superficie.blit(background, [0, 0])
        message_to_screen("Pausa", Rojo, -200)
        pygame.display.update()
        reloj.tick(5)

def rapidez(speed):
    text = font.render("Rapidez: "+str(speed), True, Negro)
    superficie.blit(text, [600,0])

def puntos(score):
    text = font.render("Puntos: "+str(score), True, Negro)
    superficie.blit(text, [0,0])

def intro_juego():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        background = load_image('03.jpg')
        superficie.blit(background, [0, 0])
        message_to_screen("Bienvenid@s", Blanco, -50)
        message_to_screen("Controla a la serpiente usando", Rojo, 0)
        message_to_screen("teclas de movimiento para comer manzanas Rojas, Verdes y Lilas", Rojo, 50)
        message_to_screen("Lila Largo+10, Verde Rapidez+1, Roja Puntaje+1 cada 3 rojas Rapidez+1", Rojo, 100)
        message_to_screen("Si la serpiente toca el borde o se toca a si misma, pierdes.", Blanco, 150)
        message_to_screen("'P' pausa", Blanco, 200)
        message_to_screen("'C' Continuar", Blanco, 250)
        message_to_screen("'Q' Salir", Blanco, 300)
        pygame.display.update()
        reloj.tick(CPS)

def serpiente(serp_tamano, listaSerpiente):
    for i in listaSerpiente:
        pygame.draw.rect(superficie, Negro, [i[0],i[1],serp_tamano,serp_tamano])

def text_objetos(text, color):
    textSuperficie = font.render(text, True, color)
    return textSuperficie, textSuperficie.get_rect()
def message_to_screen(msg, color, y_displace=0):
    textSur, textRect = text_objetos(msg, color)
    textRect.center = (ancho/2), (altura/2)+ y_displace
    superficie.blit(textSur, textRect)
        
    
def gameLoop():
    gameExit = False
    gameOver = False

    upSpeed = 0
    speed = 0
    
    mover_x = 700
    mover_y = 700

    mover_x_cambio = 0
    mover_y_cambio = 0

    listaSerpiente = []
    largoSerpiente = 1
    snake = 1

    azarManzanaX = round(random.randrange(0, 1060 - 20)/20.0)*20.0
    azarManzanaY = round(random.randrange(0, 700 - 20)/20.0)*20.0

    azarManzanaX2 = round(random.randrange(0, 1060 - 20)/20.0)*20.0
    azarManzanaY2 = round(random.randrange(0, 700 - 20)/20.0)*20.0

    azarManzanaX3 = round(random.randrange(0, 1060 - 20)/20.0)*20.0
    azarManzanaY3 = round(random.randrange(0, 700 - 20)/20.0)*20.0

    pulsar_sonido = pygame.mixer.Sound("loop.ogg")
    pulsar_sonido.set_volume(0.50)
    pulsar_sonido.play(18)
    

    
    while not gameExit:

        while gameOver == True:

            superficie.blit(background, [0, 0])
            pulsar_sonido.stop()
            message_to_screen("Game Over", Rojo, -50)
            message_to_screen("'V' para Volver, 'S' para Salir.", Rojo, 50)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_v:
                        gameLoop()
                    
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    mover_x_cambio = -serp_tamano
                    mover_y_cambio = 0
                elif event.key == pygame.K_RIGHT:
                    mover_x_cambio = serp_tamano
                    mover_y_cambio = 0
                elif event.key == pygame.K_UP:
                    mover_y_cambio = -serp_tamano
                    mover_x_cambio = 0
                elif event.key == pygame.K_DOWN:
                    mover_y_cambio = serp_tamano
                    mover_x_cambio = 0   
                elif event.key == pygame.K_p:
                    pulsar_sonido.set_volume(0.0)
                    pausa()
                    pulsar_sonido.set_volume(0.50)

                                     
        if mover_x >= ancho or mover_x < 0 or mover_y >= altura or mover_y < 0:
            gameOver = True


        mover_x += mover_x_cambio
        mover_y += mover_y_cambio
        superficie.blit(background, [0, 0])

        pygame.draw.rect(superficie, Rojo, [azarManzanaX, azarManzanaY, 20, 20])
        pygame.draw.rect(superficie, Verde, [azarManzanaX2, azarManzanaY2, 20, 20])
        pygame.draw.rect(superficie, Lila, [azarManzanaX3, azarManzanaY3, 20, 20])

        cabezaSerpiente = []
        cabezaSerpiente.append(mover_x)
        cabezaSerpiente.append(mover_y)
        listaSerpiente.append(cabezaSerpiente)
        if len(listaSerpiente) > largoSerpiente:
            del listaSerpiente[0]

        for eachSegment in listaSerpiente[:-1]:
            if eachSegment == cabezaSerpiente:
                gameOver = True


        serpiente(serp_tamano,listaSerpiente)
        puntos(snake-1)
        rapidez(speed)
        
        pygame.display.update()

        

        if mover_x == azarManzanaX and mover_y == azarManzanaY:

            pygame.mixer.music.load("beat2.ogg")
            
            azarManzanaX = round(random.randrange(0, 1060-20)/20.0)*20.0
            azarManzanaY = round(random.randrange(0, 700-20)/20.0)*20.0
            largoSerpiente += 1
            snake += 1
            upSpeed += 1
            if upSpeed == 3:
                speed +=1
                upSpeed = 0
                
            pygame.mixer.music.play(0)
                   
            
        elif mover_x == azarManzanaX2 and mover_y == azarManzanaY2:

            pygame.mixer.music.load("beat1.ogg")
            
            azarManzanaX2 = round(random.randrange(0, 1060-20)/20.0)*20.0
            azarManzanaY2 = round(random.randrange(0, 700-20)/20.0)*20.0
            speed +=1
            pygame.mixer.music.play(0)
                                
            
        elif mover_x == azarManzanaX3 and mover_y == azarManzanaY3:

            pygame.mixer.music.load("beat.ogg")
            
            azarManzanaX3 = round(random.randrange(0, 1060-20)/20.0)*20.0
            azarManzanaY3 = round(random.randrange(0, 700-20)/20.0)*20.0
            largoSerpiente += 10
            
            pygame.mixer.music.play(0)
                    
        reloj.tick(CPS+speed)

    pygame.quit()
    quit()

intro_juego()
gameLoop()

