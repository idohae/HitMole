# 🐒__HitMole__🙉
---
## 1. game rule
> ### tutorial
>  >* 두더지의 행동거지
>  >
>  >    tutorial에서는 랜덤으로 나타난 두더지가 사용자가 올바른 키를 입력할 때까지 사라지지 않는다.
>  >
>  >* 게임 시작
>  >    스페이스바를 누르면 튜토리얼을 멈추고 게임을 시작할 수 있다.

> ### main game
>  >* 두더지의 행동거지
>  >
>  >    <img src="https://github.com/idohae/HitMole/assets/152246147/be75f801-9c0a-4526-bda0-34844adc66f7" width="20%" height="20%" alt="round1_0 8"></img>
>  >    <img src="https://github.com/idohae/HitMole/assets/152246147/c7936090-0b0d-4a24-8c13-4ee9020d5bbe" width="20%" height="20%" alt="round2_0 6"></img>
>  >    <img src="https://github.com/idohae/HitMole/assets/152246147/485d173c-1805-4254-9f22-683875e1dfcf" width="20%" height="20%" alt="round3_0 4"></img>
>  >    <img src="https://github.com/idohae/HitMole/assets/152246147/c60f80da-2936-4c55-ba55-3b951220b244" width="20%" height="20%" alt="round4_0 2"></img>
>  >    
>  >    round는 총 4개로, 1라운드에선 두더지가 0.8초만에 들어가고, 각각 라운드 마다 머무는 시간이 0.2초씩 빨라진다.
>  >
>  >    두더지가 나오지 않은 구멍을 때리면 두더지가 바로 숨어버린다.
>  >
>  >    그외에 잘못된 키를 누르면 1라운드에선 0.3초 더 기다려주며, 그 뒤로는 0.05초씩 줄어든다.
>  >  
>  >* 점수
>  >
>  >    정상적으로 두더지를 잡으면 10점
>  >  
>  >    잘못된 키를 눌렀다 추가된 시간에 잡으면 5점
>  >* 라운드 진행
>  >    1,2 round에서는 각 라운드에서의 결과와 관계없이 만점의 80% 이상을 획득해야 다음 라운드로 넘어간다.
>  >
>  >        ex) 1라운드: 총점 80점 이상, 2라운드: 총점 160점 이상
>  >
>  >    4라운드는 히든 라운드로 3라운드에서 모두 다 맞추면 4라운드로 넘어갈 수 있다.

---
## 2. package
> ### What's in My Package
>  > HitMole에는 hitmole_pkg와 main.py로 구성되어있고, 패키지 안에는 __init__.py, hitmole_boards.py, 
>  > hitmole2.py로 구성되어있다.
>  > hitmole_boards는 보드판을 띄우는 역할로, 숫자나 문구를 보여줄 때 쓰고, 
>  > hitmole2는 게임을 진행하는 역할이다.

> ### how to start
>  >* 사전 준비
>  > 
>  >       pip install module_name
>  >
>  >    pynput, numpy, os-sys 등의 외부 모듈이 필요하기에 없을 시 명령창에 위 코드를 입력하여 설치한다.
>  >
>  >* 게임 실행
>  >
>  >       python3 main.py
>  >  
>  >    위 명령어를 HitMole 디렉토리 밑에서 실행하면 게임이 시작된다.
>  >
>  >    입력창이 뜨면 6자 이내의 영어 소문자로 닉네임을 입력하면 시작된다.
