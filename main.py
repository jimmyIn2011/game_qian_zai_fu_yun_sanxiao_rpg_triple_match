import pygame as pg
import random as rd
import numpy as np
import time


def chk(sa):
    flag = True
    for i in range(len(sa) - 1):
        if sa[i] is None or sa[i + 1] is None:
            return False
        if sa[i].name != sa[i + 1].name or sa[i].level != sa[i + 1].level or sa[i].level > 8:
            flag = False
            break
    return flag


def posi(hh, ll):
    return hh + ll * 14


def he(ks):
    for _ in range(9):
        for i in range(len(ks)-1):
            if ks[i] is None:
                ks[i] = ks[i + 1]
                ks[i + 1] = None
    for i in range(len(ks)):
        if ks[i] is None:
            ks[i] = Res(rd.choice(["剑", "刀", "枪", "符", "笔"]), 1)
    return ks


def triple_match(board):
    for m in range(14):
        for n in range(9):
            if m + 2 <= 13 and n + 2 <= 8:
                if chk([board[posi(m, n)], board[posi(m + 1, n)], board[posi(m + 2, n)],
                        board[posi(m, n + 1)], board[posi(m, n + 2)]]):
                    board[posi(m, n)].level += 1
                    board[posi(m + 1, n)].level += 1
                    board[posi(m + 2, n)] = None
                    board[posi(m, n + 1)].level += 1
                    board[posi(m, n + 2)] = None
                if chk([board[posi(m, n)], board[posi(m + 1, n)], board[posi(m + 2, n)],
                        board[posi(m + 2, n + 1)], board[posi(m + 2, n + 2)]]):
                    board[posi(m, n)] = None
                    board[posi(m + 1, n)].level += 1
                    board[posi(m + 2, n)].level += 1
                    board[posi(m + 2, n + 1)].level += 1
                    board[posi(m + 2, n + 2)] = None
                if chk([board[posi(m, n)], board[posi(m + 1, n + 2)], board[posi(m + 2, n + 2)],
                        board[posi(m, n + 1)], board[posi(m, n + 2)]]):
                    board[posi(m, n)] = None
                    board[posi(m + 1, n + 2)].level += 1
                    board[posi(m + 2, n + 2)] = None
                    board[posi(m, n + 1)].level += 1
                    board[posi(m, n + 2)].level += 1
                if chk([board[posi(m + 2, n)], board[posi(m, n + 2)], board[posi(m + 1, n + 2)],
                        board[posi(m + 2, n + 1)], board[posi(m + 2, n + 2)]]):
                    board[posi(m + 2, n)] = None
                    board[posi(m, n + 2)] = None
                    board[posi(m + 1, n + 2)].level += 1
                    board[posi(m + 2, n + 1)].level += 1
                    board[posi(m + 2, n + 2)].level += 1
                # 以上为L
                if chk([board[posi(m, n)], board[posi(m + 1, n)], board[posi(m + 2, n)],
                        board[posi(m + 1, n + 1)], board[posi(m + 1, n + 2)]]):
                    board[posi(m, n)] = None
                    board[posi(m + 1, n)].level += 1
                    board[posi(m + 2, n)] = None
                    board[posi(m + 1, n + 1)].level += 1
                    board[posi(m + 1, n + 2)].level += 1
                if chk([board[posi(m, n + 1)], board[posi(m + 1, n + 1)], board[posi(m + 2, n)],
                        board[posi(m + 2, n + 1)], board[posi(m + 2, n + 2)]]):
                    board[posi(m, n + 1)].level += 1
                    board[posi(m + 1, n + 1)].level += 1
                    board[posi(m + 2, n)] = None
                    board[posi(m + 2, n + 1)].level += 1
                    board[posi(m + 2, n + 2)] = None
                if chk([board[posi(m, n)], board[posi(m + 1, n + 1)], board[posi(m + 2, n + 1)],
                        board[posi(m, n + 1)], board[posi(m, n + 2)]]):
                    board[posi(m, n)] = None
                    board[posi(m + 1, n + 1)].level += 1
                    board[posi(m + 2, n + 1)].level += 1
                    board[posi(m, n + 1)].level += 1
                    board[posi(m, n + 2)] = None
                if chk([board[posi(m + 1, n)], board[posi(m, n + 2)], board[posi(m + 1, n + 1)],
                        board[posi(m + 1, n + 2)], board[posi(m + 2, n + 2)]]):
                    board[posi(m + 1, n)].level += 1
                    board[posi(m, n + 2)] = None
                    board[posi(m + 1, n + 1)].level += 1
                    board[posi(m + 1, n + 2)].level += 1
                    board[posi(m + 2, n + 2)] = None
                # 以上为T
            if m + 4 <= 13 and chk([board[posi(m, n)], board[posi(m + 1, n)], board[posi(m + 2, n)],
                                    board[posi(m + 3, n)], board[posi(m + 4, n)]]):
                board[posi(m, n)] = None
                board[posi(m + 1, n)].level += 1
                board[posi(m + 2, n)].level += 1
                board[posi(m + 3, n)].level += 1
                board[posi(m + 4, n)] = None
            if n + 4 <= 8 and chk([board[posi(m, n)], board[posi(m, n + 1)], board[posi(m, n + 2)],
                                   board[posi(m, n + 3)], board[posi(m, n + 4)]]):
                board[posi(m, n)] = None
                board[posi(m, n + 1)].level += 1
                board[posi(m, n + 2)].level += 1
                board[posi(m, n + 3)].level += 1
                board[posi(m, n + 4)] = None
            # 以上为5个
            if m + 3 <= 13 and chk([board[posi(m, n)], board[posi(m + 1, n)], board[posi(m + 2, n)],
                                    board[posi(m + 3, n)]]):
                board[posi(m, n)] = None
                board[posi(m + 1, n)].level += 1
                board[posi(m + 2, n)].level += 1
                board[posi(m + 3, n)] = None
            if n + 3 <= 8 and chk([board[posi(m, n)], board[posi(m, n + 1)], board[posi(m, n + 2)],
                                   board[posi(m, n + 3)]]):
                board[posi(m, n)] = None
                board[posi(m, n + 1)].level += 1
                board[posi(m, n + 2)].level += 1
                board[posi(m, n + 3)] = None
            # 以上为4个
            if m + 2 <= 13 and chk([board[posi(m, n)], board[posi(m + 1, n)], board[posi(m + 2, n)]]):
                board[posi(m, n)] = None
                board[posi(m + 1, n)].level += 1
                board[posi(m + 2, n)] = None
            if n + 2 <= 8 and chk([board[posi(m, n)], board[posi(m, n + 1)], board[posi(m, n + 2)]]):
                board[posi(m, n)] = None
                board[posi(m, n + 1)].level += 1
                board[posi(m, n + 2)] = None
    for iiiii in range(14 * 9):
        if board[iiiii] is not None:
            board[iiiii].upd()
    for iiiii in range(14):
        board[iiiii+0], board[iiiii+14], board[iiiii+28], board[iiiii+42], board[iiiii+56], board[iiiii+70], board[iiiii+84], board[iiiii+98], board[iiiii+112] = he([board[iiiii+0], board[iiiii+14], board[iiiii+28], board[iiiii+42], board[iiiii+56], board[iiiii+70], board[iiiii+84], board[iiiii+98], board[iiiii+112]])
    return board


