import random

import numpy as np
import time

BLACK = 1
WHITE = -1


def MakeFiled():
    Board = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, -1, 0, 0, 0],
        [0, 0, 0, -1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ]
    # Board = [
    #     [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    #     [9, -1, -1, -1, -1, -1, -1, -1, -1, 9],
    #     [9, 1, 1, -1, 1, 1, 1, 1, 1, 9],
    #     [9, 1, 1, 1, 1, 1, 1, -1, -1, 9],
    #     [9, -1, -1, -1, -1, -1, -1, -1, -1, 9],
    #     [9, 0, 0, 0, -1, -1, 0, 0, 0, 9],
    #     [9, 0, 0, 0, 0, -1, 0, 0, 0, 9],
    #     [9, 0, 0, 0, 0, 0, 0, 0, 0, 9],
    #     [9, 0, 0, 0, 0, 0, 0, 0, 0, 9],
    #     [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    # ]

    field = np.pad(
        Board, [1, 1], 'constant', constant_values=9
    )
    return field


class ReversiBoard:
    def __init__(self):
        self.ok_list = np.zeros((9, 9))
        self.filed = MakeFiled()
        self.TurnCount = 0
        self.turn = 1
        self.black = np.sum(self.filed == BLACK)
        self.white = np.sum(self.filed == WHITE)
        self.remain = np.sum(self.filed == 0)
        self.total = 0
        self.can_put = []

    def ChangeStone(self, x, y):
        self.filed[x, y] = self.turn

    # 石を置く
    def PutStone(self, x, y):
        b = self.check(x, y)
        self.TurnCount += 1
        self.black = np.sum(self.filed == BLACK)
        self.white = np.sum(self.filed == WHITE)
        self.remain = np.sum(self.filed == 0)
        return b

    # 置けるかどうか判断する

    def check(self, x, y):
        if (0 < y < 9) & (0 < x < 9) & (self.filed[x, y] == 0):
            # 上下左右斜めに駒があるか
            # 右
            if self.filed[x, y + 1] == -self.turn:
                num = 1
                while self.filed[x, y + num] == -self.turn:
                    num += 1
                if self.filed[x, y + num] == self.turn:
                    for i in range(num):
                        self.ChangeStone(x, y + i)
            # 左
            if self.filed[x, y - 1] == -self.turn:
                num = 1
                while self.filed[x, y - num] == -self.turn:
                    num += 1
                if self.filed[x, y - num] == self.turn:
                    for i in range(num):
                        self.ChangeStone(x, y - i)
            # 上
            if self.filed[x - 1, y] == -self.turn:
                num = 1
                while self.filed[x - num, y] == -self.turn:
                    num += 1
                if self.filed[x - num, y] == self.turn:
                    for i in range(num):
                        self.ChangeStone(x - i, y)
            # 下
            if self.filed[x + 1, y] == -self.turn:
                num = 1
                while self.filed[x + num, y] == -self.turn:
                    num += 1
                if self.filed[x + num, y] == self.turn:
                    for i in range(num):
                        self.ChangeStone(x + i, y)
            # 右上
            if self.filed[x - 1, y + 1] == -self.turn:
                num = 1
                while self.filed[x - num, y + num] == -self.turn:
                    num += 1
                if self.filed[x - num, y + num] == self.turn:
                    for i in range(num):
                        self.ChangeStone(x - i, y + i)
            # 右下
            if self.filed[x + 1, y + 1] == -self.turn:
                num = 1
                while self.filed[x + num, y + num] == -self.turn:
                    num += 1
                if self.filed[x + num, y + num] == self.turn:
                    for i in range(num):
                        self.ChangeStone(x + i, y + i)
            # 左上
            if self.filed[x - 1, y - 1] == -self.turn:
                num = 1
                while self.filed[x - num, y - num] == -self.turn:
                    num += 1
                if self.filed[x - num, y - num] == self.turn:
                    for i in range(num):
                        self.ChangeStone(x - i, y - i)
            # 左下
            if self.filed[x + 1, y - 1] == -self.turn:
                num = 1
                while self.filed[x + num, y - num] == -self.turn:
                    num += 1
                if self.filed[x + num, y - num] == self.turn:
                    for i in range(num):
                        self.ChangeStone(x + i, y - i)
            if self.filed[x, y] == 0:
                print("そこには置けません")
                return 0

        else:
            return 0

    def ok_point(self, x, y):
        if (0 < y < 9) & (0 < x < 9) & (self.filed[x, y] == 0):
            # 上下左右斜めに駒があるか
            # 右
            self.total = 0
            if self.filed[x, y + 1] == -self.turn:
                num = 1
                while self.filed[x, y + num] == -self.turn:
                    num += 1
                if self.filed[x, y + num] == self.turn:
                    self.total += num
            # 左
            if self.filed[x, y - 1] == -self.turn:
                num = 1
                while self.filed[x, y - num] == -self.turn:
                    num += 1
                if self.filed[x, y - num] == self.turn:
                    self.total += num
            # 上
            if self.filed[x - 1, y] == -self.turn:
                num = 1
                while self.filed[x - num, y] == -self.turn:
                    num += 1
                if self.filed[x - num, y] == self.turn:
                    self.total += num
            # 下
            if self.filed[x + 1, y] == -self.turn:
                num = 1
                while self.filed[x + num, y] == -self.turn:
                    num += 1
                if self.filed[x + num, y] == self.turn:
                    self.total += num
            # 右上
            if self.filed[x - 1, y + 1] == -self.turn:
                num = 1
                while self.filed[x - num, y + num] == -self.turn:
                    num += 1
                if self.filed[x - num, y + num] == self.turn:
                    self.total += num
            # 右下
            if self.filed[x + 1, y + 1] == -self.turn:
                num = 1
                while self.filed[x + num, y + num] == -self.turn:
                    num += 1
                if self.filed[x + num, y + num] == self.turn:
                    self.total += num
            # 左上
            if self.filed[x - 1, y - 1] == -self.turn:
                num = 1
                while self.filed[x - num, y - num] == -self.turn:
                    num += 1
                if self.filed[x - num, y - num] == self.turn:
                    self.total += num
            # 左下
            if self.filed[x + 1, y - 1] == -self.turn:
                num = 1
                while self.filed[x + num, y - num] == -self.turn:
                    num += 1
                if self.filed[x + num, y - num] == self.turn:
                    self.total += num
            if self.total > 0:
                return 1

            return 0
        else:
            return 0

    # 置けるマスを探す
    def ok(self):
        for x in range(9):
            for y in range(9):
                self.ok_list[x][y] = self.ok_point(x, y)

    def can(self):
        self.ok()
        self.can_put.clear()
        for x in range(9):
            for y in range(9):
                if self.ok_point(x, y) == 1:
                    a = [x, y]
                    self.can_put.append(a)


