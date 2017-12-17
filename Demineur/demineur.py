#!/usr/bin/env python2
# coding: utf-8

from Tkinter import *
from random import randint
from PIL import Image, ImageTk
from os.path import join
from random import randint
from tkMessageBox import *
import datetime


class Assets:
    def __init__(self, folder="assets"):
        self.folder = folder
        self.digits = []
        self.values = []
        self.mine = ""
        self.flag = ""
        self.grid = ""
        self.smiley = ""
        self.smiley_down = ""

    def load_assets(self):
        for id in range(0, 10):
            asset_path = join(self.folder, "_%s.png" % id)
            self.digits.append(ImageTk.PhotoImage(Image.open(asset_path)))
            if id != 9:
                asset_path = join(self.folder, "%s.png" % id)
                self.values.append(ImageTk.PhotoImage(Image.open(asset_path)))
        self.mine = ImageTk.PhotoImage(
            Image.open(join(self.folder, "mine.png")))
        self.grid = ImageTk.PhotoImage(
            Image.open(join(self.folder, "grid.png")))
        self.flag = ImageTk.PhotoImage(
            Image.open(join(self.folder, "flag.png")))
        self.smiley = ImageTk.PhotoImage(
            Image.open(join(self.folder, "smiley.png")))
        self.smiley_down = ImageTk.PhotoImage(
            Image.open(join(self.folder, "smiley_down.png")))


