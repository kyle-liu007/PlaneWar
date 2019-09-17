from settings import HeroSettings,CanvasSettings
from base import Base
from bullet import Bullet

settings_hero = HeroSettings()
settings_canvas = CanvasSettings()

class Hero(Base):
    def __init__(self, root, canvas, queue, tags):
        super(Hero, self).__init__(root, canvas, queue, settings_hero.hero_path,
                                   settings_hero.hero_lives, tags)
        self.direction = (0, 0)
        self.count = 0
        self.score = 0
        self.bullets = []
        self.hero_xpos = settings_canvas.canvas_width // 2
        self.hero_ypos = settings_canvas.canvas_height - (settings_hero.hero_height / 2)
        self.create_image(self.hero_xpos, self.hero_ypos)
        self.put_pos(
            (self.hero_xpos - settings_hero.hero_width / 2),
            (self.hero_ypos - settings_hero.hero_height / 2),
            (self.hero_xpos + settings_hero.hero_width / 2),
            (self.hero_ypos + settings_hero.hero_height / 2)
        )
        self.root.bind('<KeyPress-Left>', self.key_press)
        self.root.bind('<KeyPress-Up>', self.key_press)
        self.root.bind('<KeyPress-Down>', self.key_press)
        self.root.bind('<KeyPress-Right>', self.key_press)
        self.speed = settings_hero.hero_speed

    def run(self):
        x, y = self.direction
        if self.hero_xpos == 0 or self.hero_xpos == settings_canvas.canvas_width:
            x = 0
        if self.hero_ypos == 0 or self.hero_ypos == settings_canvas.canvas_height:
            y = 0
        xspeed = self.speed * x
        yspeed = self.speed * y
        self.canvas.move(self.tags, xspeed, yspeed)
        self.hero_xpos += xspeed
        self.hero_ypos += yspeed
        self.put_pos(
            (self.hero_xpos - settings_hero.hero_width / 2),
            (self.hero_ypos - settings_hero.hero_height / 2),
            (self.hero_xpos + settings_hero.hero_width / 2),
            (self.hero_ypos + settings_hero.hero_height / 2)
        )

    def key_press(self, event):
        code = event.keycode
        if code == 38: # 上
            self.direction = (0, -1)
        if code == 40: # 下
            self.direction = (0, 1)
        if code == 37: # 左
            self.direction = (-1, 0)
        if code == 39: # 右
            self.direction = (1, 0)

    def produce_bullet(self):
        self.count += 1
        for id in range((self.count - 1) * 3, self.count * 3):
            bullet = Bullet(self.canvas,
                            "bullet_" + str(id),
                            self.hero_xpos,
                            (self.hero_ypos - settings_hero.hero_height / 2),
            )
            self.bullets.append(bullet)

