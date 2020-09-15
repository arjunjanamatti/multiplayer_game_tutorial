import pygame
from network import Network

width = 1800
height = 1000
win = pygame.display.set_mode(size = (width, height))
pygame.display.set_caption('Client')

clientsNumber = 0

class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width, height)
        self.value = 3


    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.value
        if keys[pygame.K_RIGHT]:
            self.x += self.value
        if keys[pygame.K_UP]:
            self.y -= self.value
        if keys[pygame.K_DOWN]:
            self.y += self.value

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)


def read_pos(str):
    str = str.split(',')
    return int(str[0]), int(str[1])

def make_pos(tup):
    return str(tup[0]) + ',' + str(tup[1])

def redrawWindow(win, player, player2):
    win.fill((255,255,255))
    player.draw(win)
    player2.draw(win)
    pygame.display.update()

def main():
    run = True

    n = Network()
    startPos = read_pos(n.getPos())

    # player_1
    p = Player(x = startPos[0],
               y = startPos[1],
               width = 100,
               height = 100,
               color = (0,255,0))
    # player_2
    p_2 = Player(x = 0,
               y = 0,
               width = 100,
               height = 100,
               color = (0,255,0))

    clock = pygame.time.Clock()

    while run:
        clock.tick(60)

        p2Pos = n.send(data = make_pos(tup = (p.x, p.y)))
        p_2.x = p2Pos[0]
        p_2.y = p2Pos[1]
        p_2.update()




        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move()
        redrawWindow(win, p, p_2)


main()