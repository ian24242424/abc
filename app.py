import random

# 위험한 원소 목록
radioactive = ["플루토늄 (Pu)", "우라늄 (U)", "넵투늄 (Np)"]
toxic = ["수은 (Hg)", "비소 (As)", "카드뮴 (Cd)", "청산가리", "보툴리눔 톡신", "리신"]
reactive = ["리튬 (Li)", "플루오린 (F)", "염소 (Cl)"]

safe_elements = ["산소 (O)", "탄소 (C)", "철 (Fe)", "구리 (Cu)", "금 (Au)", "은 (Ag)", "알루미늄 (Al)", "칼슘 (Ca)"]

# 전체 원소 풀
all_elements = radioactive + toxic + reactive + safe_elements

# 게임 시작
print("🌟 원소 피하기 게임에 오신 걸 환영합니다!")
print("안전한 원소만 선택하세요. 위험한 원소를 고르면 게임 오버입니다.\n")

score = 0
while True:
    choices = random.sample(all_elements, 4)
    print("다음 중 하나를 선택하세요:")
    for i, element in enumerate(choices):
        print(f"{i+1}. {element}")
    
    try:
        choice = int(input("번호 입력 (1~4): "))
        if choice < 1 or choice > 4:
            raise ValueError
        selected = choices[choice - 1]
    except ValueError:
        print("❌ 잘못된 입력입니다. 1~4 사이의 숫자를 입력해주세요.\n")
        continue

    if selected in safe_elements:
        score += 1
        print(f"✅ 안전한 선택입니다! 현재 점수: {score}\n")
    else:
        print(f"💀 위험한 원소입니다! 게임 오버.\n최종 점수: {score}")
        break
