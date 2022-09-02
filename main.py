import math
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
        self.blockHeight = math.floor((self.height - self.topPad) / (self.maxVal - self.minVal))
        self.startX = self.sidePad // 2

def draw(drawInfo, algName, ascending):
    drawInfo.window.fill(drawInfo.BG_COLOR)

    title = drawInfo.LGFONT.render(f"{algName} - {'Ascending' if ascending else 'Descending'}", 1, drawInfo.GREEN)
    drawInfo.window.blit(title, (drawInfo.width / 2 - title.get_width() / 2, 5))

    controls = drawInfo.FONT.render("R-reset | S-start sorting | A-ascending | D-descending", 1, drawInfo.BLACK)
    drawInfo.window.blit(controls, (drawInfo.width/2 - controls.get_width()/2, 55))

    sorts = drawInfo.FONT.render("I-insertion sort | B-bubble sort", 1, drawInfo.BLACK)
    drawInfo.window.blit(sorts, (drawInfo.width / 2 - sorts.get_width() / 2, 95))

    drawList(drawInfo)

    pygame.display.update()

def drawList(drawInfo, colorPositions={}, clearBG = False):
    lst = drawInfo.lst

    if clearBG:
        clearRect = (drawInfo.sidePad // 2, drawInfo.topPad,
                     drawInfo.width-drawInfo.sidePad, drawInfo.height-drawInfo.topPad)
        pygame.draw.rect(drawInfo.window, drawInfo.BG_COLOR, clearRect)

    for i,val in enumerate(lst):
        x = drawInfo.startX + i * drawInfo.blockWidth
        y = drawInfo.height - (val - drawInfo.minVal) * drawInfo.blockHeight

        color = drawInfo.GRADIENTS[i % 3]

        if i in colorPositions:
            color = colorPositions[i]

        pygame.draw.rect(drawInfo.window, color, (x, y, drawInfo.blockWidth, drawInfo.height))

    if clearBG:
        pygame.display.update()



def generateStartingList(k, minVal, maxVal):
    lst = []
    for _ in range(k):
        val = random.randint(minVal, maxVal)
        lst.append(val)
    return lst

def bubbleSort(drawInfo, ascending = True):
    lst = drawInfo.lst

    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            num1 = lst[j]
            num2 = lst[j+1]

            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                lst[j], lst[j+1] = lst[j+1], lst[j]
                drawList(drawInfo, {j:drawInfo.GREEN, j+1:drawInfo.RED}, True)
                yield True
    return lst

def insertionSort(drawInfo, ascending = True):
    lst = drawInfo.lst

    for i in range(1, len(lst)):
        current = lst[i]

        while True:
            ascendingSort = i > 0 and lst[i-1] > current and ascending
            descendingSort = i > 0 and lst[i-1] < current and not ascending

            if not ascendingSort and not descendingSort:
                break

            lst[i] = lst[i-1]
            i = i - 1
            lst[i] = current
            drawList(drawInfo, {i-1 : drawInfo.GREEN, i: drawInfo.RED}, True)
            yield True
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

    sortingAlg = bubbleSort
    sortingAlgName = 'Bubble Sort'
    sortingAlgGen = None


    while run:
        clock.tick(120)
        if sorting:
            try:
                next(sortingAlgGen)
            except StopIteration:
                sorting = False
        else:
            draw(drawInfo, sortingAlgName, ascending)

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
                sortingAlgGen = sortingAlg(drawInfo, ascending)
            elif event.key == pygame.K_a and not sorting:
                ascending = True
            elif event.key == pygame.K_d and not sorting:
                ascending = False
            elif event.key == pygame.K_i and not sorting:
                sortingAlg = insertionSort
                sortingAlgName = 'Insertion Sort'
            elif event.key == pygame.K_b and not sorting:
                sortingAlg = bubbleSort
                sortingAlgName = 'Bubble Sort'

    pygame.quit()

if __name__ == "__main__":
    main()















