import tkinter
import time
import queue
import settings
import enemy
import background
import hero
from queuehandler import QueueHandler

settings_hero = settings.HeroSettings()
settings_canvas = settings.CanvasSettings()
settings_start_canvas = settings.StartCanvasSettings()
settings_one = settings.EnemyOneSettings()
settings_two = settings.EnemyTwoSettings()
settings_three = settings.EnemyThreeSettings()

enemy_count = 0

def create_bg(canvas):
    bg = background.Background(canvas)
    return bg

def create_hero(root, canvas, queue, tags):
    h = hero.Hero(root, canvas, queue, tags)
    h_img = canvas.create_image(h.hero_xpos, h.hero_ypos, image = h.bg_image, tags = tags)
    h.get_image(h_img)
    return h

def create_enemy_1(root, canvas, queue, tags, enemy_tags, enemies):
    # 创建enemy_1
    global enemy_count
    if len(enemies) < 5 and enemy_count % 2 == 0:
        e_1 = enemy.Enemy_1(root,canvas, queue, tags+str(enemy_count))
        e_1_img = canvas.create_image(e_1.xpos, e_1.ypos, image = e_1.bg_image, tags = tags+str(enemy_count))
        e_1.get_image(e_1_img)
        enemy_tags.append(tags+str(enemy_count))
        enemies.append(e_1)
        enemy_count += 1
        return e_1
    else:
        enemy_count += 1

def create_enemy_2(root, canvas, queue, tags, enemy_tags, enemies):
    # 创建enemy_2
    global enemy_count
    if len(enemies) <5 and enemy_count >= 3 and enemy_count % 5 == 0:
        e_2 = enemy.Enemy_2(root, canvas, queue, tags+str(enemy_count))
        e_2_img = canvas.create_image(e_2.xpos, e_2.ypos, image=e_2.bg_image, tags=tags + str(enemy_count))
        e_2.get_image(e_2_img)
        enemy_tags.append(tags+str(enemy_count))
        enemies.append(e_2)
        return e_2
    else:
        enemy_count += 1

def create_enemy_3(root, canvas, queue, tags, enemy_tags, enemies):
    # 创建enemy_3
    global enemy_count
    if len(enemies) <5 and enemy_count >= 5 and enemy_count % 8 == 0:
        e_3 = enemy.Enemy_3(root, canvas, queue, tags+str(enemy_count))
        e_3_img = canvas.create_image(e_3.xpos, e_3.ypos, image=e_3.bg_image, tags=tags + str(enemy_count))
        e_3.get_image(e_3_img)
        enemy_tags.append(tags+str(enemy_count))
        enemies.append(e_3)
        return e_3
    else:
        enemy_count += 1

def collapse_detecting(enemies, bullets, hero,canvas):
    # 碰撞检测
    # 敌机与子弹的碰撞检测
    for enemy in enemies:
        # 敌机与子弹的碰撞检测
        if canvas.coords(enemy.image) != []:
            for bullet in bullets:
                if enemy.NW_xpos <= bullet.b_xpos <= enemy.SE_xpos and enemy.NW_ypos <= bullet.b_ypos <= enemy.SE_ypos:
                    enemy.update_lives()
                    canvas.delete(bullet)
                    hero.bullets.remove(bullet)
            # 敌机与英雄机的碰撞检测
            if hero.NW_xpos <= enemy.SE_xpos and hero.SE_xpos >= enemy.NW_xpos \
                    and hero.NW_ypos <= enemy.SE_ypos and hero.SE_ypos >= enemy.NW_ypos:
                enemy.update_lives()
                hero.update_lives()
        else:
            enemies.remove(enemy)

def detecting_out_of_canvas(canvas, enemies, bullets, hero):
    # 检测物体是否超出画面
    for enemy in enemies:
        if enemy.NW_ypos > settings_canvas.canvas_height:
            canvas.delete(enemy)
            enemies.remove(enemy)
    for bullet in bullets:
        if bullet.b_ypos < 0 :
            canvas.delete(bullet)
            bullets.remove(bullet)
    if hero.NW_xpos <= 0 or hero.SE_xpos >= settings_canvas.canvas_width:
        hero.direction[0] = -hero.direction[0]
    if hero.NW_ypos >= settings_canvas.canvas_height or hero.SE_ypos <= 0:
        hero.direction[1] = -hero.direction[1]

def start_game(event, root, canvas, queue):
    game_flag = True
    canvas.delete("start")
    q_handler = QueueHandler(root, canvas, queue)
    enemy_tags = []
    enemies = []
    bg = create_bg(canvas)
    create_enemy_1(root, canvas, queue, "enemy_1_", enemy_tags, enemies)
    h = create_hero(root, canvas, queue, "hero")
    root.update()
    while game_flag:
        create_enemy_1(root, canvas, queue, "enemy_1_", enemy_tags, enemies)
        create_enemy_2(root, canvas, queue, "enemy_2_", enemy_tags, enemies)
        create_enemy_3(root, canvas, queue, "enemy_3_", enemy_tags, enemies)
        h.produce_bullet()
        root.update()
        for bullet in h.bullets:
            bullet.run()
        for enemy in enemies:
            enemy.run()
        h.run()
        bg.run()
        root.update()
        collapse_detecting(enemies, h.bullets, h, canvas)
        detecting_out_of_canvas(canvas, enemies, h.bullets, h)
        q_handler.handle()
        root.update()
        time.sleep(0.03)


def main():
    # 入口程序
    root = tkinter.Tk()
    root.title("PlaneWar")
    root.resizable(width = False, height=False)
    canvas = tkinter.Canvas(root, width = settings_canvas.canvas_width, height = settings_canvas.canvas_height)
    canvas.pack()
    q = queue.LifoQueue()

    # 起始界面
    start_img = tkinter.PhotoImage(file = settings_start_canvas.path)
    canvas.create_image(settings_canvas.canvas_width / 2,
                        settings_canvas.canvas_height / 2,
                        anchor = tkinter.CENTER,
                        image = start_img,
                        tags = "start")

    root.bind('<KeyPress-space>', lambda event: start_game(event, root, canvas, q))
    tkinter.mainloop()


main()