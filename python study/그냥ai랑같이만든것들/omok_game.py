import pygame
import sys

# --- 상수 정의 ---
# 화면 크기
WIDTH, HEIGHT = 600, 600
# 격자 크기 및 줄 수
BOARD_SIZE = 19
GRID_SIZE = WIDTH // (BOARD_SIZE + 1)

# 색상
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWN = (139, 69, 19)

# --- 게임 초기화 ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("오목 게임")

# 게임판 (0: 빈칸, 1: 흑돌, 2: 백돌)
board = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]
turn = 1  # 1: 흑돌, 2: 백돌
game_over = False

# --- 함수 정의 ---
def draw_board():
    """게임판을 그리는 함수"""
    screen.fill(BROWN)
    for i in range(BOARD_SIZE):
        # 가로줄
        pygame.draw.line(screen, BLACK, (GRID_SIZE, (i + 1) * GRID_SIZE), (WIDTH - GRID_SIZE, (i + 1) * GRID_SIZE), 1)
        # 세로줄
        pygame.draw.line(screen, BLACK, ((i + 1) * GRID_SIZE, GRID_SIZE), ((i + 1) * GRID_SIZE, HEIGHT - GRID_SIZE), 1)

def draw_stones():
    """게임판 위의 돌을 그리는 함수"""
    for y in range(BOARD_SIZE):
        for x in range(BOARD_SIZE):
            if board[y][x] == 1:
                pygame.draw.circle(screen, BLACK, ((x + 1) * GRID_SIZE, (y + 1) * GRID_SIZE), GRID_SIZE // 2 - 2)
            elif board[y][x] == 2:
                pygame.draw.circle(screen, WHITE, ((x + 1) * GRID_SIZE, (y + 1) * GRID_SIZE), GRID_SIZE // 2 - 2)

def check_win(player):
    """승리 조건을 확인하는 함수"""
    for y in range(BOARD_SIZE):
        for x in range(BOARD_SIZE):
            if board[y][x] == player:
                # 가로 확인
                if x + 4 < BOARD_SIZE and all(board[y][x+i] == player for i in range(5)):
                    return True
                # 세로 확인
                if y + 4 < BOARD_SIZE and all(board[y+i][x] == player for i in range(5)):
                    return True
                # 대각선 (오른쪽 아래) 확인
                if x + 4 < BOARD_SIZE and y + 4 < BOARD_SIZE and all(board[y+i][x+i] == player for i in range(5)):
                    return True
                # 대각선 (왼쪽 아래) 확인
                if x - 4 >= 0 and y + 4 < BOARD_SIZE and all(board[y+i][x-i] == player for i in range(5)):
                    return True
    return False

def show_message(message):
    """화면에 메시지를 표시하는 함수"""
    font = pygame.font.Font(None, 50)
    text = font.render(message, True, BLACK)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    pygame.draw.rect(screen, WHITE, (text_rect.left - 10, text_rect.top - 10, text_rect.width + 20, text_rect.height + 20))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.wait(3000) # 3초 대기

# --- 메인 게임 루프 ---
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if not game_over and event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = event.pos
            # 클릭된 격자 위치 계산
            x = round((mouseX - GRID_SIZE) / GRID_SIZE)
            y = round((mouseY - GRID_SIZE) / GRID_SIZE)

            # 유효한 위치이고 비어있는 칸인지 확인
            if 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE and board[y][x] == 0:
                board[y][x] = turn # 돌 놓기
                if check_win(turn):
                    winner = "흑돌" if turn == 1 else "백돌"
                    game_over = True
                    print(f"{winner} 승리!")
                
                # 턴 변경
                turn = 2 if turn == 1 else 1

    # --- 화면 그리기 ---
    draw_board()
    draw_stones()
    
    # 게임이 종료되면 승리 메시지 표시
    if game_over:
        winner = "백돌" if turn == 2 else "흑돌" # 이전 턴의 승자
        show_message(f"{winner} 승리!")
        # 게임 재시작을 위한 초기화
        board = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]
        turn = 1
        game_over = False


    pygame.display.flip()