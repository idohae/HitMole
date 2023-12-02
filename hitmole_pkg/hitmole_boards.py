import os
import time

HIT_MOLE = '''
                                                              
                                                              





      ██ ██ ████ ██████      ███  ███  ███  ███   █████       
      ██ ██  ██  █ ██ █       ██ ███  ██ ██  ██    ██         
█ █   █████  ██    ██         ██████  ██ ██  ██    ████   █ █ 
      ██ ██  ██    ██         █ █ ██  ██ ██  ██ █  ██         
      ██ ██ ████  ████       ██ █ ███  ███  █████ █████       

      



                                                              
                                                              
'''
TUTORIAL = '''
                                                   
                                                   





    ██████ ██  █ ██████  ███  █████  ████   ██   ███   
    █ ██ █ ██  █ █ ██ █ ██ ██  ██ ██  ██   █ ██   ██   
      ██   ██  █   ██   ██ ██  ████   ██   ████   ██   
      ██   ██  █   ██   ██ ██  ██ █   ██   █ ██   ██ █ 
     ████   ███   ████   ███  ███ ██ ████ ██ ███ █████ 
                                                   





                                                   
'''
START = '''
                                                                






 ███    ██   ███  ███ █████    ████ ██████   ██   █████  ██████ 
██     █ ██   ██ ███   ██     ███   █ ██ █  █ ██   ██ ██ █ ██ █ 
██ ██  ████   ██████   ████    ███    ██    ████   ████    ██   
██ ██  █ ██   █ █ ██   ██       ███   ██    █ ██   ██ █    ██   
 ███  ██ ███ ██ █ ███ █████   ████   ████  ██ ███ ███ ██  ████  
                                                                





                                                                
 
'''
OVER = '''
                                                        
                                                        





     ███    ██   ███  ███ █████    ███  ███  █ █████ █████   
    ██     █ ██   ██ ███   ██     ██ ██  ██ ██  ██    ██ ██ 
    ██ ██  ████   ██████   ████   ██ ██  ██ █   ████  ████  
    ██ ██  █ ██   █ █ ██   ██     ██ ██   ███   ██    ██ █  
     ███  ██ ███ ██ █ ███ █████    ███     █   █████ ███ ██ 





                                                        
                                                        
'''
SCORE = [
    '       ████  ███   ███  █████  █████        ',
    '      ███   ██  █ ██ ██  ██ ██  ██     █    ',
    '       ███  ██    ██ ██  ████   ████        ',
    '        ███ ██  █ ██ ██  ██ █   ██     █    ',
    '      ████   ███   ███  ███ ██ █████        '
]
ROUND = [
    '         █████   ███  ██  █ ██  ██ ████      ',
    '          ██ ██ ██ ██ ██  █  ██ █   ██ █     ',
    '          ████  ██ ██ ██  █  ████   ██ █     ',
    '          ██ █  ██ ██ ██  █  █ ██   ██ █     ',
    '         ███ ██  ███   ███  ██  █  ████      '
]
NUMS = [
    ' ██  ███  ███  ███    █  ████  ███ ████  ██   ██  ',
    '██ █  ██    ██   ██  ██  ██   ██     ██ ██ █ █ ██ ',
    '██ █  ██   ██   ███ █ █   ██  ████  ██   ██   ███ ',
    '██ █  ██  ██     ██ ████   ██ ██ █  █   ██ █   ██ ',
    ' ██  ████ ████ ███   ██  ███   ██  ██    ██  ███  '
]
# ALPHA = [
#     '       █             █           █         █      █      █   █      █                                                                                        ',
#     '       █             █          █          █                 █      █                                                █                                       ',
#     ' ██    ██     ██    ██    ██   ███    ██   ██     █      █   █ █    █    █████   ███    ██   ██    ██   ███    ██   ███   █ █   ██ █ █   █  █ █   █ █   ███  ',
#     '  ██   █ █   ██    █ █   ███    █    █ █   █ █    █      █   ██     █    █ █ █  ██ █  ██ █  █ █   █ █   █     ██     █    █ █   ██ █ █ █ █   █    █ █    ██  ',
#     ' █ █   █ █   ██    █ █   ██     █    █ █   █ █    █      █   █ █    █    █ █ █  ██ █  ██ █  █ █   █ █   █      ██    █    █ █   ███  █████   █    █ █   ██   ',
#     ' ███   ██     ██    ██    ██    █     ██   █ █    █      █   █ █    █    █ █ █  ██ █   ██   ██     ██   █     ██      █    ██    █    █ █   █ █    ██   ███  ',
#     '                                       █                █                                   █       █                                               █        ',
#     '                                     ██                █                                    █       █                                             ██         '
# ]
MOLE = [
    '⣿⣿⣿⣿⣿⣿⣿⠿⠛⠛⠛⠛⠿⢿⣿⣿⣿⣿⣿⣿',
    '⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿',
    '⣿⣿⣿⣿⠃⠀⣿⠀⠀⠀⣿⠀⠀⠀⠀⠈⣿⣿⣿⣿',
    '⣿⣿⣿⣿⠀⢠⠂⠉⠉⠁⢢⠀⠀⠀⠀⠀⢸⣿⣿⣿',
    '⣿⣿⣿⣿⠀⠀⠡⠠⠤⠴⠈⠀⠀⠀⠀⠀⢸⣿⣿⣿',
    '⣿⡿⢻⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⢿⣿⣿',
    '⡿⠐⠀⠜⠒⢄⣀⠀⠀⡀⠀⣀⠀⠀⡀⡠⢀⢌⠈⢿',
    '⣧⣮⡘⠄⠀⠐⠀⠡⡐⢊⠉⠐⠀⠤⠠⠂⠁⢃⠀⣬',
    '⣿⣿⣿⣶⣾⣿⣷⣤⣤⣶⣦⣭⣦⣶⣶⣤⣼⣿⣿⣿'
]
HIT = [
    '⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿',
    '⣿⣿⣿⢻⣿⣋⢿⢻⢻⣿⣿⡿⡿⢻⢿⢿⣷⣿⣿⣿',
    '⣿⣿⣿⢿⡏⠀⠀⠀⠡⡐⢊⠉⠀⠀⠀⠈⣿⣡⣿⣿',
    '⣿⣿⣿⣿⠀⠀⠒⠤⠀⠀⠤⠒⠀⠀⠀⠀⢸⣿⣿⣿',
    '⣿⣿⣿⣿⠀⠀⠀⢋⣉⣉⣉⡙⠀⠀⠀⠀⢸⣿⣿⣿',
    '⣿⡿⢻⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⢿⣿⣿',
    '⡿⠐⠀⠜⠒⢄⣀⠀⠀⡀⠀⣀⠀⠀⡀⡠⢀⢌⠈⢿',
    '⣧⣮⡘⠄⠀⠐⠀⠡⡐⢊⠉⠐⠀⠤⠠⠂⠁⢃⠀⣬',
    '⣿⣿⣿⣶⣾⣿⣷⣤⣤⣶⣦⣭⣦⣶⣶⣤⣼⣿⣿⣿'
]
HOLE = [
    '⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿',
    '⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿',
    '⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿',
    '⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿',
    '⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿',
    '⣿⡿⢻⢿⣿⢻⢿⣿⣿⣿⣿⣿⣿⣿⢿⢿⢻⢿⣿⣿',
    '⡿⠐⠀⠜⠒⢄⠉⡿⢻⢿⣿⢻⢿⠜⡀⡠⢀⢌⠈⢿',
    '⣧⣮⡘⠄⠀⠐⠀⠡⡐⢊⠉⠐⠀⠤⠠⠂⠁⢃⠀⣬',
    '⣿⣿⣿⣶⣾⣿⣷⣤⣤⣶⣦⣭⣦⣶⣶⣤⣼⣿⣿⣿'
]

