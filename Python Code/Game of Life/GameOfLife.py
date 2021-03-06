import pygame
import numpy as np
import time


pygame.init()

width,heigh = 1000,1000
screen = pygame.display.set_mode((heigh,width))

bg = 25,25,25
screen.fill(bg)

#Numero de celldas y dimension
nxC,nyC = 50,50
dimCW = width / nxC
dimCH = heigh / nyC

#Estado de las celdas (Matriz) Alive = 1, Dead = 0
gameState = np.zeros((nxC,nyC))

PauseExecution = False
ExitGame = False
#Automata Palo
gameState[5,3] = 1
gameState[5,4] = 1
gameState[5,5] = 1



#Bucle de ejecucion
while not ExitGame:
    # Copy status
    newGameState = np.copy(gameState)
    #Refresco de pantalla
    screen.fill(bg)
    

    #Contrtol de eventos de teclado y raton
    events = pygame.event.get()
    for ev in events:
        if ev.type == pygame.KEYDOWN:
            PauseExecution = not PauseExecution
        #Detecion de raton
        mouseClick = pygame.mouse.get_pressed()

        #Dar vida a celda
        if mouseClick[0] == 1:
            posX,posY = pygame.mouse.get_pos()
            celX,celY = int(np.floor(posX / dimCW)), int(np.floor(posY/dimCH))
            newGameState[celX,celY] = 1
        #Matar a celda
        elif mouseClick[2] == 1:
            posX,posY = pygame.mouse.get_pos()
            celX,celY = int(np.floor(posX / dimCW)), int(np.floor(posY/dimCH))
            newGameState[celX,celY] = 0

        #RatonCentral = Exit main game loop  
        if mouseClick[1] == 1:
            ExitGame = True

    for x in range(0,nxC):
        for y in range(0,nyC):
            if not PauseExecution:
                #Calculo del numero de vecinos de cada una de la celdas
                n_neigh = gameState[(x-1)%nxC,(y-1)%nyC] + gameState[(x)%nxC,(y-1)%nyC] + \
                        gameState[(x+1)%nxC,(y-1)%nyC] + gameState[(x-1)%nxC,(y)%nyC] + \
                        gameState[(x+1)%nxC,(y)%nyC] + gameState[(x-1)%nxC,(y+1)%nyC] + \
                         gameState[(x)%nxC,(y+1)%nyC] + gameState[(x+1)%nxC,(y+1)%nyC]

                #Reglas de juego
                #(1)Una celda muerta(state = 0), con 3 vecinas vivas, "revive"
                if gameState[x,y] == 0 and n_neigh == 3:
                    newGameState[x,y] = 1
                
                #(2)Una celda viva con menos de 2 vecionos o mas de 3, "muere"
                elif gameState[x,y] == 1 and (n_neigh < 2 or n_neigh > 3):
                    newGameState [x,y] = 0

            #Cada un de los cuadraditos con sus 4 coordenadas
            poly = [((x)  * dimCW, y * dimCH),
                    ((x+1)* dimCW, y * dimCH),
                    ((x+1)* dimCW, (y+1) * dimCH),
                    ((x)  * dimCW, (y+1) * dimCH)]


            #Pintado de los polys en funcion del estado de la celda
            if newGameState[x,y] == 0:
                pygame.draw.polygon(screen,(128,128,128),poly,2)
            else:
                pygame.draw.polygon(screen,(255,255,255),poly,0)
            
    
    gameState = np.copy(newGameState)
    time.sleep(0.1)
    pygame.display.flip()


