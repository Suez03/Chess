import pygame as pg

pg.init()
#screen dimension
pg.display.set_caption("Chess by PyGame")
screen= pg.display.set_mode([800, 500])

font = pg.font.Font('freesansbold.ttf', 25)
big_font= pg.font.Font('freesansbold.ttf', 50)
timer= pg.time.Clock()
fps= 30

#game items and resource
white_pp= ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
           'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_loc= [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
          (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
black_pp= ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
           'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_loc= [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
          (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
capture_white= []
capture_black= []

#tt
turn_step= 0
selection= 1000
valid_move= []
# load in game piece images (queen, king, rook, bishop, knight, pawn) x 2
black_queen = pg.image.load('assets/bq.png')
black_queen = pg.transform.scale(black_queen, (80, 80))
black_queen_small = pg.transform.scale(black_queen, (45, 45))
black_king = pg.image.load('assets/bk.png')
black_king = pg.transform.scale(black_king, (80, 80))
black_king_small = pg.transform.scale(black_king, (45, 45))
black_rook = pg.image.load('assets/br.png')
black_rook = pg.transform.scale(black_rook, (80, 80))
black_rook_small = pg.transform.scale(black_rook, (45, 45))
black_bishop = pg.image.load('assets/bb.png')
black_bishop = pg.transform.scale(black_bishop, (80, 80))
black_bishop_small = pg.transform.scale(black_bishop, (45, 45))
black_knight = pg.image.load('assets/bn.png')
black_knight = pg.transform.scale(black_knight, (80, 80))
black_knight_small = pg.transform.scale(black_knight, (45, 45))
black_pawn = pg.image.load('assets/bp.png')
black_pawn = pg.transform.scale(black_pawn, (65, 65))
black_pawn_small = pg.transform.scale(black_pawn, (45, 45))
white_queen = pg.image.load('assets/wq.png')
white_queen = pg.transform.scale(white_queen, (80, 80))
white_queen_small = pg.transform.scale(white_queen, (45, 45))
white_king = pg.image.load('assets/wk.png')
white_king = pg.transform.scale(white_king, (80, 80))
white_king_small = pg.transform.scale(white_king, (45, 45))
white_rook = pg.image.load('assets/wr.png')
white_rook = pg.transform.scale(white_rook, (80, 80))
white_rook_small = pg.transform.scale(white_rook, (45, 45))
white_bishop = pg.image.load('assets/wb.png')
white_bishop = pg.transform.scale(white_bishop, (80, 80))
white_bishop_small = pg.transform.scale(white_bishop, (45, 45))
white_knight = pg.image.load('assets/wn.png')
white_knight = pg.transform.scale(white_knight, (80, 80))
white_knight_small = pg.transform.scale(white_knight, (45, 45))
white_pawn = pg.image.load('assets/wp.png')
white_pawn = pg.transform.scale(white_pawn, (65, 65))
white_pawn_small = pg.transform.scale(white_pawn, (45, 45))
white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop]
small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_knight_small,
                      white_rook_small, white_bishop_small]
black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]
small_black_images = [black_pawn_small, black_queen_small, black_king_small, black_knight_small,
                      black_rook_small, black_bishop_small]
piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']

def board():
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pg.draw.rect(screen, 'light gray', [600 - (column * 200), row * 100, 100, 100])
        else:
            pg.draw.rect(screen, 'light gray', [700 - (column * 200), row * 100, 100, 100])
        pg.draw.rect(screen, 'gray', [0, 800, WIDTH, 100])
        pg.draw.rect(screen, 'gold', [0, 800, WIDTH, 100], 5)
        pg.draw.rect(screen, 'gold', [800, 0, 200, HEIGHT], 5)
        status_text = ['White: Select a Piece to Move!', 'White: Select a Destination!',
                       'Black: Select a Piece to Move!', 'Black: Select a Destination!']
        screen.blit(big_font.render(status_text[turn_step], True, 'black'), (20, 820))
        for i in range(9):
            pg.draw.line(screen, 'black', (0, 100 * i), (800, 100 * i), 2)
            pg.draw.line(screen, 'black', (100 * i, 0), (100 * i, 800), 2)
        screen.blit(medium_font.render('FORFEIT', True, 'black'), (810, 830))
        
#gameloop
run=True
while run:
    timer.tick(fps)
    screen.fill('gray')
    
    #get inputs aka event
    for event in pg.event.get():
        if event.type==pg.QUIT:
            run=False

    pg.display.flip()
pg.quit()

