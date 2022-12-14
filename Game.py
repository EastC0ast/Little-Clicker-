import pygame
import pygame_widgets
from pygame_widgets.button import Button

class Game:

    def __init__(self):
        self.score = 0
        self.level = 0
        self.clock = pygame.time.Clock()
        self.size = self.width, self.height = 650, 800
        self.center_of_window = self.width // 2, self.height // 2
        self.top_of_window = self.width // 2, 35
        self.bot_of_window = self.width // 2, 800
        self.screen = pygame.display.set_mode(self.size)
        self.screen.fill((255, 255, 255))
        self.screen_rect = self.screen.get_rect()
        self.font = pygame.font.match_font('Mont')

        self.ingame = True

    def but(self):
        self.ingame = False
        print('Clicked!')


    def start_game(self):
        x = 80
        y = 270
        v = 5
        m = 1
        pygame.display.set_caption('My Hommie Uses Clicker')
        background_image = pygame.image.load('background_img.png')
        lvl_img, lvl2_img = pygame.image.load('lvl.png'), pygame.image.load('1lvl.png')
        lvl_img, lvl2_img = pygame.transform.scale(lvl_img, (250, 283)), pygame.transform.scale(lvl2_img, (250, 283))
        lvl_img_rect = lvl_img.get_rect()
        font = pygame.font.match_font('Mont')
        mont64, mont32 = pygame.font.Font(font, 64), pygame.font.Font(font, 32)
        target_img, target2_img, target3_img = pygame.image.load('1st.png'), pygame.image.load(
            '2nd.png'), pygame.image.load('3rd.png')
        self.button = Button(
            self.screen,
            550,
            10,
            90,
            45,

            text='Магазин',
            fontSize=30,
            margin=20,
            radius=5,
            onClick=lambda: self.but()
        )
        running = True
        while running:
            self.screen.blit(background_image, (0, 0))
            if self.level == 0 or self.level == 2:
                self.cur_image = lvl_img
                if self.level == 0:
                    self.cur_target = target_img
                else:
                    self.cur_target = target3_img
            elif self.level == 1:
                self.cur_image = lvl2_img
                self.cur_target = target2_img
            self.screen.blit(self.cur_image, (0, 40))
            self.screen.blit(self.cur_target, (x, y))
            text = mont64.render(f'Кол-во очков {self.score}', True, (255, 255, 255))
            place = text.get_rect(center=self.top_of_window)
            self.screen.blit(text, place)
            events = pygame.event.get()
            pygame_widgets.update(events)
            isjump = False
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                    quit()
                if not isjump:
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.ingame:
                        if self.screen_rect.collidepoint(event.pos):
                            if self.level == 0:
                                self.score += 1
                            elif self.level == 1:
                                self.score += 2
                            elif self.level == 2:
                                self.score += 4
                            elif self.level == 3:
                                self.score += 8
                            elif self.level == 4:
                                self.score += 16
                            elif self.level == 5:
                                self.score += 32
                        if lvl_img_rect.collidepoint(event.pos):
                            if self.score >= 100:
                                if self.level == 0:
                                    self.level += 1
                                    self.score -= 100
                                if self.score >= 500:
                                    if self.level == 1:
                                        self.level += 1
                                        self.score -= 500
                                    if self.score >= 1000:
                                        if self.level == 2:
                                            self.level += 0
                                            self.score -= 1000
            mouse = pygame.mouse.get_pressed()
            if isjump == False:
                if mouse[0]:
                    isjump = True
            if isjump:
                F = (1 / 2) * m * (v ** 2)
                y -= F
                print(y)
                v = v - 1
                if v < 0:
                    m = -1
                if v == -6:
                    isjump = False
                    v = 5
                    m = 1
            pygame.time.delay(10)
            pygame.display.update()

    def exit_game(self):
        pass

    def choose_hero(self):
        pass

    def shop(self):
        pass

    def total_coins(self):
        pass
