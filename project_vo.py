import pygame, sys, random, time, os
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Andrew Vo - Asteroid Dodging Game - Mercury

name = profile_main['name']               # Player Name
score1 = profile_main['score1']           # Score for Asteroid Minigame
score2 = profile_main['score2']           # Score for Simon Minigame
score3 = profile_main['score3']           # Score for Multiple Choice Minigame
score4 = profile_main['score4']           # Score for Minesweeper Minigame
score5 = profile_main['score5']           # Score for Shooting Minigame

class Player(pygame.sprite.Sprite):
    def __init__(self,screen):
        import pygame
        super(Player,self).__init__()
        self.screen=screen
        self.image1=pygame.image.load("images\ship.png")
        self.rect=self.image1.get_rect()
        self.rect.inflate_ip(-30,-10)
        self.speed= 25

    def moveUp(self):
        if self.rect.top > 0:
            self.rect.top -= self.speed
    def moveDown(self):
        if self.rect.bottom < self.screen.get_height():
            self.rect.bottom += self.speed
    def moveLeft(self):
        if self.rect.left > 0:
            self.rect.left -= self.speed
    def moveRight(self):
        if self.rect.right < self.screen.get_width():
            self.rect.right += self.speed

    def collide(self, group):
        import pygame, pickle
        global profile_main, name, score1, score2, score3, score4, score5
        global score
        if pygame.sprite.spritecollide(self, group, False):
            print "You've Been Hit! GAME OVER"
            score1 = max(score, score1)
            nprofile = {'name': name, 'score1': score1, 'score2': score2, 'score3': score3, 'score4': score4,
                        'score5': score5}
            spath = 'profiles\\' + name + '.p'
            pickle.dump(nprofile, open(spath, 'wb'))
            profile_main = nprofile
            pygame.time.wait(2000)
            pygame.display.quit()
            return True
        else:
            return False


class Rock(pygame.sprite.Sprite):
    def __init__(self,screen):
        import pygame, random
        super(Rock,self).__init__()
        self.image=pygame.image.load("images\\rock.png")
        self.rect=self.image.get_rect()
        self.screen=screen
        self.speed=random.randint(1,10)
        self.moveRockoff(random.randint(1,50))

    def moveRockoff(self, offset):
        import random
        self.rect.top=0
        self.rect.centerx=random.randint(0,self.screen.get_width())

    def update(self):
        if self.rect.top >= 1000:
            self.moveRockoff(0)
        else:
            self.rect.top += self.speed

def main():
    import pygame, sys, time
    global Rock, Player
    global score
    pygame.init()

    WIDTH = 1100
    HEIGHT = 950
    mainSurface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

    number_of_rocks = 8
    clock = pygame.time.Clock()

    scoreFont = pygame.font.SysFont("monospace", 72)

    score = 0

    background_file = "images\space.png"
    background = pygame.image.load(background_file)
    background = pygame.transform.scale(background,(WIDTH,HEIGHT))

    pygame.display.set_caption("Astroid Belt Cruise")

    rockGroup = pygame.sprite.Group()

    myPlayer=Player(mainSurface)
    myPlayer.rect.left=20
    myPlayer.rect.centerx=mainSurface.get_width()/2
    myPlayer.rect.centery=mainSurface.get_height()-100

    for x in range(number_of_rocks):
        newRock=Rock(mainSurface)
        rockGroup.add(newRock)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        mainSurface.fill((255,255,255))

        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_UP):
                myPlayer.moveUp()
            if (event.key == pygame.K_DOWN):
                myPlayer.moveDown()
            if (event.key == pygame.K_LEFT):
                myPlayer.moveLeft()
            if (event.key == pygame.K_RIGHT):
                myPlayer.moveRight()

        if myPlayer.collide(rockGroup):
            pygame.time.wait(400)
            return

        mainSurface.fill((255, 255, 255))
        mainSurface.blit(background,[0,0])
        rockGroup.update()
        rockGroup.draw(mainSurface)
        mainSurface.blit(myPlayer.image1, myPlayer.rect)

        scoreBoard = scoreFont.render("Score {0}".format(score), 1, (255, 255, 255))
        mainSurface.blit(scoreBoard, (5, 10))
        score += 1

        if score == 1500:
            print "You've Made it!!"
            score1 = max(score, score1)
            nprofile = {'name': name, 'score1': score1, 'score2': score2, 'score3': score3, 'score4': score4,
                        'score5': score5}
            spath = 'profiles\\' + name + '.p'
            pickle.dump(nprofile, open(spath, 'wb'))
            profile_main = nprofile
            pygame.time.wait(400)
            pygame.display.quit()
            break

        pygame.display.update()
        myPlayer.update()
        clock.tick(60)
main()
