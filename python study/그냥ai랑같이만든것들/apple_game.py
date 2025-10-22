import pygame
import random
import sys
import os

# 초기화
pygame.init()

# 화면 크기
WIDTH, HEIGHT = 600, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("사과 게임 🍎")

# 이미지 로드 (스크립트 폴더 기준 경로 사용)
script_dir = os.path.dirname(__file__)
apple_path = os.path.join(script_dir, "apple.png")
basket_path = os.path.join(script_dir, "basket.jpg")

apple_img = pygame.image.load(apple_path).convert_alpha()
basket_img = pygame.image.load(basket_path).convert_alpha()

# 스케일 (너비, 높이)
apple_img = pygame.transform.scale(apple_img, (30, 30))
basket_img = pygame.transform.scale(basket_img, (170, 50))

# 색상
WHITE = (255, 255, 255)
RED = (200, 0, 0)
BROWN = (139, 69, 19)

# 바구니
basket_width, basket_height = 100, 20
basket_x = WIDTH // 2 - basket_width // 2
basket_y = HEIGHT - 40
basket_speed = 25

# 사과 (이미지 크기에 맞춘 좌표/속도)
apple_w, apple_h = apple_img.get_size()
apple_speed = 7

# 사과 시스템
TOTAL_APPLES = 100  # 총 사과 개수
apples_fallen = 0  # 떨어진 사과 개수
apples_caught = 0  # 받은 사과 개수

# 화면에 동시에 보이는 사과들
apples = []
for _ in range(10):  # 동시에 10개씩 떨어짐
    if apples_fallen < TOTAL_APPLES:
        apple_x = random.randint(0, WIDTH - apple_w)
        apple_y = random.randint(-HEIGHT, 0)
        apples.append([apple_x, apple_y])
        apples_fallen += 1

# 폰트
font = pygame.font.SysFont(None, 40)
big_font = pygame.font.SysFont(None, 80)

# 게임 루프
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(WHITE)

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 키 입력
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket_x > 0:
        basket_x -= basket_speed
    if keys[pygame.K_RIGHT] and basket_x < WIDTH - basket_width:
        basket_x += basket_speed

    # 게임이 끝났는지 확인
    game_over = len(apples) == 0 and apples_fallen >= TOTAL_APPLES
    
    if not game_over:
        # 모든 사과 이동 및 충돌 체크
        basket_rect = basket_img.get_rect(topleft=(basket_x, basket_y))
        
        apples_to_remove = []
        for i, apple in enumerate(apples):
            # 사과 이동
            apple[1] += apple_speed
            
            # 사과가 바구니에 닿았는지 확인
            apple_rect = apple_img.get_rect(topleft=(apple[0], apple[1]))
            if apple_rect.colliderect(basket_rect):
                apples_caught += 1
                apples_to_remove.append(i)
                # 새 사과 추가 (총 개수 제한 내에서)
                if apples_fallen < TOTAL_APPLES:
                    new_x = random.randint(0, WIDTH - apple_w)
                    new_y = random.randint(-HEIGHT // 2, -apple_h)
                    apples.append([new_x, new_y])
                    apples_fallen += 1
            
            # 사과가 바닥에 닿으면 제거하고 새 사과 추가
            elif apple[1] > HEIGHT:
                apples_to_remove.append(i)
                # 새 사과 추가 (총 개수 제한 내에서)
                if apples_fallen < TOTAL_APPLES:
                    new_x = random.randint(0, WIDTH - apple_w)
                    new_y = random.randint(-HEIGHT // 2, -apple_h)
                    apples.append([new_x, new_y])
                    apples_fallen += 1
        
        # 제거할 사과들을 뒤에서부터 제거 (인덱스 오류 방지)
        for i in sorted(apples_to_remove, reverse=True):
            apples.pop(i)

        # 모든 사과 그리기
        for apple in apples:
            screen.blit(apple_img, (apple[0], apple[1]))
        
        # 바구니 그리기
        screen.blit(basket_img, (basket_x, basket_y))

        # 점수 및 진행 상황 표시
        score_text = font.render(f"받은 사과: {apples_caught} / {TOTAL_APPLES}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))
    else:
        # 게임 종료 화면
        game_over_text = big_font.render("게임 종료!", True, (255, 0, 0))
        result_text = font.render(f"받은 사과: {apples_caught} / {TOTAL_APPLES}", True, (0, 0, 0))
        percentage = int((apples_caught / TOTAL_APPLES) * 100)
        percent_text = font.render(f"성공률: {percentage}%", True, (0, 0, 0))
        restart_text = font.render("ESC를 눌러 종료", True, (100, 100, 100))
        
        screen.blit(game_over_text, (WIDTH // 2 - 150, HEIGHT // 2 - 100))
        screen.blit(result_text, (WIDTH // 2 - 150, HEIGHT // 2))
        screen.blit(percent_text, (WIDTH // 2 - 100, HEIGHT // 2 + 50))
        screen.blit(restart_text, (WIDTH // 2 - 120, HEIGHT // 2 + 120))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
