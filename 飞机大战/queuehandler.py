import tkinter
from tkinter import font
import time
from settings import PlayImageSettings, OverCanvasSettings

settings_playimage = PlayImageSettings()
settings_overcanvas = OverCanvasSettings()

class QueueHandler():
    def __init__(self, root, canvas, queue):
        self.root = root
        self.canvas = canvas
        self.queue = queue
        self.score = 0

    def handle(self):
        try :
            task = self.queue.get(block = False)
        except Exception:
            pass
        else:
            # 处理播放死亡动画的信号
            try:
                i, t = task.get("if_play")
            except Exception:
                pass
            else:
                if i:
                    self.play(t)
            try:
                i, t = task.get('if_score')
            except Exception:
                pass
            else:
                if i:
                    self.scoring(t)
            try:
                i = task.get("if_show_over_canvas")
            except Exception:
                pass
            else:
                self.show_over_canvas()

    def play(self, t):
        if "enemy_1" in t:
            print(self.canvas.coords(t))
            x = self.canvas.coords(t)[0]
            y = self.canvas.coords(t)[1]
            self.canvas.delete(t)
            for p in settings_playimage.enemy_1_down_image_list:
                enemy_1_down = tkinter.PhotoImage(file = p)
                self.canvas.create_image(x, y, anchor = tkinter.CENTER, image = enemy_1_down,
                                         tags = "enemy1_down")
                self.canvas.delete("enemy1_down")
        elif "enemy_2" in t:
            x = self.canvas.coords(t)[0]
            y = self.canvas.coors(t)[1]
            self.canvas.delete(t)
            for p in settings_playimage.enemy_2_down_image_list:
                enemy_2_down = tkinter.PhotoImage(file = p)
                self.canvas.create_image(x, y, anchor = tkinter.CENTER, image = enemy_2_down,
                                         tags = "enemy2_down")
                self.canvas.delete("enemy2_down")
        elif "enemy_3" in t:
            x = self.canvas.coords(t)[0]
            y = self.canvas.coors(t)[1]
            self.canvas.delete(t)
            for p in settings_playimage.enemy_3_down_image_list:
                enemy_3_down = tkinter.PhotoImage(file = p)
                self.canvas.create_image(x, y, anchor = tkinter.CENTER, image = enemy_3_down,
                                         tags = "enemy3_down")
                self.canvas.delete("enemy3_down")
        else:
            x = self.canvas.coords(t)[0]
            y = self.canvas.coors(t)[1]
            self.canvas.delete(t)
            for p in settings_playimage.hero_blowup_list:
                hero_blowup = tkinter.PhotoImage(file = p)
                self.canvas.create_image(x, y, anchor = tkinter.CENTER, image = hero_blowup,
                                         tags = "hero_blowup")
                self.canvas.delete("hero_blowup")

    def scoring(self, t):
        if "enemy_1" in t:
            self.score += 1

        if "enemy_2" in t:
            self.score += 2

        if "enemy_3" in t:
            self.score += 3

    def show_over_canvas(self):
        over_canvas = tkinter.Canvas(self.root, width = settings_overcanvas.canvas_width,
                                     height = settings_overcanvas.canvas_height)
        img = tkinter.PhotoImage(file = settings_overcanvas.canvas_path)
        over_canvas.create_image(settings_overcanvas.canvas_width / 2,
                                 settings_overcanvas.canvas_height / 2,
                                 anchor = tkinter.CENTER,
                                 image = img,
                                 tags = "over_image")
        time.sleep(0.5)
        over_canvas.delete("over_image")
        f = font.Font(font=("黑体", 30, 'bold'))
        over_canvas.create_text(200, 250, text="游戏结束", fill='green', font=f)
        over_canvas.create_text(200, 300, text="最高得分为：", fill='green', font=f)
        over_canvas.create_text(200, 350, text= str(self.score)+"分", fill = 'green', font=f)
        def quit_game():
            self.root.destroy()
        # b1 = tkinter.Button(over_canvas, text='retry', background='green', width=20)
        # b1.place(x=100, y=400)
        b2 = tkinter.Button(over_canvas, text='quit', width = 20)
        b2.place(x=100, y=450)
