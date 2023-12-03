# 🐒__HitMole__🙉

## **⋆ . 🎁˚🎄 ✦Game Developers.. 🧸⊹ ･ﾟ✧**
> 이해정(Haejeong, Lee) <pouwuoq0815@pukyong.ac.kr>
> 
> 백서연(Seoyeon, Baek) <callmeseoyeon@naver.com>
> 
> 주효빈(Hyobin, Ju) <zns12201220@gmail.com>

---
## 1. game rule
> ### tutorial
>  >* 두더지의 행동거지   
>  >    tutorial에서는 랜덤으로 나타난 두더지가 플레이어가 올바른 키를 입력할 때까지 사라지지 않는다.
>  >
>  >* 게임 시작   
>  >    스페이스바를 누르면 튜토리얼을 멈추고 게임을 시작할 수 있다.

> ### main game
>  >* 두더지의 행동거지   
>  >    <img src="https://github.com/idohae/HitMole/assets/152246147/16bc9880-c75c-4180-ba40-d7b3a92b24b4" width="20%" height="20%" alt="round1"></img>
>  >    <img src="https://github.com/idohae/HitMole/assets/152246147/3419f68e-5666-4f60-876a-522565c22bcb" width="20%" height="20%" alt="round2"></img>
>  >    <img src="https://github.com/idohae/HitMole/assets/152246147/b0ef3959-e0d1-4e79-a066-65a9439f672c" width="20%" height="20%" alt="round3"></img>
>  >    <img src="https://github.com/idohae/HitMole/assets/152246147/b8b1c1ce-f1e1-45fe-890d-7cffb34c8362" width="20%" height="20%" alt="round4"></img>
>  >    
>  >    round는 총 4개로, 1라운드에선 두더지가 0.8초만에 들어가고, 각각 라운드 마다 머무는 시간이 0.2초씩 빨라진다.   
>  >    두더지가 나오지 않은 구멍을 때리면 두더지가 바로 숨어버린다.   
>  >    그외에 잘못된 키를 누르면 1라운드에선 0.3초 더 기다려주며, 그 뒤로는 0.05초씩 줄어든다.
>  >  
>  >* 점수   
>  >    정상적으로 두더지를 잡으면 10점   
>  >    잘못된 키를 눌렀다 추가된 시간에 잡으면 5점   
>  >    각 라운드가 끝날 때마다 총점을 출력해준다.
>  >  
>  >* 라운드 진행   
>  >    1,2 round에서는 각 라운드에서의 결과와 관계없이 만점의 80% 이상을 획득해야 다음 라운드로 넘어간다.   
>  >    *`ex) 1라운드: 총점 80점 이상, 2라운드: 총점 160점 이상`*   
>  >    4라운드는 히든 라운드로 3라운드에서 모두 다 맞추면 4라운드로 넘어갈 수 있다.   
>  >    조건을 넘기지 못하고 게임이 종료되면 순위가 나온다.