if os.name == "nt":
    eraser = "cls"
elif os.name == "posix":
    eraser = "clear"
def hitmole_board():
    '''
    게임 시작을 알림
    HIT MOLE 글자판을 한 번 깜박이도록 한다.
    '''
    os.system(eraser)
    print(HIT_MOLE)
    time.sleep(1.5)
    os.system(eraser)
    print("\n"*20)
    time.sleep(0.5)

def tutorial_board():
    '''
    튜토리얼 시작을 알림
    TUTORIAL 글자판을 한 번 깜박이도록 한다.
    '''
    os.system(eraser)
    print(TUTORIAL)
    time.sleep(1.5)
    os.system(eraser)
    print("\n"*20)
    time.sleep(0.5)

def start_board():
    '''
    게임 시작 전 카운트 다운과 함께 시작을 알림
    3,2,1의 카운트 후 GAME START 글자판을 깜박이도록 한다.
    '''
    os.system(eraser)
    for i in range(3):
        print('\n'*8,end='')
        index = (3-i)*5
        for l in range(5):
            print(' '*26, NUMS[l][index:index+5])
        print("\n"*8)
        time.sleep(0.5)
        os.system(eraser)
        print("\n"*21)
        time.sleep(0.5)
        os.system(eraser)
    print(START)
    time.sleep(1.0)