class Demineur:
    def __init__(self, assets, width=1920, height=1080, sprite_size=50, grid_size=16, mines=50):
        self.sprite_size = sprite_size
        self.number_mines = mines
        self.number_mines_bckup = mines
        self.grid_size = grid_size
        self.mines = mines
        self.root = Tk()
        self.assets = assets
        self.assets.load_assets()
        self.game_frame = None
        self.setup_window()
        self.start_time = None
        self.start_game()
        self.update_clock()

    def update_clock(self):
        if not self.start_time:
            return
        now = datetime.datetime.now() - self.start_time
        minutes, secondes = now.seconds // 60, now.seconds % 60
        digit_one, digit_two = minutes // 10, minutes % 10
        digit_three, digit_four = secondes // 10, secondes % 10

        self.canvas2.create_image(self.grid_size*self.sprite_size-25, 0, anchor=NW, image=self.assets.digits[digit_four])
        self.canvas2.create_image(self.grid_size*self.sprite_size-50, 0, anchor=NW, image=self.assets.digits[digit_three])
        self.canvas2.create_image(self.grid_size*self.sprite_size-85, 0, anchor=NW, image=self.assets.digits[digit_two])
        self.canvas2.create_image(self.grid_size*self.sprite_size-110, 0, anchor=NW, image=self.assets.digits[digit_one])

        self.root.after(1000, self.update_clock)

    def start_game(self):
        if hasattr(self, 'canvas'):
            self.canvas.destroy()
            self.start_time = None

        self.number_mines = self.number_mines_bckup
        self.show_mines_left()
        self.grid = Grid(self.grid_size, self.mines)
        self.player_grid = [[-1 for i in range(self.grid_size)] for j in range(self.grid_size)]
        self.canvas = Canvas(self.game_frame, width=self.sprite_size*self.grid_size, height=self.sprite_size*self.grid_size)
        self.canvas.grid()
        self.draw_grid()
        self.canvas.bind("<Button-1>", self.left_click)
        self.canvas.bind("<Button-3>", self.right_click)
        self.start_time = datetime.datetime.now()

    def show_mines(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if self.grid.mat[i][j] == 9:
                    self.canvas.create_image(j * self.sprite_size, i * self.sprite_size, anchor=NW, image=self.assets.mine)


    def setup_window(self):
        self.root.title("MineSweeper")
        menubar = Menu(self.root)
        menu1 = Menu(menubar, tearoff=0)
        menu1.add_command(label="Quitter", command=self.root.quit)
        menubar.add_cascade(label="Fichier", menu=menu1)
        self.root.config(menu=menubar)

        buttons_frame = Frame(self.root, borderwidth=2, relief=GROOVE)
        buttons_frame.pack(side=TOP, padx=10, pady=10)

        self.game_frame = Frame(self.root, borderwidth=2, relief=GROOVE)
        self.game_frame.pack(anchor=CENTER, padx=10, pady=10)

        self.canvas2 = Canvas(buttons_frame, width=self.sprite_size*self.grid_size, height=50)
        self.canvas2.grid()
        self.canvas2.create_image(self.sprite_size*self.grid_size/2, 25, image=self.assets.smiley)
        self.canvas2.bind("<Button-1>", self.begin_game)
        self.canvas2.bind("<ButtonRelease-1>", self.begin_game1)

    def begin_game(self, event):
        self.canvas2.create_image(self.sprite_size*self.grid_size/2, 25, image=self.assets.smiley_down)

    def begin_game1(self, event):
        self.canvas2.create_image(self.sprite_size*self.grid_size/2, 25, image=self.assets.smiley)
        if askyesno("New game ?", "Commencer une nouvelle partie ?"):
            self.start_game()

    def left_click(self, event):
        j, i = int(event.x / 50), int(event.y / 50)
        if self.player_grid[i][j] == -2:
            return
        if not self.grid.mat[i][j]:
            self.spread(i, j)
        elif self.grid.mat[i][j] == self.grid.mine:
            self.player_loses()
        else:
            self.update_grid(i, j)

    def player_loses(self):
        self.show_mines()
        if askyesno("Game Over!", "Voulez-vous commencer une nouvelle partie ?"):
            self.start_game()
        else:
            pass

    def spread(self, x, y):
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if i != x or j != y:
                    if 0 <= i < self.grid_size:
                        if 0 <= j < self.grid_size:
                            if self.grid.mat[i][j] == 0 and self.player_grid[i][j] != 0:
                                self.canvas.create_image(
                                    j * self.sprite_size, i * self.sprite_size, anchor=NW, image=self.assets.values[0])
                                self.player_grid[i][j] = 0
                                self.spread(i, j)
                            elif self.grid.mat[i][j] != 0:
                                self.update_grid(i, j)

    def update_grid(self, i, j):
        for value in range(self.grid.mine):
            if value == self.grid.mine:
                self.canvas.create_image(
                    j * self.sprite_size, i * self.sprite_size, anchor=NW, image=self.assets.values[value])
                self.player_grid[i][j] = value
            elif value == self.grid.mat[i][j]:
                self.canvas.create_image(
                    j * self.sprite_size, i * self.sprite_size, anchor=NW, image=self.assets.values[value])
                self.player_grid[i][j] = value

    def right_click(self, event):
        j, i = int(event.x / 50), int(event.y / 50)
        if self.player_grid[i][j] == -1:
            self.canvas.create_image(
                j * self.sprite_size, i * self.sprite_size, anchor=NW, image=self.assets.flag)
            self.player_grid[i][j] = -2
            self.number_mines -= 1
        elif self.player_grid[i][j] == -2:
            self.canvas.create_image(
                j * self.sprite_size, i * self.sprite_size, anchor=NW, image=self.assets.grid)
            self.player_grid[i][j] = -1
            self.number_mines += 1

        self.show_mines_left()

    def show_mines_left(self):
        first_digit = self.number_mines / 10
        second_digit = self.number_mines % 10

        self.canvas2.create_image(0, 0, anchor=NW, image=self.assets.digits[first_digit])
        self.canvas2.create_image(25, 0, anchor=NW, image=self.assets.digits[second_digit])

    def draw_grid(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                self.canvas.create_image(j * self.sprite_size, i * self.sprite_size,
                                         anchor=NW, image=self.assets.grid)

    def run(self):
        self.draw_grid()
        self.root.mainloop()


class Grid:
    def __init__(self, size, mines):
        self.size = size
        self.mines = mines
        self.mine = 9
        self.setup_mines()
        self.setup_mines_indicator()

    def setup_mines(self):
        self.mat = [[0 for i in range(self.size)] for j in range(self.size)]
        mines = 0
        while mines != self.mines:
            x, y = randint(0, self.size - 1), randint(0, self.size - 1)
            if not self.mat[x][y]:
                mines += 1
                self.mat[x][y] = self.mine

    def setup_mines_indicator(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.mat[i][j] == self.mine:
                    continue
                else:
                    self.mat[i][j] = self.test_neighbours(i, j)

    def test_neighbours(self, x, y):
        mines = 0
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if i != x or j != y:
                    if 0 <= i < self.size:
                        if 0 <= j < self.size:
                            if self.mat[i][j] == self.mine:
                                mines += 1

        return mines


def main():
    a = Assets()
    d = Demineur(a)
    d.run()

if __name__ == '__main__':
    main()
