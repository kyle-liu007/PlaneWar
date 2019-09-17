import tkinter
import settings
import enemy
import background
import hero
import queuehandler


def create_bg(canvas):
    bg = background.Background()
    return bg

def create_enemy_1(root, canvas, queue, tags, enemies, enemy_count):
    # 创建enemy_1
    if len(enemies) < 5:
        e_1 = enemy.Enemy_1(root,canvas, queue, tags+str(enemy_count))

        enemies.append(e_1)
        enemy_count += 1
    else:
        pass

def create_enemy_2(root, canvas, queue, tags, enemies, enemy_count):
    # 创建enemy_2
    if enemy_count >= 3 and enemy_count % 3 == 0:
        e_2 = enemy.Enemy_2(root, canvas, queue, tags+str(enemy_count))
        enemies.append(e_2)
    else:
        pass

def create_enemy_3(root, canvas, queue, tags, enemies, enemy_count):
    # 创建enemy_3
    if enemy_count >= 5 and enemy_count % 5 == 0:
        e_3 = enemy.Enemy_3(root, canvas, queue, tags+str(enemy_count))
        enemies.append(e_3)
    else:
        pass

def collapse_detecting(enemies, bullets, hero, queue, canvas):
    # 碰撞检测
    # 敌机与子弹的碰撞检测
    coords = queue.get(block = False)
    for enemy in enemies:
        e_t = canvas.gettags(enemy)
        e_x_1, e_y_1, e_x_2, e_y_2 = coords.get(e_t+"_pos")
        # 敌机与子弹的碰撞检测
        for bullet in bullets:
            if e_x_1 <= bullet.b_xpos <= e_x_2 and e_y_1 <= bullet.b_ypos <= e_y_2:
                enemy.update_lives()
                canvas.delete(bullet)
                hero.bullets.remove(bullet)
        # 敌机与英雄机的碰撞检测
        h_t = canvas.gettags(hero)
        h_x_1, h_y_1, h_x_2, h_y_2 = coords.get(h_t+"_pos")
        if h_x_1 <= e_x_2 and h_x_2 >= e_x_1 and h_y_1 <= e_y_2 and h_y_2 >= e_y_1:
            enemy.update_lives()
            hero.update_lives()

def start_game(event, root, canvas, queue):
    q_handler = queuehandler.QueueHandler(root, canvas, queue)
    enemies = []
    enemy_count = 0
    create_enemy_1(root, canvas, queue, "enemy_1", enemies, enemy_count)
    h = hero.Hero(root, canvas, queue, "hero")
    bg = create_bg(canvas)
    while True:
        create_enemy_1(root, canvas, queue, "enemy_1", enemies, enemy_count)
        create_enemy_2(root, canvas, queue, "enemy_2", enemies, enemy_count)
        create_enemy_3(root, canvas, queue, "enemy_3", enemies, enemy_count)
        h.produce_bullet()
        for bullet in h.bullets:
            bullet.run()
        for enemy in enemies:
            enemy.run()
        collapse_detecting(enemies, h.bullets, h, queue, canvas)
        q_handler.handle()

def main():
    # 入口程序
