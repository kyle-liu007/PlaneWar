import tkinter
from tkinter import font
from settings import CanvasSettings

canvas_settings = CanvasSettings()

class Base():
    def __init__(self,root,canvas,queue, lives, tags):
        self.root = root
        self.canvas = canvas
        # 对象的生命值
        self.lives = lives
        # 对象的标签
        self.tags = tags
        # 传递消息的队列
        self.queue = queue

    # 创建图片
    # def create_image(self, x, y):
    #     img = tkinter.PhotoImage(file = self.path)
    #     self.canvas.create_image(x, y, image = img, tags=self.tags)

    # 获取图片
    def get_image(self, image):
        self.image = image

    # 将自己的对角坐标放入队列中
    # def put_pos(self, NW_x, NW_y, SE_x, SE_y):
    #     self.queue.put({(self.tags + '_pos'):(NW_x,NW_y,SE_x,SE_y)})

    # 更新自己的血量，同时检测血量是否为0
    def update_lives(self):
        self.lives -= 1
        self.living_test()

    # 检测血量是否为0, 若为0，则释放播放死亡动画的信号, 同时调用删除该图像的函数
    def living_test(self):
        if self.lives == 0:
            self.if_paly = True
            self.queue.put({"if_play":(self.if_paly, self.tags)})
            self.delete()

    # 删除血量为0的图像,若hero血量为0，则结束游戏，若敌军血量为0，则释放加分的信号
    def delete(self):
        if "enemy" in self.tags:
            self.queue.put({"if_score":(True, self.tags)})
        else:
            self.canvas.delete(self.tags)
            self.game_over()

    # 英雄的血量为0时，结束游戏, 释放显示结束画面的消息
    def game_over(self):
        self.canvas.destroy()
        self.show_over_canvas()

    # 释放结束画面的显示的消息
    def show_over_canvas(self):
        self.queue.put({"if_show_over_canvas":True})