def get_qh():
    with open("./settings.filename", 'r') as file:
        lliinneess = file.readlines()
        return {'剑': int(lliinneess[2].strip()), '刀': int(lliinneess[3].strip()),
                '枪': int(lliinneess[4].strip()),
                '符': int(lliinneess[5].strip()), '笔': int(lliinneess[6].strip())}


def get_gs():
    with open("./settings.filename", 'r') as file:
        return int(file.readline().strip())


def get_ls():
    with open("./settings.filename", 'r') as file:
        return int(file.readlines()[1].strip())


def write_all():
    with open('./settings.filename', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    if lines:
        lines[0] = str(gs) + '\n'
        lines[1] = str(lingshi) + '\n'
        lines[2] = str(qh['剑']) + '\n'
        lines[3] = str(qh['刀']) + '\n'
        lines[4] = str(qh['符']) + '\n'
        lines[5] = str(qh['笔']) + '\n'
    with open('./settings.filename', 'w', encoding='utf-8') as file:
        file.writelines(lines)


class Res:
    def __init__(self, name, lv):
        self.name = name
        self.level = lv
        self.attack = qh[self.name] + rd.randint(17, 21) + 5 * self.level
        self.speed = 13 - self.level
        self.xl = 0

    def upd(self):
        self.speed = 13 - self.level
        self.attack = qh[self.name] + rd.randint(17, 21) + 5 * self.level


class Enemy:
    def __init__(self, bloods, position, speed, att):
        self.b = bloods
        self.tb = bloods
        self.pic = pg.image.load("./images/yaoshou1.png")
        self.p = position
        self.s = speed
        self.a = att
        self.fl = False


def draw_scaled_weapon(sc, imagess, position):
    original_image = imagess
    scale_factor = np.array([0.5, 0.5])
    scaled_size = (original_image.get_width() * scale_factor[0],
                   original_image.get_height() * scale_factor[1])
    scaled_image = pg.transform.scale(original_image, (int(scaled_size[0]), int(scaled_size[1])))
    sc.blit(scaled_image, position)


pg.init()
pg.display.init()
screen = pg.display.set_mode([800, 800])
pg.display.set_caption("千载浮云")
gs = get_gs()  # 通关数量
lingshi = get_ls()  # 灵石数量->通关+关卡数*4
qh = get_qh()  # 武器强化等级
weapon = {'剑': pg.image.load("./images/wooden_sword.png"), '枪': pg.image.load("./images/wooden_gun.png"),
          '刀': pg.image.load("./images/wooden_blade.png"), '符': pg.image.load("./images/fulu.png"),
          '笔': pg.image.load("./images/wooden_pen.png")}
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
GREEN = [0, 255, 0]
BLUE = [0, 0, 255]
RED = [255, 0, 0]
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GOLDEN = (205, 127, 50)
PYCOLOR = (90, 192, 241)
BROWN = [128, 64, 0]
clrs = [WHITE, GREEN, BLUE, PURPLE, YELLOW, BLACK, RED, GOLDEN]
hcmap = [[5, 5], [60, 5], [115, 5], [170, 5], [225, 5], [280, 5], [335, 5], [390, 5], [445, 5], [500, 5], [555, 5],
         [610, 5], [665, 5], [720, 5],
         [5, 60], [60, 60], [115, 60], [170, 60], [225, 60], [280, 60], [335, 60], [390, 60], [445, 60], [500, 60],
         [555, 60], [610, 60], [665, 60], [720, 60],
         [5, 115], [60, 115], [115, 115], [170, 115], [225, 115], [280, 115], [335, 115], [390, 115], [445, 115],
         [500, 115], [555, 115], [610, 115], [665, 115], [720, 115],
         [5, 170], [60, 170], [115, 170], [170, 170], [225, 170], [280, 170], [335, 170], [390, 170], [445, 170],
         [500, 170], [555, 170], [610, 170], [665, 170], [720, 170],
         [5, 225], [60, 225], [115, 225], [170, 225], [225, 225], [280, 225], [335, 225], [390, 225], [445, 225],
         [500, 225], [555, 225], [610, 225], [665, 225], [720, 225],
         [5, 280], [60, 280], [115, 280], [170, 280], [225, 280], [280, 280], [335, 280], [390, 280], [445, 280],
         [500, 280], [555, 280], [610, 280], [665, 280], [720, 280],
         [5, 335], [60, 335], [115, 335], [170, 335], [225, 335], [280, 335], [335, 335], [390, 335], [445, 335],
         [500, 335], [555, 335], [610, 335], [665, 335], [720, 335],
         [5, 390], [60, 390], [115, 390], [170, 390], [225, 390], [280, 390], [335, 390], [390, 390], [445, 390],
         [500, 390], [555, 390], [610, 390], [665, 390], [720, 390],
         [5, 445], [60, 445], [115, 445], [170, 445], [225, 445], [280, 445], [335, 445], [390, 445], [445, 445],
         [500, 445], [555, 445], [610, 445], [665, 445], [720, 445]]
mapall = [None for i in range(14 * 9)]
# 14/行；9/列
scene = 1
back = pg.Rect(0, 750, 800, 50)
bg1 = pg.image.load("./images/bg.png")
lspng = pg.image.load("./images/nbstone.png")
cgbtn = pg.Rect(288, 595, 220, 95)
qhbtn = [pg.Rect(115, 141, 100, 50), pg.Rect(345, 141, 100, 50), pg.Rect(575, 141, 100, 50),
         pg.Rect(115, 311, 100, 50), pg.Rect(345, 311, 100, 50)]
lst = {0: '剑', 1: '刀', 2: '枪', 3: '符', 4: '笔'}
lst2 = {'剑': BLUE, '刀': GREEN, '枪': BROWN, '符': PURPLE, '笔': YELLOW}
now_tpe = None
smallgs = 0  # 小关数
enemies = []
attack = []   # [attack, pos, clr]
start_time = 0
steps = 0  # 步数
onmove = False
move_square = -1
movex = 0
win = False
movey = 0
blood = 0
running = True
while running:
    screen.fill(WHITE)
    for event in pg.event.get():
        pos = pg.mouse.get_pos()
        if event.type == pg.QUIT:
            running = False
            write_all()
        if event.type == pg.MOUSEBUTTONDOWN:
            if scene == 1:
                if back.collidepoint(pos):
                    scene = 2
                if cgbtn.collidepoint(pos):
                    smallgs = 1
                    scene = 3
                    now_tpe = 1
                    blood = 1000
                    mapall = [Res(rd.choice(["剑", "刀", "枪", "符", "笔"]), 1) for _ in range(14 * 9)]
                    # mapall = triple_match(mapall)
                    steps = 15
            elif scene == 2:
                if back.collidepoint(pos):
                    scene = 1
                for i in range(len(qhbtn)):
                    if qhbtn[i].collidepoint(pos):
                        if lingshi >= qh[lst[i]] + 1:
                            lingshi -= qh[lst[i]] + 1
                            qh[lst[i]] += 1
            elif scene == 3:
                for i in range(len(hcmap)):
                    if pg.Rect(hcmap[i][0], hcmap[i][1] + 250, 50, 50).collidepoint(pos) and now_tpe == 1:
                        if move_square != -1:
                            hcmap[move_square][0] = movex
                            hcmap[move_square][1] = movey
                            move_square = -1
                            movex = 0
                            movey = 0
                        move_square = i
                        onmove = True
                        movex = hcmap[move_square][0]
                        movey = hcmap[move_square][1]
                        hcmap[move_square][0] = pos[0]
                        hcmap[move_square][1] = pos[1]
            elif scene == 4:
                if back.collidepoint(pos):
                    scene = 1
        elif event.type == pg.MOUSEMOTION:
            if scene == 3 and onmove:
                hcmap[move_square][0] = pos[0]
                hcmap[move_square][1] = pos[1]
        elif event.type == pg.MOUSEBUTTONUP:
            if onmove and scene == 3:
                if move_square >= 14:
                    over = pg.Rect(hcmap[move_square][0], hcmap[move_square][1], 50, 50).clip(
                        hcmap[move_square - 14][0],
                        hcmap[move_square - 14][1] + 250, 50, 50)
                    if over.width * over.height >= 1000 and steps > 0:
                        tmp = mapall[move_square]
                        mapall[move_square] = mapall[move_square - 14]
                        mapall[move_square - 14] = tmp
                        steps -= 1
                        mapall = triple_match(mapall)
                if move_square < 112:
                    over = pg.Rect(hcmap[move_square][0], hcmap[move_square][1], 50, 50).clip(
                        hcmap[move_square + 14][0],
                        hcmap[move_square + 14][1] + 250, 50, 50)
                    if over.width * over.height >= 1000 and steps > 0:
                        tmp = mapall[move_square]
                        mapall[move_square] = mapall[move_square + 14]
                        mapall[move_square + 14] = tmp
                        steps -= 1
                        mapall = triple_match(mapall)
                if move_square % 14 != 0:
                    over = pg.Rect(hcmap[move_square][0], hcmap[move_square][1], 50, 50).clip(hcmap[move_square - 1][0],
                                                                                              hcmap[move_square - 1][
                                                                                                  1] + 250,
                                                                                              50, 50)
                    if over.width * over.height >= 1000 and steps > 0:
                        tmp = mapall[move_square]
                        mapall[move_square] = mapall[move_square - 1]
                        mapall[move_square - 1] = tmp
                        steps -= 1
                        mapall = triple_match(mapall)
                if move_square % 14 != 13:
                    over = pg.Rect(hcmap[move_square][0], hcmap[move_square][1], 50, 50).clip(hcmap[move_square + 1][0],
                                                                                              hcmap[move_square + 1][
                                                                                                  1] + 250,
                                                                                              50, 50)
                    if over.width * over.height >= 1000 and steps > 0:
                        tmp = mapall[move_square]
                        mapall[move_square] = mapall[move_square + 1]
                        mapall[move_square + 1] = tmp
                        steps -= 1
                        mapall = triple_match(mapall)
                hcmap[move_square][0] = movex
                hcmap[move_square][1] = movey
                move_square = -1
                onmove = False
                movex = 0
                movey = 0
                if steps == 0:
                    now_tpe = 2
                    lasdasda = rd.randint(5, 20)
                    enemies = [Enemy(rd.randint(100, 500), [rd.randint(0, 700),
                                                            rd.randint(0, 600) - 599],
                                     rd.randint(2, 7), rd.randint(10, 65)) for _ in range(lasdasda)]
    if scene == 1:
        screen.blit(bg1, [0, 0])
        pg.draw.rect(screen, PYCOLOR, back)
        screen.blit(pg.font.SysFont("华文楷体", 30).render("            培养", True, BLACK), [1, 751])
        pg.draw.rect(screen, (84, 237, 184), cgbtn)
        screen.blit(pg.font.SysFont("华文楷体", 60).render("第 %s 关" % gs, True, BLACK), [cgbtn[0] + 1, cgbtn[1] + 1])
        screen.blit(pg.font.SysFont("华文楷体", 55).render("千载浮云", True, BLACK), [180, 110])
    elif scene == 2:
        pg.draw.rect(screen, PYCOLOR, back)
        screen.blit(pg.font.SysFont("华文楷体", 30).render("            退出", True, BLACK), [1, 751])
        screen.blit(lspng, [0, 0])
        screen.blit(pg.font.SysFont("华文楷体", 44).render(str(lingshi), True, BLACK), [100, 0])
        screen.blit(weapon['剑'], [10, 110])
        screen.blit(pg.font.SysFont("华文楷体", 28).render("+" + str(qh['剑']), True, BLACK), [115, 110])
        pg.draw.rect(screen, YELLOW, qhbtn[0])
        screen.blit(pg.font.SysFont("华文楷体", 33).render("强化+1", True, BLACK), [116, 142])
        screen.blit(weapon['刀'], [240, 110])
        screen.blit(pg.font.SysFont("华文楷体", 28).render("+" + str(qh['刀']), True, BLACK), [345, 110])
        pg.draw.rect(screen, YELLOW, qhbtn[1])
        screen.blit(pg.font.SysFont("华文楷体", 33).render("强化+1", True, BLACK), [346, 142])
        screen.blit(weapon['枪'], [470, 110])
        screen.blit(pg.font.SysFont("华文楷体", 28).render("+" + str(qh['枪']), True, BLACK), [575, 110])
        pg.draw.rect(screen, YELLOW, qhbtn[2])
        screen.blit(pg.font.SysFont("华文楷体", 33).render("强化+1", True, BLACK), [576, 142])
        screen.blit(weapon['符'], [10, 280])
        screen.blit(pg.font.SysFont("华文楷体", 28).render("+" + str(qh['符']), True, BLACK), [115, 280])
        pg.draw.rect(screen, YELLOW, qhbtn[3])
        screen.blit(pg.font.SysFont("华文楷体", 33).render("强化+1", True, BLACK), [116, 312])
        screen.blit(weapon['笔'], [240, 280])
        screen.blit(pg.font.SysFont("华文楷体", 28).render("+" + str(qh['笔']), True, BLACK), [345, 280])
        pg.draw.rect(screen, YELLOW, qhbtn[4])
        screen.blit(pg.font.SysFont("华文楷体", 33).render("强化+1", True, BLACK), [346, 312])
    elif scene == 3:
        start_time += 1
        for i in range(len(mapall)):
            if mapall[i] is not None and move_square != i:
                pg.draw.rect(screen, clrs[mapall[i].level - 1 if mapall[i].level <= 8 else -1],
                             [hcmap[i][0], hcmap[i][1] + 250, 50, 50])
                draw_scaled_weapon(screen, weapon[mapall[i].name], [hcmap[i][0], hcmap[i][1] + 250])
                pg.draw.rect(screen, BLACK, [hcmap[i][0], hcmap[i][1] + 250, 50, 50], 1)
                if now_tpe == 2:
                    mapall[i].xl += 1
                if mapall[i].xl > mapall[i].speed * 50 and mapall[i].level >= 2 and now_tpe == 2:
                    mapall[i].xl = 0
                    attack.append([mapall[i].attack, [hcmap[i][0] + rd.randint(1, 49), hcmap[i][1] + 250],
                                   lst2[mapall[i].name], True])
        if move_square != -1 and mapall[move_square] is not None:
            pg.draw.rect(screen, clrs[mapall[move_square].level - 1 if mapall[move_square].level <= 8 else -1],
                         [hcmap[move_square][0], hcmap[move_square][1], 50, 50])
            draw_scaled_weapon(screen, weapon[mapall[move_square].name],
                               [hcmap[move_square][0], hcmap[move_square][1]])
            pg.draw.rect(screen, BLACK, [hcmap[move_square][0], hcmap[move_square][1], 50, 50], 1)
        pg.draw.rect(screen, RED, [back[0], back[1], back[2] * (blood / 1000), back[3]])
        screen.blit(pg.font.SysFont("华文楷体", 30).render("血量：" + str(blood), True, BLACK), [1, 751])
        if start_time >= 20 and onmove is False:
            start_time -= 20
            mapall = triple_match(mapall)
        if steps == 0:
            now_tpe = 2
        if now_tpe == 1:
            screen.blit(pg.font.SysFont("华文楷体", 30).render("剩余步数: " + str(steps), True, BLACK), [0, 0])
            screen.blit(pg.font.SysFont("华文楷体", 50).render("第" + str(smallgs) + "关", True, BLACK), [100, 50])
        elif now_tpe == 2:
            nt = 0
            for i in range(len(attack)):
                if attack[i][3] is True:
                    for j in range(len(enemies)):
                        over2 = pg.Rect(enemies[j].p[0], enemies[j].p[1], 100, 100).clip(pg.Rect(attack[i][1][0], attack[i][1][1], 1, 50))
                        if over2.width * over2.height > 0 and enemies[j].fl is False:
                            attack[i][3] = False
                            enemies[j].b -= attack[i][0]
                            if enemies[j].b <= 0:
                                enemies[j].fl = True
                    attack[i][1][1] -= 1
                    if attack[i][1][1] < 0:
                        attack[i][3] = False
                    pg.draw.line(screen, attack[i][2], attack[i][1], [attack[i][1][0], attack[i][1][1] - 50], 1)
            for i in range(len(enemies)):
                if enemies[i].p[1] + 100 > 0 and enemies[i].p[1] < 800 and enemies[i].fl is False:
                    screen.blit(enemies[i].pic, enemies[i].p)
                    pg.draw.rect(screen, RED, [enemies[i].p[0], enemies[i].p[1] - 10, 100 * (enemies[i].b / enemies[i].tb), 10])
                if enemies[i].fl is False:
                    nt += 1
                enemies[i].p[1] += enemies[i].s / 20
                if enemies[i].p[1] >= 800 and enemies[i].fl is False:
                    blood -= enemies[i].a
                    enemies[i].fl = True
                    if blood <= 0:
                        win = False
                        time.sleep(0.5)
                        scene = 4
            if nt == 0 and scene == 3:
                now_tpe = 1
                steps = 15
                attack = []
                enemies = []
                if smallgs >= 50:
                    win = True
                    time.sleep(0.5)
                    scene = 4
                    lingshi += gs * 10
                    gs += 1
                    smallgs = 0
                smallgs += 1
    elif scene == 4:
        screen.blit(bg1, [0, 0])
        screen.blit(pg.font.SysFont("华文楷体", 50).render(f"你{'赢' if win else '输'}了", True, GREEN if win else RED), [180, 110])
        pg.draw.rect(screen, PYCOLOR, back)
        screen.blit(pg.font.SysFont("华文楷体", 30).render("      回到首页", True, BLACK), [1, 751])
    pg.display.flip()
pg.quit()
