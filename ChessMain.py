#Responsible for handingling user input and displaying gameState

import ChessEngine
import pygame as p

p.init()
WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT //DIMENSION
MAX_FPS = 15 #Helps with animation
IMAGES = {}


#Make a global dictionary of images 
def loadImages():
    pieces = ['wP', 'bP', 'wR', 'bR', 'bK', 'wK', 'bQ', 'wQ', 'bN','wN','bB','wB']

    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load(f"/home/oso/Coding Projects/ChessGame/Images for Chess Game/Pieces/{piece}.png"), 
        (SQ_SIZE, SQ_SIZE))

def main():

    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    loadImages()
    gameOn = True

    while gameOn:
        for e in p.event.get():
            if e.type == p.QUIT:
                gameOn = False

        drawBoard(screen,gs)
        clock.tick(MAX_FPS)
        p.display.flip()


def drawBoard(screen, gs):
    drawBackground(screen)
    drawPieces(screen, gs.board)

def drawBackground(screen): 
    for row in range(8):
        for col in range(8):
            if(row%2 != 0):
                if(col%2 !=0):
                    p.draw.rect(screen, p.Color("gray"), p.Rect(col*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))
                else:
                    p.draw.rect(screen, p.Color("darkgreen"), p.Rect(col*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))
            else:
                if(col%2 !=0):
                    p.draw.rect(screen, p.Color("darkgreen"), p.Rect(col*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))
                else:
                    p.draw.rect(screen, p.Color("gray"), p.Rect(col*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))

def drawPieces(screen, board):
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece != '--':
                screen.blit(IMAGES[piece], p.Rect(col*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))


if __name__ == "__main__":
    main()


