class CanvasSettings():
    def __init__(self):
        '''
        画布
        '''
        self.canvas_width = 480
        self.canvas_height = 852 #画面的大小根据背景图的大小来设置

class StartCanvasSettings():
    def __init__(self):
        self.path = ".\\image\\start.png"

class OverCanvasSettings():
    def __init__(self):
        # 结束画面
        self.canvas_width = 400
        self.canvas_height = 654
        self.canvas_path = ".\\image\\gameover.gif"

class BackgroundSettings():
    def __init__(self):
        '''
        背景
        '''
        self.background_1_path = '.\\image\\background_1.png'
        self.background_2_path = '.\\image\\background_2.png'
        self.bg_speed = 10

class EnemyOneSettings():
    def __init__(self):
        '''
        enemy_1
        '''
        self.enemy_1_path = ".\\image\\enemy1.png"
        self.enemy_1_width = 57
        self.enemy_1_height = 51
        self.enemy_1_speed = 8
        self.enemy_1_lives = 1

class EnemyTwoSettings():
    def __init__(self):
        '''
        enemy_2
        '''
        self.enemy_2_path = ".\\image\\enemy2.png"
        self.enemy_2_width = 69
        self.enemy_2_height = 95
        self.enemy_2_speed = 5
        self.enemy_2_lives = 3

class EnemyThreeSettings():
    def __init__(self):
        '''
        enemy_3
        '''
        self.enemy_3_path = ".\\image\\enemy3.png"
        self.enemy_3_width = 169
        self.enemy_3_height = 258
        self.enemy_3_speed = 3
        self.enemy_3_lives = 6

class HeroSettings():
    def __init__(self):
        '''
        hero
        '''
        self.hero_path = ".\\image\\hero1.png"
        self.hero_width = 99
        self.hero_height = 124
        self.hero_lives = 3
        self.hero_speed = 5

class BulletSettings():
    def __init__(self):
        '''
        bullet
        '''
        self.bullet_path = ".\\image\\bullet1.png"
        self.bullet_speed = -21

class PlayImageSettings():
    def __init__(self):
        self.enemy_1_down_image_list = [".\\image\\enemy1_down1.png", ".\\image\\enemy1_down2.png",
                                        ".\\image\\enemy1_down3.png", ".\\image\\enemy1_down4.png"]

        self.enemy_2_down_image_list = [".\\image\\enemy2_down1.png", ".\\image\\enemy2_down2.png",
                                        ".\\image\\enemy2_down3.png", ".\\image\\enemy2_down4.png"]

        self.enemy_3_down_image_list = [".\\image\\enemy3_down1.png", ".\\image\\enemy3_down2.png",
                                        ".\\image\\enemy3_down3.png", ".\\image\\enemy3_down4.png",
                                        ".\\image\\enemy3_down5.png", ".\\image\\enemy3_down6.png"]

        self.hero_blowup_list = [".\\image\\hero_blowup_n1.png", ".\\image\\hero_blowup_n2.png",
                                 ".\\image\\hero_blowup_n3.png", ".\\image\\hero_blowup_n4.png"]