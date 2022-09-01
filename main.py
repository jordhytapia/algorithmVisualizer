import pygame
import random

pygame.init()

class DrawInfo:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    BG_COLOR = WHITE

    GRADIENTS = [
        (128, 128, 128),
        (170,170,170),
        (190,190,190)
    ]

    FONT = pygame.font.SysFont('comicsans', 30)
    LGFONT = pygame.font.SysFont('comicsans', 40)
    sidePad = 100
    topPad = 150

    def __init__(self, width, height, lst):
        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Visual")
        self.set_list(lst)

    def set_list(self, lst):
        self.lst = lst
        self.minVal = min(lst)
        self.maxVal = max(lst)

        self.blockWidth = round((self.width - self.sidePad) / len(lst))
        self.blockHeight = round((self.height - self.topPad) / (self.maxVal - self.minVal))
        self.startX = self.sidePad // 2

def draw(drawInfo):
    drawInfo.window.fill(drawInfo.BG_COLOR)

    controls = drawInfo.FONT.render("R-reset | S-start sorting | A-ascending | D-descending", 1, drawInfo.BLACK)
    drawInfo.window.blit(controls, (drawInfo.width/2 - controls.get_width()/2, 5))

    sorts = drawInfo.FONT.render("I-insertion sort | B-bubble sort", 1, drawInfo.BLACK)
    drawInfo.window.blit(sorts, (drawInfo.width / 2 - sorts.get_width() / 2, 35))

    drawList(drawInfo)
    pygame.display.update()

def drawList(drawInfo):
    lst = drawInfo.lst
    for i,val in enumerate(lst):
        x = drawInfo.startX + i * drawInfo.blockWidth
        y = drawInfo.height - (val - drawInfo.minVal) * drawInfo.blockHeight
        color = drawInfo.GRADIENTS[i % 3]
        pygame.draw.rect(drawInfo.window, color, (x, y, drawInfo.blockWidth, drawInfo.height))

def generateStartingList(k, minVal, maxVal):
    lst = []
    for _ in range(k):
        val = random.randint(minVal, maxVal)
        lst.append(val)
    return lst

def main():
    run = True
    clock = pygame.time.Clock()

    k = 50
    minVal = 0
    maxVal = 100

    lst = generateStartingList(k, minVal, maxVal)
    drawInfo = DrawInfo(800, 600, lst)
    sorting = False
    ascending = True


    while run:
        clock.tick(60)
        draw(drawInfo)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type != pygame.KEYDOWN:
                continue
            if event.key == pygame.K_r:
                lst = generateStartingList(k, minVal, maxVal)
                drawInfo.set_list(lst)
                sorting == False
            elif event.key == pygame.K_SPACE and sorting == False:
                sorting = True
            elif event.key == pygame.K_a and not sorting:
                ascending = True
            elif event.key == pygame.K_d and not sorting:
                ascending = False

    pygame.quit()

if __name__ == "__main__":
    main()















