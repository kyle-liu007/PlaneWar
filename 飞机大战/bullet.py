import tkinter
from settings import BulletSettings

settings_bullet = BulletSettings()

class Bullet():
    def __init__(self, canvas, tags, x, y):
        self.canvas = canvas
        self.tags = tags
        self.b_xpos = x
        self.b_ypos = y
        self.bullet_path = settings_bullet.bullet_path
        self.bullet = tkinter.PhotoImage(file = self.bullet_path)
        self.canvas.create_image(self.b_xpos,
                            self.b_ypos,
                            image = self.bullet,
                            tags = self.tags)
        self.speed = settings_bullet.bullet_speed

    def run(self):
        self.canvas.move(self.tags, 0, self.speed)
        self.b_ypos += self.speed