def print_board(pop):
    '''
    현재 랜덤으로 튀어나온 두더지를 출력
    랜덤으로 숫자를 뽑아둔 pop_up을 받아 해당 인덱스만 두더지를 출력하고
    나머지는 구멍을 출력하도록 한다.

    pop = [0 0 0 0 0 0 0 0 0]
    랜덤으로 두더지가 들어갈 인덱스만 1인 상태로 변수 pop을 넘겨받을 것.
    pop에서의 인덱스와 매칭되는 키보드값은 다음과 같음.
    q w e   0 1 2
    a s d   3 4 5
    z x c   6 7 8
    '''
    os.system(eraser)
    for i in range(3):
        for r in range(len(HOLE)):
            for ii in range(3):
                index = 3*i + ii
                if pop[index] == 1:
                    print(MOLE[r], end='')
                else:
                    print(HOLE[r], end='')
            print()

def hit_board(pop):
    '''
    사용자가 두더지를 잡은 경우에
    랜덤으로 숫자를 뽑아둔 pop_up을 받아 해당 인덱스만 찌그러진 두더지를 출력하고
    나머지는 구멍을 출력하도록 한다.
    '''
    os.system(eraser)
    for i in range(3):
        for r in range(len(HOLE)):
            for ii in range(3):
                index = 3*i + ii
                if pop[index] == 1:
                    print(HIT[r], end='')
                else:
                    print(HOLE[r], end='')
            print()

def score_board(points):
    '''
    최종점수 출력
    SCORE 글자판과 함께 점수 속성을 화면에 출력한다.
    '''
    os.system(eraser)
    points = str(points)
    print('\n'*8)
    for i in range(5):
        print(SCORE[i],end='')
        for n in range(len(points)):
            index = int(points[n])*5
            print(NUMS[i][index:index+5],end='')
        print()
    print('\n'*10,end='')

def round_board(round):
    '''
    게임 라운드 출력
    사용자가 일정 점수를 넘겨 다음 라운드로 진입할 경우 라운드를 출력한다.
    '''
    os.system(eraser)
    print('\n'*8)
    for i in range(5):
        print(ROUND[i],end='')
        index = round*5
        print(NUMS[i][index:index+5],end='')
        print()
    print('\n'*10,end='')

def over_board():
    '''
    게임이 끝났음을 알림
    GAME OVER 글자판을 세 번 깜박이도록 한다.
    '''
    for _ in range(3):
        os.system(eraser)
        print(OVER)
        time.sleep(0.5)
        os.system(eraser)
        print("\n"*20)
        time.sleep(0.5)