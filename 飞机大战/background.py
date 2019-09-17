import tkinter
from settings import BackgroundSettings, CanvasSettings

settings_canvas = CanvasSettings()
settings_bg = BackgroundSettings()

class Background():
    def __init__(self,canvas):
        self.canvas = canvas
        self.backgroung_1 = tkinter.PhotoImage(file = settings_bg.background_1_path )
        self.bg_1 = self.canvas.create_image(settings_canvas.canvas_width / 2,
                                 settings_canvas.canvas_height / 2,
                                 anchor = tkinter.CENTER,
                                 image = self.backgroung_1)
        self.bg_1_pos = settings_canvas.canvas_height / 2
        self.backgroung_2 = tkinter.PhotoImage(file = settings_bg.background_2_path )
        self.bg_2 = self.canvas.create_image(settings_canvas.canvas_width / 2,
                                 - (settings_canvas.canvas_height / 2),
                                 anchor=tkinter.CENTER,
                                 image=self.backgroung_2)
        self.bg_2_pos =  -(settings_canvas.canvas_height / 2)

    def run(self):
        self.canvas.move(self.bg_1, 0, settings_bg.bg_speed)
        self.bg_1_pos += settings_bg.bg_speed
        self.canvas.move(self.bg_2, 0, settings_bg.bg_speed)
        self.bg_2_pos += settings_bg.bg_speed
        if self.bg_1_pos >= (settings_canvas.canvas_height * 1.5):
            self.canvas.move(self.bg_1, 0, -(settings_canvas.canvas_height * 2))
            self.bg_1_pos = - (settings_canvas.canvas_height / 2)
        if self.bg_2_pos >= (settings_canvas.canvas_height * 1.5):
            self.canvas.move(self.bg_2, 0, -(settings_canvas.canvas_height * 2))
            self.bg_2_pos = - (settings_canvas.canvas_height / 2)
