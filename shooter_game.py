from pygame import *
from random import *
mixer.init()
she2 = (0)
mixer.music.load('space.ogg')
mixer.music.play()
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed

        if keys_pressed[K_d] and self.rect.x < 595:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet("bullet.png",self.rect.centerx,self.rect.top,10)
        bulets.add(bullet)



class Cyborg(GameSprite):
    def update(self):
        global she2
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.y = -50
            self.rect.x = randint(0,700)
            self.speed = randint(2,7)
            she2 += 1

class Bullet(GameSprite):
    def update(self):
        self.rect.y-=self.speed
        if self.rect.y < 0:
            self.kill()

bulets = sprite.Group()





window = display.set_mode((700, 500))
display.set_caption("Шутер")
background = transform.scale(image.load("galaxy.jpg"), (700, 500))

font.init()
font = font.SysFont('Arial',70)
win = font.render("YOU WIN!!!!",True, (34, 255, 3))
los = font.render("YOU LOSE!!!!",True, (254,2,2))
she   = (0)

win1 = font.render("Убитые"+ str(she),True, (34, 255, 3))
los1 = font.render("Попущеные!"+ str(she2),True, (37,255,3))
clock = time.Clock()
FPS = 60

hero = Player('rocket.png', 300, 400, 10)


monsters = sprite.Group()

for i in range(3):
    monster0 = Cyborg('ufo.png',randint(0,700), -60, randint(2,4))
    monsters.add(monster0)

asteroids = sprite.Group()

for i in range(3):
    asreroid1 = Cyborg('asteroid.png',randint(0,700), -60, randint(2,4))
    asteroids.add(asreroid1)


finish = False
game = True
while game:
    if not finish:
        window.blit(background,(0, 0))
        window.blit(win1,(0, 0))
        window.blit(los1,(0, 30))
        hero.reset()
        hero.update()
        monsters.update()
        monsters.draw(window)
        bulets.update()
        bulets.draw(window)
        asteroids.update()
        asteroids.draw(window)
        if she > 30:
            finish = True
            window.blit(win,(250,150))
        if she2 > 30:
            finish = True
            window.blit(los,(250, 150))





    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                hero.fire()

    clock.tick(FPS)
    win1 = font.render("Убитые"+ str(she),True, (34, 255, 3))
    los1 = font.render("Попущеные!"+ str(she2),True, (37,255,3))
    kos =  sprite.groupcollide(monsters,bulets,True,True)
    for k in kos:
        monster0 = Cyborg('ufo.png',randint(0,700), -60, randint(2,3))
        monsters.add(monster0)
        she += 1



    



        
    display.update()