---
## 2. package
> ### what's in my HitMole
>  > <img src="https://github.com/idohae/HitMole/assets/152246147/cb526c88-7f14-4abe-bd7b-18671b82b468" width="40%" height="40%" alt="image"></img>
>  >
>  > `hitmole_pkg`
>  >  > [`hitmole_boards.py`](#hitmole_boards)   
>  >  >    보드판을 띄우는 역할로, 두더지나 숫자, 문구를 아스키 아트로 출력하는 메소드들로 구성된 모듈이다.
>  >  >
>  >  > [`hitmole2.py`](#hitmole2)   
>  >  >    hitmole_boards 모듈을 이용하여 튜토리얼부터 끝까지 전반적인 진행 코드가 작성된 파일이다.
>  >
>  > [`main.py`](#main)   
>  >    게임의 시작과 함께 플레이어로부터 닉네임을 입력받고, hitmole2.py 의 게임 진행 메소드 [`play()`](#play) 를 호출한다.

> ### how to start
>  >* 사전 준비
>  > 
>  >       pip install module_name
>  >
>  >    `pynput, numpy, os-sys` 등의 외부 모듈이 필요하기에 없을 시 명령창에 위 코드를 입력하여 설치한다.
>  >
>  >* 게임 실행
>  >
>  >       python3 main.py
>  >  
>  >    위 명령어를 HitMole 디렉토리 밑에서 입력하면 게임이 실행된다.   
>  >    입력창이 뜨면 6자 이내의 영어 소문자로 닉네임을 입력하면 시작된다.

---
## 3. codes
`tutorial` → `1라운드` → `점수출력` → `판별` → `2라운드` → `점수` → `3라운드` → `점수` → `랭킹출력`
> ## `hitmole_boards`[▲](#whats-in-my-hitmole)
> [`hitmole_board`](#hitmole_board)
> [`tutorial_board`](#tutorial_board)
> [`start_board`](#start_board)
> [`print_board`](#print_boardpop)
> [`hit_board`](#hit_boardpop)  
> ```python
> if os.name == "nt":
>     eraser = "cls"
> elif os.name == "posix":
>     eraser = "clear"
> ```
> 게임을 실행하는 os 가 Mac 또는 Linux 일 경우 아래에서 쓰이는 os.system() 함수에 넘겨주는 명령어를 `clear`로, Window 일 경우 `cls`로 한다.   
> 보드판을 반복해서 출력하기 위해 터미널 화면을 초기화 하는 데 사용된다.
> 
>  > ### `hitmole_board()`[▲](#hitmole_boards)
>  > 게임 시작 화면 출력 메소드
>  > ```python
>  > hitmole_board():
>  >     os.system(eraser)
>  >     print(HIT_MOLE)
>  >     time.sleep(1.5)
>  >     os.system(eraser)
>  >     print("\n"*20)
>  >     time.sleep(0.5)
>  > ```
>  > 터미널 코드 전적 지운 후 저장된 문자열인 게임명 출력, 읽을 수 있게 1.5초 유지   
>  > 다음 화면으로 넘어가기 전 공백을 위한 print를 0.5초 유지
>
>  > ### `tutorial_board()`[▲](#hitmole_boards)
>  > 튜토리얼 시작 화면 출력 메소드
>  > ```python
>  > tutorial_board(): 
>  >     os.system(eraser)
>  >     print(TUTORIAL)
>  >     ...
>  > ```
>  > 프린트 하는 문자만 다를 뿐 나머지 코드는 [`hitmole_board()`](#hitmole_board) 와 동일
>
>  > ### `start_board()`[▲](#hitmole_boards)
>  > 본 게임 시작 화면 출력 메소드
>  > ```python
>  > start_board():
>  >     os.system(eraser)
>  >     for i in range(3):
>  >         print('\n'*8,end='')
>  >         index = (3-i)*5
>  >         for l in range(5):
>  >             print(' '*26, NUMS[l][index:index+5])
>  >         print("\n"*8)
>  >         time.sleep(0.5)
>  >         os.system(eraser)
>  >         print("\n"*21)
>  >         time.sleep(0.5)
>  >         os.system(eraser)
>  >     print(START)
>  >     time.sleep(1.0)
>  > ```
>  > 3,2,1 카운트 다운을 위한 반복 루프 제작, 카운트 값에 따라 숫자를 가져오기 위한 index 계산   
>  > → `NUMS` 리스트에서 해당 인덱스 범위의 숫자를 출력하기 위해 반복 루프(5번인 이유는 리스트에서 숫자 하나가 5열로 구성)   
>  > → 숫자 출력 후 화면 정리를 위한 엔터 출력   
> 
>  > ### `print_board(pop)`[▲](#hitmole_boards)
>  > 랜덤 두더지 아스키 아트 출력 메소드
>  > ```python
>  > pop = [0 0 0 0 0 1 0 0 0]
>  > 
>  > q w e   0 1 2  
>  > a s d   3 4 5  
>  > z x c   6 7 8
>  > ```
>  > 랜덤으로 두더지가 들어갈 인덱스만 1인 상태로 변수 pop을 넘겨받을 것.   
>  > pop에서의 인덱스와 매칭되는 키보드값은 위와 같음. 위에서의 두더지 인덱스는 `5`, 키보드 위치는 `d`에 해당
>  > ```python
>  > def print_board(pop):
>  >     os.system("clear")
>  >     for i in range(3):
>  >         for r in range(len(HOLE)):
>  >             for ii in range(3):
>  >                 index = 3*i + ii
>  >                 if pop[index] == 1:
>  >                     print(MOLE[r], end='')
>  >                 else:
>  >                     print(HOLE[r], end='')
>  >             print()
>  > ```
>  > 세로로 3개의 행을 나타내기 위한 반복 루프 → HOLE의 길이만큼 반복하는 루프 → 가로로 3개의 열을 나타내는 루프  
>  > 
>  > 현재의 행과 열을 기반으로 pop 리스트에서 가져올 인덱스를 계산  
>  > → 인덱스가 1인 경우 (즉, 해당 위치에 두더지가 나타난 경우) : __두더지__ 출력  
>  > → 인덱스가 0인 경우 (즉, 해당 위치에 두더지가 나타나지 않은 경우) : __구멍__ 출력  
>
>  > ### `hit_board(pop)`[▲](#hitmole_boards)
>  > 맞아서 찌그러진 두더지 아스키 아트 출력 메소드
>  > ```python
>  > def hit_board(pop):  
>  >     ...(위의 [print_board()](#print_boardpop) 함수와 동일)
>  >                 if pop[index] == 1: 
>  >                     print(HIT[r], end='') 
>  >                 else:
>  >                     print(HOLE[r], end='') 
>  >         print()
>  > ```
>  > 생략된 부분은 위의 [`print_board()`](#print_boardpop) 함수와 동일
>  >
>  > 사용자가 두더지를 잡은 경우에  
>  > 랜덤으로 숫자를 뽑아둔 pop_up을 받아 해당 인덱스만 찌그러진 두더지를 출력하고  
>  > 나머지는 구멍을 출력하도록 한다.
>  > 
> ## `hitmole2`
>
> ## `main`