# board = ReversiBoard()
# board.PutStone(3, 6)
# print(board.filed)
def choice(board):
    board.can()
    print(board.can_put)
    a = input('半角数字、間空白')
    a = a.split()
    x, y = a[0], a[1]
    b = board.PutStone(int(x), int(y))
    return b


def game():
    print('Game Start !!')
    board = ReversiBoard()
    while True:
        print(board.filed)
        board.can()
        print('残りは', board.remain, 'コマです')
        end = game_set(board)
        if board.remain == 0 or end == 0:
            print('置ける場所がありません')
            if board.black > board.white:
                print('あなたのかち')
                return 1
            else:
                print('あなたのまけ')
                return 0
        if board.turn == 1:

            print(
                'Your Turn\n下の数字の中から入れたい場所の座標を半角数字で入力してください\nなお間は半角空白を入れてください')
            while True:
                b = choice(board)
                if b != 0:
                    break
            print("そこには置けません")
            time.sleep(.1)
            board.turn = -board.turn
        else:
            while True:
                end = game_set(board)
                if end == 1: break
                print(
                    'Ai Turn')
                print(board.can_put)
                ai_choice = random.choice(board.can_put)
                board.PutStone(int(ai_choice[0]), (ai_choice[1]))
                time.sleep(.1)
                board.turn *= -1
                break


def game_set(board):
    if board.can_put is None:
        board.turn *= -1
        if board.can_put is None:
            return 0
        else:
            board.turn *= -1
            return 1
    else:
        return 2


game()
