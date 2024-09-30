import tkinter
import time
from tkinter import messagebox

wpos = "left"
gpos = "left"
vpos = "left"
lbon = True
click = "NULL"
wolfonb = False
goatonb = False
vagetableonb = False
onboat = "off"


def wgoleft():
    global wpos
    goleft(Iwolf, "wolf", 895, 365)
    canvas.delete("wolf")
    canvas.create_image(65, 341, image=Iwolf, tag="wolf")
    wpos = "left"


def ggoleft():
    global gpos
    goleft(Igoat, "goat", 925, 370)
    canvas.delete("goat")
    canvas.create_image(200, 341, image=Igoat, tag="goat")
    gpos = "left"


def vgoleft():
    global vpos
    goleft(Ivagetable, "vagetable", 915, 398)
    canvas.delete("vagetable")
    canvas.create_image(285, 390, image=Ivagetable, tag="vagetable")
    vpos = "left"


def wgoright():
    global wpos
    goright(Iwolf, "wolf", 540, 365)
    canvas.delete("wolf")
    canvas.create_image(1135, 290, image=Iwolf, tag="wolf")
    wpos = "right"


def ggoright():
    global gpos
    goright(Igoat, "goat", 570, 370)
    canvas.delete("goat")
    canvas.create_image(1020, 310, image=Igoat, tag="goat")
    gpos = "right"


def vgoright():
    global vpos
    goright(Ivagetable, "vagetable", 560, 398)
    canvas.delete("vagetable")
    canvas.create_image(1080, 440, image=Ivagetable, tag="vagetable")
    vpos = "right"


def goright(name, tmp, x, y):
    global lbon
    for i in range(72):
        canvas.delete(tmp)
        canvas.delete("boat")
        canvas.create_image(x+i*5, y, image=name, tag=tmp)
        canvas.create_image(490+i*5, 341, image=Iboat, tag="boat")
        time.sleep(0.025)
        canvas.update()
    lbon = False


def goleft(name, tmp, x, y):
    global lbon
    for i in range(72):
        canvas.delete(tmp)
        canvas.delete("boat")
        canvas.create_image(x-i*5, y, image=name, tag=tmp)
        canvas.create_image(845-i*5, 341, image=Iboat, tag="boat")
        time.sleep(0.025)
        canvas.update()
    lbon = True


def bgoright():
    global lbon
    for i in range(72):
        canvas.delete("boat")
        canvas.create_image(490+i*5, 341, image=Iboat, tag="boat")
        time.sleep(0.025)
        canvas.update()
    lbon = False


def bgoleft():
    global lbon
    for i in range(72):
        canvas.delete("boat")
        canvas.create_image(845-i*5, 341, image=Iboat, tag="boat")
        time.sleep(0.025)
        canvas.update()
    lbon = True


def callback(event):
    global click, onboat, wpos, wolfonb, gpos, goatonb, vpos, vagetableonb, lbon
    x = event.x
    y = event.y
    if onboat == "off" and wolfonb == False and goatonb == False and vagetableonb == False:
        if wpos == "left" and lbon == True:
            if (x >= 0 and x <= 135) and (y >= 229 and y <= 453):
                click = "wolf"
                onboat = "on"
        elif wpos == "right" and lbon == False:
            if (x >= 1070 and x <= 1205) and (y >= 178 and y <= 402):
                click = "wolf"
                onboat = "on"
        if gpos == "left" and lbon == True:
            if (x >= 135 and x <= 265) and (y >= 224 and y <= 458):
                click = "goat"
                onboat = "on"
        elif gpos == "right" and lbon == False:
            if (x >= 955 and x <= 1085) and (y >= 243 and y <= 377):
                click = "goat"
                onboat = "on"
        if vpos == "left" and lbon == True:
            if (x >= 235 and x <= 335) and (y >= 340 and y <= 440):
                click = "vagetable"
                onboat = "on"
        elif vpos == "right" and lbon == False:
            if (x >= 1030 and x <= 1130) and (y >= 390 and y <= 490):
                click = "vagetable"
                onboat = "on"
    elif onboat == "on" and (wolfonb == True or goatonb == True or vagetableonb == True):
        if wpos == "left" and wolfonb == True and lbon == True:
            if (x >= 475 and x <= 610) and (y >= 253 and y <= 477):
                click = "wolf"
                onboat = "off"
        elif wpos == "right" and wolfonb == True and lbon == False:
            if (x >= 830 and x <= 965) and (y >= 253 and y <= 477):
                click = "wolf"
                onboat = "off"
        if gpos == "left" and goatonb == True and lbon == True:
            if (x >= 505 and x <= 635) and (y >= 303 and y <= 437):
                click = "goat"
                onboat = "off"
        elif gpos == "right" and goatonb == True and lbon == False:
            if (x >= 860 and x <= 995) and (y >= 303 and y <= 437):
                click = "goat"
                onboat = "off"
        if vpos == "left" and vagetableonb == True and lbon == True:
            if (x >= 510 and x <= 610) and (y >= 348 and y <= 448):
                click = "vagetable"
                onboat = "off"
        elif vpos == "right" and vagetableonb == True and lbon == False:
            if (x >= 865 and x <= 965) and (y >= 348 and y <= 448):
                click = "vagetable"
                onboat = "off"
    print(click)
    print(onboat)
    clickimg()


