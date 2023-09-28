#Создай собственный Шутер!
from random import *
from pygame import *
font.init()
mixer.init()
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed=0, image_wight=0, image_height=0):
        super().__init__()
        self.image_wight = image_wight
        self.image_height = image_height
        self.image = transform.scale(image.load(player_image), (image_wight, image_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.fire = True
        self.fps = 40
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        self.fps -= 1
        if self.fps <= 0:
            self.fire = True


class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed=0, image_wight=0, image_height=0, hearts=3):
        super().__init__(player_image, player_x, player_y, player_speed, image_wight, image_height)
        self.hearts = hearts
    def move(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < x-70:
            self.rect.x += self.speed
        if keys_pressed[K_SPACE] and self.fire:
            self.fire = False
            self.fps = 40
            bullet = Bullet('bullet.png', self.rect.centerx-3, self.rect.centery, 2, 10, 15)
            bullets.add(bullet)
            # kick = mixer.Sound('fire.ogg') 
            # kick.play()
            
        

class Enemy(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed=0, image_wight=0, image_height=0, hearts=1):
        super().__init__(player_image, player_x, player_y, player_speed, image_wight, image_height)
        self.hearts = hearts
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 570:
            self.rect.y = -70
            global lost
            lost += 1
            self.rect.x = randint(70, 630)

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed

def lose():
    lose = font1.render('YOU LOSE!', True, (255, 255, 255))
    window.blit(lose, (290, 250))
    global end
    end = False

class Button():
    def __init__(self, x, y, wight, height, color):
        self.rect = Rect(x, y, wight, height)
        self.color = color
        self.x = x
        self.y = y

    def draw_rect(self, border_color=0, new_color=0):
        if border_color == 0:
            border_color = self.color
        if new_color == 0:
            new_color = self.color
        draw.rect(window, self.color, self.rect)
        draw.rect(window, border_color, self.rect, 5)
    
    def create_text(self, size):
        self.font = font.SysFont('Arial', size)

    def draw_text(self, text_color, text, xofset, yofset):
        question = self.font.render(text, True, text_color)
        window.blit(question, (self.x+xofset, self.y+yofset))

def enemy():
    global monsters
    for monster in monsters:
        monster.kill()
    sprite2 = Enemy('ufo.png', randint(70, 630), randint(-110, -70), 1, 65, 65)
    sprite3 = Enemy('ufo.png', randint(70, 630), randint(-110, -70), 1.3, 65, 65)
    sprite4 = Enemy('ufo.png', randint(70, 630), randint(-110, -70), 1.5, 65, 65)
    sprite5 = Enemy('ufo.png', randint(70, 630), randint(-110, -70), 1.7, 65, 65)
    sprite6 = Enemy('ufo.png', randint(70, 630), randint(-110, -70), 1.8, 65, 65)
    monsters.add(sprite2, sprite3, sprite4, sprite5, sprite6)
    

x = 700
y = 500
window = display.set_mode((x, y))
display.set_caption('Шутер')
background = transform.scale(image.load('galaxy.jpg'), (x, y))
window.blit(background, (0,0))
    



sprite1 = Player('rocket.png', 315, 405, 3.5, 65, 90, 3)
# sprite2 = Enemy('ufo.png', randint(70, 630), randint(-110, -70), 1, 65, 65)
# sprite3 = Enemy('ufo.png', randint(70, 630), randint(-110, -70), 1.3, 65, 65)
# sprite4 = Enemy('ufo.png', randint(70, 630), randint(-110, -70), 1.5, 65, 65)
# sprite5 = Enemy('ufo.png', randint(70, 630), randint(-110, -70), 1.7, 65, 65)
# sprite6 = Enemy('ufo.png', randint(70, 630), randint(-110, -70), 1.8, 65, 65)
sprite8 = GameSprite('heart1.png', 1, 80, 0, 55, 35)
sprite9 = GameSprite('heart1.png', 41, 80, 0, 55, 35)
sprite10 = GameSprite('heart1.png', 81, 80, 0, 55, 35)
sprite12 = Enemy('boss.png', 270, -100, 1, 165, 105, 3)




monsters = sprite.Group()
# monsters.add(sprite2, sprite3, sprite4, sprite5, sprite6)
enemy()

bullets = sprite.Group()

start = Button(263, 200, 150, 65, (255, 255, 255))
start.draw_rect((0, 0, 0))
start.create_text(40)
start.draw_text((0, 0, 0), 'START', 30, 20)


restart = Button(265, 100, 175, 65, (255, 255, 255))




    



# mixer.music.load('space.ogg')
# mixer.music.play()




font1 = font.SysFont('Arial', 35)
kill = 0
lost = 0
end = False
game = True
list_hearts = [sprite8, sprite9, sprite10]
clock = time.Clock()
while game:
    if end:
        window.blit(background, (0,0))
        bullets.draw(window)
        bullets.update()
        sprite1.reset()
        sprite1.move()

       
        
        if kill <= 7:
            monsters.draw(window)
            monsters.update()
        if kill >= 7:
            for monster in monsters:
                monster.kill()
            sprite12.reset()
            sprite12.update()   


        for i in range(sprite1.hearts):
            list_hearts[i].reset()   
        count = font1.render('Счёт:'+str(kill), True, (255, 255, 255))
        miss = font1.render('Пропущено:'+str(lost), True, (255, 255, 255))
        window.blit(count, (5,20))
        window.blit(miss, (5,55))
        
        hits = sprite.groupcollide(monsters, bullets, True, True)
        for hit in hits:
            kill += 1
            sprite7 = Enemy('ufo.png', randint(70, 630), randint(-110, -70), random()+1, 65, 65)
            monsters.add(sprite7)
        
        hits1 = sprite.spritecollide(sprite1, monsters, True)
        for hit in hits1:
            sprite1.hearts -= 1
            sprite11 = Enemy('ufo.png', randint(70, 630), randint(-110, -70), random()+1, 65, 65)
            monsters.add(sprite11)
        
        hits2 = sprite.spritecollide(sprite12, bullets, True)
        for hit in hits2:
            sprite12.hearts -=1
            sprite12.rect.x = randint(70, 630)

        if sprite.collide_rect(sprite12, sprite1):
            print(sprite12.rect.y)
            lose()
            restart.draw_rect((0, 0, 0))
            restart.create_text(40)
            restart.draw_text((0, 0, 0), 'RESTART', 24, 20)
        
        if lost >= 5:
            lose()
            restart.draw_rect((0, 0, 0))
            restart.create_text(40)
            restart.draw_text((0, 0, 0), 'RESTART', 24, 20)
        
        if sprite12.hearts <= 0:
            win = font1.render('YOU WIN!', True, (255, 255, 255))
            window.blit(win, (290, 250))
            end = False
            restart.draw_rect((0, 0, 0))
            restart.create_text(40)
            restart.draw_text((0, 0, 0), 'RESTART', 24, 20)
        
        if sprite12.rect.y >= 570:
            lose()
            restart.draw_rect((0, 0, 0))
            restart.create_text(40)
            restart.draw_text((0, 0, 0), 'RESTART', 24, 20)
            
        if sprite1.hearts <= 0:
            lose()
            restart.draw_rect((0, 0, 0))
            restart.create_text(40)
            restart.draw_text((0, 0, 0), 'RESTART', 24, 20)
            
            
            
    
    for e in event.get():
        if e.type == MOUSEBUTTONDOWN and e.button == 1:
            x_button, y_button = e.pos
            if start.rect.collidepoint(x_button, y_button):
                end = True
            if restart.rect.collidepoint(x_button, y_button):
                kill = 0
                lost = 0
                sprite12.hearts = 3
                sprite1.hearts = 3
                for monster in monsters:
                    monster.rect.y = randint(-110, -70)
                bullets = sprite.Group()
                sprite12.rect.y = -100
                enemy()
                monsters.draw(window)
                monsters.update()
                end = True
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(105)