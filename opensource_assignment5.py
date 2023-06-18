import pygame
import random


pygame.init() #초기화

# 화면 크기 설정
screen_width = 480 # 가로크기
screen_height = 640 # 세로크기
screen = pygame.display.set_mode((screen_width,screen_height))



# 화면 타이틀 설정
pygame.display.set_caption("avoid F Game") 

clock = pygame.time.Clock()

background = pygame.image.load("C:\\Users\\윤제\\OneDrive\\바탕 화면\\Pythonworkspace\\pygame_basic\\school.png")

character = pygame.image.load("C:\\Users\\윤제\\OneDrive\\바탕 화면\\Pythonworkspace\\pygame_basic\\student.png")
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0] # 캐릭터의 가로크기
character_height = character_size[1] # 캐릭터의 세로크기
character_x_pos = screen_width / 2 - (character_width / 2) # 화면 가로의 절반 크기에 해당하는 곳에 위치(가로)
character_y_pos = screen_height - character_height # 화면 세로 크기 가장 아래에 해당하는 곳에 위치(세로)

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.5

# F학점 만들기
ddong = pygame.image.load("C:\\Users\\윤제\\OneDrive\\바탕 화면\\Pythonworkspace\\pygame_basic\\fgrade.png")
ddong_size = ddong.get_rect().size
ddong_width = ddong_size[0] # 가로크기
ddong_height = ddong_size[1] # 세로크기
ddong_x_pos = random.randint(0, screen_width - ddong_width)
ddong_y_pos = 0
ddong_speed = 0.5


# 폰트 정의
game_font = pygame.font.Font(None,40) # 폰트 생성 

# 총 시간
total_time = 30

# 시작 시간
start_ticks = pygame.time.get_ticks() 

# 이벤트 루프
running = True # 게임이진행중인지?
while running:
    dt = clock.tick(60) 
    for event in pygame.event.get(): # 무슨 이벤트가 발생하는지?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False

        if event.type == pygame.KEYDOWN: # 무슨 키가 눌러졌는지
            if event.key == pygame.K_LEFT: #캐릭터를 왼쪽으로
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로
                to_x += character_speed
            

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # 가로 경계값 처리
    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 세로 경계값 처리
    if character_y_pos < 0 :
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    ddong_y_pos += ddong_speed*dt

    if ddong_y_pos > screen_height:
        ddong_y_pos = 0
        ddong_x_pos = random.randint(0, screen_width - ddong_width)

    # 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    ddong_rect = ddong.get_rect()
    ddong_rect.left = ddong_x_pos
    ddong_rect.top = ddong_y_pos
    
    # 충돌체크
    if character_rect.colliderect(ddong_rect):
        print("충돌했어요")
        running = False

    screen.blit(background, (0,0)) # 배경 그리기
    screen.blit(character,(character_x_pos, character_y_pos)) # 캐릭터 그리기
    screen.blit(ddong, (ddong_x_pos, ddong_y_pos))

    # 타이머 집어넣기
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255,255,255))
    # 출력할 글자, True, 글자 생상
    screen.blit(timer, (10,10))

    # 만약 시간이 0 이하면 게임 종료
    if total_time - elapsed_time <= 0:
        print("타임 아웃")
        running = False

    pygame.display.update() # 게임화면을 다시 그리기

pygame.time.delay(1000) # 1초 대기

# game 종료
pygame.quit()