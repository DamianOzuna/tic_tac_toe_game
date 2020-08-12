import pygame, sys, random
from pygame.locals import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Game():
    def __init__(self):
        self.x_width = 1200
        self.y_height = 900
        self.basicAI = False
        self.reset = True
        self.running = True
        self.winner = "none"
        self.player_turn = 'X'
        self.grid = [[None]*3,
                     [None]*3,
                     [None]*3]
        pygame.init()
        self.DISPLAY = pygame.display.set_mode((self.x_width, self.y_height))
        self.DISPLAY.fill(WHITE)
        self.x_img = pygame.image.load('redX.png')
        self.o_img = pygame.image.load('blackO.png')
        self.rect_img = pygame.image.load('rect.png')
        pygame.display.set_caption('TIC-TAC-TOE')
        pygame.draw.line(self.DISPLAY, BLACK, (0, 300), (900, 300), 3)
        pygame.draw.line(self.DISPLAY, BLACK, (0, 600), (900, 600), 3)
        pygame.draw.line(self.DISPLAY, BLACK, (300, 0), (300, 900), 3)
        pygame.draw.line(self.DISPLAY, BLACK, (600, 0), (600, 900), 3)
        pygame.draw.line(self.DISPLAY, BLACK, (900, 0), (900, 900), 3)

        self.score_font = pygame.font.SysFont("ariel", 56)
        self.x_wins = 0
        self.o_wins = 0
        self.draws = 0
        self.x_counter_str = self.score_font.render("X Wins:", 1, BLACK)
        self.o_counter_str = self.score_font.render("O Wins:", 1, BLACK)
        self.draws_str = self.score_font.render("Draws:", 1, BLACK)
        self.rect_str = self.score_font.render("Play vs AI", 1, BLACK)
        self.rect_str_player = self.score_font.render("Play vs", 1, BLACK)
        self.rect_str_player2 = self.score_font.render("player", 1, BLACK)
        self.x_wins_display = self.score_font.render(str(self.x_wins), 1, BLACK)
        self.o_wins_display = self.score_font.render(str(self.o_wins), 1, BLACK)
        self.draws_display = self.score_font.render(str(self.draws), 1, BLACK)

        pygame.display.update();

    def drawXO(self, x, y):
        if x < 300 and y < 300 and self.grid[0][0] is None:
            if self.player_turn == 'X':
                self.DISPLAY.blit(self.x_img, (2, 2))
                self.grid[0][0] = self.player_turn
                self.player_turn = 'O'
            elif self.player_turn == 'O':
                self.DISPLAY.blit(self.o_img, (2, 2))
                self.grid[0][0] = self.player_turn
                self.player_turn = 'X'
        elif 300 < x < 600 and y < 300 and self.grid[0][1] is None:
            if self.player_turn == 'X':
                self.DISPLAY.blit(self.x_img, (302, 2))
                self.grid[0][1] = self.player_turn
                self.player_turn = 'O'
            elif self.player_turn == 'O':
                self.DISPLAY.blit(self.o_img, (302, 2))
                self.grid[0][1] = self.player_turn
                self.player_turn = 'X'
        elif 600 < x < 900 and y < 300 and self.grid[0][2] is None:
            if self.player_turn == 'X':
                self.DISPLAY.blit(self.x_img, (602, 2))
                self.grid[0][2] = self.player_turn
                self.player_turn = 'O'
            elif self.player_turn == 'O':
                self.DISPLAY.blit(self.o_img, (602, 2))
                self.grid[0][2] = self.player_turn
                self.player_turn = 'X'
        elif 0 < x < 300 and 300 < y < 600 and self.grid[1][0] is None:
            if self.player_turn == 'X':
                self.DISPLAY.blit(self.x_img, (2, 302))
                self.grid[1][0] = self.player_turn
                self.player_turn = 'O'
            elif self.player_turn == 'O':
                self.DISPLAY.blit(self.o_img, (2, 302))
                self.grid[1][0] = self.player_turn
                self.player_turn = 'X'
        elif 300 < x < 600 and 300 < y < 600 and self.grid[1][1] is None :
            if self.player_turn == 'X':
                self.DISPLAY.blit(self.x_img, (302, 302))
                self.grid[1][1] = self.player_turn
                self.player_turn = 'O'
            elif self.player_turn == 'O':
                self.DISPLAY.blit(self.o_img, (302, 302))
                self.grid[1][1] = self.player_turn
                self.player_turn = 'X'
        elif 600 < x < 900 and 300 < y < 600 and self.grid[1][2] is None:
            if self.player_turn == 'X':
                self.DISPLAY.blit(self.x_img, (602, 302))
                self.grid[1][2] = self.player_turn
                self.player_turn = 'O'
            elif self.player_turn == 'O':
                self.DISPLAY.blit(self.o_img, (602, 302))
                self.grid[1][2] = self.player_turn
                self.player_turn = 'X'
        elif x < 300 and 600 < y < 900 and self.grid[2][0] is None:
            if self.player_turn == 'X':
                self.DISPLAY.blit(self.x_img, (2, 602))
                self.grid[2][0] = self.player_turn
                self.player_turn = 'O'
            elif self.player_turn == 'O':
                self.DISPLAY.blit(self.o_img, (2, 602))
                self.grid[2][0] = self.player_turn
                self.player_turn = 'X'
        elif 300 < x < 600 and 600 < y < 900 and self.grid[2][1] is None:
            if self.player_turn == 'X':
                self.DISPLAY.blit(self.x_img, (302, 602))
                self.grid[2][1] = self.player_turn
                self.player_turn = 'O'
            elif self.player_turn == 'O':
                self.DISPLAY.blit(self.o_img, (302, 602))
                self.grid[2][1] = self.player_turn
                self.player_turn = 'X'
        elif 600 < x < 900 and 600 < y < 900 and self.grid[2][2] is None:
            if self.player_turn == 'X':
                self.DISPLAY.blit(self.x_img, (602, 602))
                self.grid[2][2] = self.player_turn
                self.player_turn = 'O'
            elif self.player_turn == 'O':
                self.DISPLAY.blit(self.o_img, (602, 602))
                self.grid[2][2] = self.player_turn
                self.player_turn = 'X'
        elif x > 940 and y > 740:
            self.basicAI = not self.basicAI
            self.reset_game()
        pygame.display.update()

    def reset_game(self):
        self.grid = [[None]*3,
                    [None]*3,
                    [None]*3]
        self.winner = "none"
        self.clear_screen()

    def clear_screen(self):
        self.DISPLAY.fill(WHITE)
        pygame.draw.line(self.DISPLAY, BLACK, (0, 300), (900, 300), 3)
        pygame.draw.line(self.DISPLAY, BLACK, (0, 600), (900, 600), 3)
        pygame.draw.line(self.DISPLAY, BLACK, (300, 0), (300, 900), 3)
        pygame.draw.line(self.DISPLAY, BLACK, (600, 0), (600, 900), 3)
        pygame.draw.line(self.DISPLAY, BLACK, (900, 0), (900, 900), 3)
        self.DISPLAY.blit(self.rect_img, (920, 670))

        self.x_counter_str = self.score_font.render("X Wins:", 1, BLACK)
        self.o_counter_str = self.score_font.render("O Wins:", 1, BLACK)
        self.draws_str = self.score_font.render("Draws:", 1, BLACK)
        self.x_wins_display = self.score_font.render(str(self.x_wins), 1, BLACK)
        self.o_wins_display = self.score_font.render(str(self.o_wins), 1, BLACK)
        self.draws_display = self.score_font.render(str(self.draws), 1, BLACK)

        self.DISPLAY.blit(self.x_counter_str, (1000, 200))
        self.DISPLAY.blit(self.x_wins_display, (1000, 240))
        self.DISPLAY.blit(self.o_counter_str, (1000, 300))
        self.DISPLAY.blit(self.o_wins_display, (1000, 340))
        self.DISPLAY.blit(self.draws_str, (1000, 400))
        self.DISPLAY.blit(self.draws_display, (1000, 440))
        if self.basicAI is False:
            self.DISPLAY.blit(self.rect_str, (960, 790))
        else:
            self.DISPLAY.blit(self.rect_str_player, (980, 770))
            self.DISPLAY.blit(self.rect_str_player2, (990, 820))

    def detect_win(self):
        for i in range(0, 3):
            if self.grid[i][0] == self.grid[i][1] == self.grid[i][2] and self.grid[i][0] is not None:
                self.winner = self.grid[i][0]

        for i in range(0, 3):
            if self.grid[0][i] == self.grid[1][i] == self.grid[2][i] and self.grid[0][i] is not None:
                self.winner = self.grid[0][i]

        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] and self.grid[0][0] is not None:
            self.winner = self.grid[0][0];
        elif self.grid[0][2] == self.grid[1][1] == self.grid[2][0] and self.grid[0][2] is not None:
            self.winner = self.grid[0][2];
        if self.winner == 'X':
            self.x_wins += 1
            return self.winner
        elif self.winner == 'O':
            self.o_wins += 1
            return self.winner

        found_0 = any(None in sublist for sublist in self.grid)
        if found_0:
            return "none"
        else:
            self.winner = "draw"
            self.draws += 1
            return self.winner

    def run(self):
        self.reset_game()
        while self.running is True:
            for event in pygame.event.get():
                if self.basicAI is True and self.player_turn == "O":
                    ai_x = random.randint(0, 8)
                    ai_y = random.randint(0, 8)
                    self.drawXO(ai_x*100+1, ai_y*100+1)
                elif event.type == QUIT:
                    self.running = False
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()
                    self.drawXO(x, y)
                    winner = self.detect_win()
                    if winner != "none":
                        pygame.time.wait(500)
                        self.reset_game()

                pygame.display.update()


Game().run()
