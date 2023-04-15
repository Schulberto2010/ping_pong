from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, path_image, sprite_x, sprite_y, sprite_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(path_image), (width, height))
        self.speed = sprite_speed
        self.rect = self.image.get_rect()
        self.rect.x = sprite_x
        self.rect.y = sprite_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height-145:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height-145:
            self.rect.y += self.speed

back = (200, 255, 255)
win_width = 800
win_height = 600
window = display.set_mode((win_width, win_height))
window.fill(back)

game = True
finish = False
clock = time.Clock()
FPS = 120
racket1 = Player("racket.png", 30, 200, 4, 50, 150)
racket2 = Player("racket.png", 720, 200, 4, 50, 150)
ball = GameSprite("tenis_ball.png", 350, 250, 4, 50, 50)

font.init()
font = font.SysFont("Arial", 35)
lose1 = font.render("Player 1 LOSE!!!", True, (200, 0, 0))
lose2 = font.render("Player 2 LOSE!!!", True, (200, 0, 0))

speed_x = 3
speed_y = 3
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
            
    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
                speed_x *= -1
        
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
        
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (300,250))

        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (300,250))
        
        racket1.reset()
        racket2.reset()
        ball.reset()
    else:
        time.delay(2000)
        finish = False
        ball.kill()
        ball = GameSprite("tenis_ball.png", 350, 250, 4, 50, 50)
        
    
    display.update()
    clock.tick(FPS)
