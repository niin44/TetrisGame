import pygame
from pygame.locals import *


class App:
    gameSize = [10, 20]
    blockSize = [32, 32]
    windowSize = [15, 23]
    windowWidth = windowSize[0]*blockSize[0]
    windowHeight = windowSize[1]*blockSize[1]
    currentPiece = {(-1, 0), (0, 0), (1, 0), (0, 1)}
    currentPiecePos = (4, 0)
    filledBlocks = []

    def draw_filled(self):
        blockw, blockh = self.blockSize

        for blocks in self.filledBlocks:
            x = (blocks[0])*blockw
            y = (blocks[1]-1)*blockh
            pygame.draw.rect(self._game_surf, Color(150, 0, 0), Rect(x, y, blockw, blockh))

    def fill_blocks(self):
        filled = self.filledBlocks
        piece = self.currentPiece
        piece_pos = self.currentPiecePos
        for blocks in piece:
            x = blocks[0] + piece_pos[0]
            y = blocks[1] + piece_pos[1]
            filled.append((x, y))
        self.filledBlocks = filled

    def update_current_piece(self):
        self.currentPiecePos = (self.currentPiecePos[0],self.currentPiecePos[1]+1)
        if self.currentPiecePos[1] > self.gameSize[1]-1:
            self.fill_blocks()
            self.create_piece()

    def draw_current_piece(self):
        position = self.currentPiecePos
        piece = self.currentPiece
        block = self.blockSize
        for blocks in piece:
            x, y = position
            x2, y2 = blocks
            x += x2
            y += y2
            width, height = block
            pygame.draw.rect(self._game_surf, Color(255, 0, 0), Rect(x*width, y*height, width, height))

    def create_piece(self):
        self.currentPiecePos = (4, 0)

    def choose_piece(self):
        pass

    def __init__(self):
        self._running = True
        self._display_surf = None
        self._game_surf = None

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth, self.windowHeight))
        self._game_surf = self._display_surf.subsurface(0, 0, self.gameSize[0]*self.blockSize[0], self.gameSize[1] * self.blockSize[1])
        pygame.time.set_timer(USEREVENT, 400)

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
        if event.type == USEREVENT:
            self.update_current_piece()
            pygame.time.set_timer(USEREVENT, 400)
        if event.type == KEYDOWN:
            if pygame.key.get_pressed()[K_LEFT]:
                self.currentPiecePos = (self.currentPiecePos[0] - 1, self.currentPiecePos[1])
            if pygame.key.get_pressed()[K_RIGHT]:
                self.currentPiecePos = (self.currentPiecePos[0] + 1, self.currentPiecePos[1])
    def on_loop(self):
        pass

    def on_render(self):
        self._game_surf.fill(Color(30, 30, 30))
        self.draw_current_piece()
        self.draw_filled()
        pygame.display.flip()

    @staticmethod
    def on_cleanup():
        pygame.quit()

    def on_execute(self):

        if self.on_init() is False:
            self._running = False

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()

        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
