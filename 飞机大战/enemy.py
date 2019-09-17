import random
from base import Base
from settings import CanvasSettings,EnemyOneSettings,EnemyTwoSettings,EnemyThreeSettings

settings_canvas = CanvasSettings()
settings_one = EnemyOneSettings()
settings_two = EnemyTwoSettings()
settings_three = EnemyThreeSettings()

class Enemy_1(Base):
    def __init__(self, root, canvas, queue, tags):
        super(Enemy_1, self).__init__(root, canvas, queue,settings_one.enemy_1_path,
                                      settings_one.enemy_1_lives, tags)
        self.e_1_xpos = random.randint(settings_one.enemy_1_width//2,
                                       (settings_canvas.canvas_width - settings_one.enemy_1_width//2))
        self.e_1_ypos = -(settings_one.enemy_1_height//2)
        self.create_image(self.e_1_xpos, self.e_1_ypos)
        self.enemy.append(self.tags)
        self.speed = settings_one.enemy_1_speed
        self.put_pos((self.e_1_xpos - settings_one.enemy_1_width//2),
                     (self.e_1_ypos - settings_one.enemy_1_height//2),
                     (self.e_1_xpos + settings_one.enemy_1_width//2),
                     (self.e_1_ypos + settings_one.enemy_1_height//2)
        )

    def run(self):
        self.canvas.move(self.tags, 0, self.speed)
        self.e_1_ypos += self.speed
        self.put_pos(
            (self.e_1_xpos - settings_one.enemy_1_width // 2),
            (self.e_1_ypos - settings_one.enemy_1_height // 2),
            (self.e_1_xpos + settings_one.enemy_1_width // 2),
            (self.e_1_ypos + settings_one.enemy_1_height // 2)
        )

class Enemy_2(Base):
    def __init__(self, root, canvas, queue, tags):
        super(Enemy_2, self).__init__(root,canvas, queue, settings_two.enemy_2_path,
                                      settings_two.enemy_2_lives, tags)
        self.e_2_xpos = random.randint(settings_two.enemy_2_width // 2,
                                       (settings_canvas.canvas_width - settings_two.enemy_2_width // 2))
        self.e_2_ypos = -(settings_two.enemy_2_height // 2)
        self.create_image(self.e_2_xpos, self.e_2_ypos)
        self.enemy.append(self.tags)
        self.speed = settings_two.enemy_2_speed
        self.put_pos(
            (self.e_2_xpos - settings_two.enemy_2_width // 2),
            (self.e_2_ypos - settings_two.enemy_2_height // 2),
            (self.e_2_xpos + settings_two.enemy_2_width // 2),
            (self.e_2_ypos + settings_two.enemy_2_height // 2)
        )

    def run(self):
        self.canvas.move(self.tags, 0, self.speed)
        self.e_2_ypos += self.speed
        self.put_pos(
            (self.e_2_xpos - settings_two.enemy_2_width // 2),
            (self.e_2_ypos - settings_two.enemy_2_height // 2),
            (self.e_2_xpos + settings_two.enemy_2_width // 2),
            (self.e_2_ypos + settings_two.enemy_2_height // 2)
        )

class Enemy_3(Base):
    def __init__(self, root, canvas, queue, tags):
        super(Enemy_3, self).__init__(root, canvas, queue, settings_three.enemy_3_path,
                                      settings_three.enemy_3_lives, tags)
        self.e_3_xpos = random.randint(settings_three.enemy_3_width // 2,
                                       (settings_canvas.canvas_width - settings_three.enemy_3_width // 2))
        self.e_3_ypos = -(settings_three.enemy_3_height // 2)
        self.create_image(self.e_3_xpos, self.e_3_ypos)
        self.enemy.append(self.tags)
        self.speed = settings_three.enemy_3_speed
        self.put_pos(
            (self.e_3_xpos - settings_three.enemy_3_width // 2),
            (self.e_3_ypos - settings_three.enemy_3_height // 2),
            (self.e_3_xpos + settings_three.enemy_3_width // 2),
            (self.e_3_ypos + settings_three.enemy_3_height // 2)
        )

    def run(self):
        self.canvas.move(self.tags, 0, self.speed)
        self.e_3_ypos += self.speed
        self.put_pos(
            (self.e_3_xpos - settings_three.enemy_3_width // 2),
            (self.e_3_ypos - settings_three.enemy_3_height // 2),
            (self.e_3_xpos + settings_three.enemy_3_width // 2),
            (self.e_3_ypos + settings_three.enemy_3_height // 2)
        )
