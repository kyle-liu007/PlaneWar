import random
from base import Base
from settings import CanvasSettings,EnemyOneSettings,EnemyTwoSettings,EnemyThreeSettings

settings_canvas = CanvasSettings()
settings_one = EnemyOneSettings()
settings_two = EnemyTwoSettings()
settings_three = EnemyThreeSettings()

class Enemy_1(Base):
    def __init__(self, root, canvas, queue, tags):
        super(Enemy_1, self).__init__(root, canvas, queue, settings_one.enemy_1_lives, tags)
        self.xpos = random.randint(settings_one.enemy_1_width//2,
                                       (settings_canvas.canvas_width - settings_one.enemy_1_width//2))
        self.ypos = -(settings_one.enemy_1_height//2)
        self.speed = settings_one.enemy_1_speed
        self.NW_xpos = self.xpos - settings_one.enemy_1_width//2
        self.NW_ypos = self.ypos - settings_one.enemy_1_height//2
        self.SE_xpos = self.xpos + settings_one.enemy_1_width//2
        self.SE_ypos = self.ypos + settings_one.enemy_1_height//2


    def run(self):
        self.canvas.move(self.image, 0, self.speed)
        self.ypos += self.speed
        self.NW_xpos = self.xpos - settings_one.enemy_1_width // 2
        self.NW_ypos = self.ypos - settings_one.enemy_1_height // 2
        self.SE_xpos = self.xpos + settings_one.enemy_1_width // 2
        self.SE_ypos = self.ypos + settings_one.enemy_1_height // 2

class Enemy_2(Base):
    def __init__(self, root, canvas, queue, tags):
        super(Enemy_2, self).__init__(root,canvas, queue, settings_two.enemy_2_lives, tags)
        self.xpos = random.randint(settings_two.enemy_2_width // 2,
                                       (settings_canvas.canvas_width - settings_two.enemy_2_width // 2))
        self.ypos = -(settings_two.enemy_2_height // 2)
        self.speed = settings_two.enemy_2_speed
        self.NW_xpos = self.xpos - settings_two.enemy_2_width // 2
        self.NW_ypos = self.ypos - settings_two.enemy_2_height // 2
        self.SE_xpos = self.xpos + settings_two.enemy_2_width // 2
        self.SE_ypos = self.ypos + settings_two.enemy_2_height // 2

    def run(self):
        self.canvas.move(self.image, 0, self.speed)
        self.ypos += self.speed
        self.NW_xpos = self.xpos - settings_two.enemy_2_width // 2
        self.NW_ypos = self.ypos - settings_two.enemy_2_height // 2
        self.SE_xpos = self.xpos + settings_two.enemy_2_width // 2
        self.SE_ypos = self.ypos + settings_two.enemy_2_height // 2

class Enemy_3(Base):
    def __init__(self, root, canvas, queue, tags):
        super(Enemy_3, self).__init__(root, canvas, queue,settings_three.enemy_3_lives, tags)
        self.xpos = random.randint(settings_three.enemy_3_width // 2,
                                       (settings_canvas.canvas_width - settings_three.enemy_3_width // 2))
        self.ypos = -(settings_three.enemy_3_height // 2)
        self.speed = settings_three.enemy_3_speed
        self.NW_xpos = self.xpos - settings_three.enemy_3_width // 2
        self.NW_ypos = self.ypos - settings_three.enemy_3_height // 2
        self.SE_xpos = self.xpos + settings_three.enemy_3_width // 2
        self.SE_ypos = self.ypos + settings_three.enemy_3_height // 2

    def run(self):
        self.canvas.move(self.image, 0, self.speed)
        self.ypos += self.speed
        # self.put_pos(
        #     (self.e_3_xpos - settings_three.enemy_3_width // 2),
        #     (self.e_3_ypos - settings_three.enemy_3_height // 2),
        #     (self.e_3_xpos + settings_three.enemy_3_width // 2),
        #     (self.e_3_ypos + settings_three.enemy_3_height // 2)
        # )
        self.NW_xpos = self.xpos - settings_three.enemy_3_width // 2
        self.NW_ypos = self.ypos - settings_three.enemy_3_height // 2
        self.SE_xpos = self.xpos + settings_three.enemy_3_width // 2
        self.SE_ypos = self.ypos + settings_three.enemy_3_height // 2
