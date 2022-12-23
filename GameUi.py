import pygame

class GameUi:
    def __init__(self, debug:bool):
        self.size = (800, 650)
        self.width, self.height = self.size
        self.win = pygame.display.set_mode(self.size)
        pygame.display.set_caption('Lost In Siberia')

        self.info_width = (self.width//3)//2
        self.action_width = self.width - (self.info_width * 2)

        self.left_info_surface = pygame.Surface((self.info_width, self.height))
        self.right_info_surface = pygame.Surface((self.info_width, self.height))
        self.top_action_surface = pygame.Surface((self.action_width, self.height))
        self.bottom_action_surface = pygame.Surface((self.action_width, (self.height//3)*2))
        
        if debug:
            self.left_info_surface.fill((255, 255, 255))
            self.right_info_surface.fill((255, 0, 0))
            self.top_action_surface.fill((0, 0, 255))
            self.bottom_action_surface.fill((0, 255, 0))

        self.fps = 15 
        self.run = True

    def commands(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

    def render(self):
        self.win.blit(self.left_info_surface, (0, 0))
        self.win.blit(self.right_info_surface, (self.width - self.info_width, 0))
        self.win.blit(self.top_action_surface, (self.info_width, (self.height//3)*2))
        self.win.blit(self.bottom_action_surface, (self.info_width, 0))

    def gameloop(self):
        while self.run:
            pygame.time.Clock().tick(self.fps)
            self.commands()
            self.render()
            pygame.display.update()