def clickimg():
    global click, wpos, wolfonb, gpos, goatonb, vpos, vagetableonb
    if click == "wolf":
        canvas.delete("wolf")
        canvas.delete("boat")
        if wpos == "left":
            if wolfonb == False:
                canvas.create_image(540, 365, image=Iwolf, tag="wolf")
                wolfonb = True
            else:
                canvas.create_image(65, 341, image=Iwolf, tag="wolf")
                wolfonb = False
            canvas.create_image(490, 341, image=Iboat, tag="boat")
        else:
            if wolfonb == False:
                canvas.create_image(895, 365, image=Iwolf, tag="wolf")
                wolfonb = True
            else:
                canvas.create_image(1135, 290, image=Iwolf, tag="wolf")
                wolfonb = False
            canvas.create_image(845, 341, image=Iboat, tag="boat")
    elif click == "goat":
        canvas.delete("goat")
        canvas.delete("boat")
        if gpos == "left":
            if goatonb == False:
                canvas.create_image(570, 370, image=Igoat, tag="goat")
                goatonb = True
            else:
                canvas.create_image(200, 341, image=Igoat, tag="goat")
                goatonb = False
            canvas.create_image(490, 341, image=Iboat, tag="boat")
        else:
            if goatonb == False:
                canvas.create_image(925, 370, image=Igoat, tag="goat")
                goatonb = True
            else:
                canvas.create_image(1020, 310, image=Igoat, tag="goat")
                goatonb = False
            canvas.create_image(845, 341, image=Iboat, tag="boat")
    elif click == "vagetable":
        canvas.delete("vagetable")
        canvas.delete("boat")
        if vpos == "left":
            if vagetableonb == False:
                canvas.create_image(
                    560, 398, image=Ivagetable, tag="vagetable")
                vagetableonb = True
            else:
                canvas.create_image(
                    285, 390, image=Ivagetable, tag="vagetable")
                vagetableonb = False
            canvas.create_image(490, 341, image=Iboat, tag="boat")
        else:
            if vagetableonb == False:
                canvas.create_image(
                    915, 398, image=Ivagetable, tag="vagetable")
                vagetableonb = True
            else:
                canvas.create_image(
                    1080, 440, image=Ivagetable, tag="vagetable")
                vagetableonb = False
            canvas.create_image(845, 341, image=Iboat, tag="boat")
    click = "NULL"


def boatgo():
    global wpos, wolfonb, gpos, goatonb, vpos, vagetableonb, lbon, click, onboat
    if wolfonb == True:
        if wpos == "left":
            wgoright()
        elif wpos == "right":
            wgoleft()
        wolfonb = False
    elif goatonb == True:
        if gpos == "left":
            ggoright()
        elif gpos == "right":
            ggoleft()
        goatonb = False
    elif vagetableonb == True:
        if vpos == "left":
            vgoright()
        elif vpos == "right":
            vgoleft()
        vagetableonb = False
    else:
        if lbon == True:
            bgoright()
        elif lbon == False:
            bgoleft()
    click = "NULL"
    onboat = "off"
    checkgame()


def checkgame():
    global wpos, gpos, vpos
    if wpos == "right" and gpos == "right" and vpos == "right":
        tkinter.messagebox.showinfo(title="You Win", message="恭喜過關")
    elif (wpos == "right" and gpos == "right" and vpos == "left" and lbon == True) or (wpos == "left" and gpos == "left" and vpos == "right" and lbon == False):
        tkinter.messagebox.showerror(title="You Lose", message="羊被狼吃了")
    elif (wpos == "left" and gpos == "right" and vpos == "right" and lbon == True) or (wpos == "right" and gpos == "left" and vpos == "left" and lbon == False):
        tkinter.messagebox.showerror(title="You Lose", message="菜被羊吃了")


def reset():
    global wpos, gpos, vpos, lbon, click, wolfonb, goatonb, vagetableonb, onboat
    canvas.delete("wolf")
    canvas.delete("goat")
    canvas.delete("vagetable")
    canvas.delete("boat")
    canvas.create_image(65, 341, image=Iwolf, tag="wolf")
    canvas.create_image(200, 341, image=Igoat, tag="goat")
    canvas.create_image(285, 390, image=Ivagetable, tag="vagetable")
    canvas.create_image(490, 341, image=Iboat, tag="boat")
    wpos = "left"
    gpos = "left"
    vpos = "left"
    lbon = True
    click = "NULL"
    wolfonb = False
    goatonb = False
    vagetableonb = False
    onboat = "off"


root = tkinter.Tk()
canvas = tkinter.Canvas(root, width=1212, height=683, bg="white")
background = tkinter.PhotoImage(file="河.png")
canvas.create_image(0, 0, anchor='nw', image=background)
canvas.bind("<Button-1>", callback)
canvas.pack()
Iwolf = tkinter.PhotoImage(file="wolf.png")
canvas.create_image(65, 341, image=Iwolf, tag="wolf")
Igoat = tkinter.PhotoImage(file="goat.png")
canvas.create_image(200, 341, image=Igoat, tag="goat")
Ivagetable = tkinter.PhotoImage(file="cabbage.png")
canvas.create_image(285, 390, image=Ivagetable, tag="vagetable")
Iboat = tkinter.PhotoImage(file="boat.png")
canvas.create_image(490, 341, image=Iboat, tag="boat")
gobtn = tkinter.Button(canvas, text="GO", command=boatgo,
                       width=11, height=4).place(x=636, y=101)
resetbtn = tkinter.Button(canvas, text="Reset",
                          command=reset, width=11, height=4).place(x=536, y=101)
root.mainloop()
