import pygame


class Setting():
    #初始化游戏设置，储存游戏设置、全局变量
    def __init__(self):
        self.game_name = 'Schulte Grid'
        self.sc_w = 640
        self.sc_h = 0.7*self.sc_w
        self.sc_max = 1440
        self.sc_min = 360
        self.bg_color = (240,210,210)
        self.te_color = (40,40,40)
        self.bu_color = (120,100,100)
        self.bu_active_color = (80,60,60)
        
        self.sc_r_mark = False
        self.sc_l_mark = False
        self.game_mark = False
        self.time_mark = False
        self.over_mark = False
        self.record_mark = False

        self.update_screen()
        
    def update_screen(self):
        self.screen = pygame.display.set_mode((self.sc_w,self.sc_h))

    def init(self):
        sc_w = self.sc_w
        sc_h = self.sc_h
        self.__init__()
        
        self.sc_w = sc_w
        self.sc_h = sc_h
        self.update_screen()


