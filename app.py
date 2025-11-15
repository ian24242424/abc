import streamlit as st
import random

# 게임 상태 초기화
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'coins' not in st.session_state:
    st.session_state.coins = 0
if 'towers' not in st.session_state:
    st.session_state.towers = []
if 'enemies' not in st.session_state:
    st.session_state.enemies = []
if 'stage' not in st.session_state:
    st.session_state.stage = 1

# 타워 정보
tower_types = [
    {'name': 'Basic Tower', 'cost': 10, 'damage': 1},
    {'name': 'Sniper Tower', 'cost': 20, 'damage': 2},
    {'name': 'Cannon Tower', 'cost': 30, 'damage': 3},
    # 27개 타워 추가 가능
]

def spawn_enemy():
    if random.random() < 0.1:  # 10% 확률로 보스 적 등장
        enemy_type = 'Boss'
    else:
        enemy_type = random.choice(['Goblin', 'Orc', 'Troll'])
    st.session_state.enemies.append(enemy_type)

def place_tower(tower_index):
    tower = tower_types[tower_index]
    if st.session_state.coins >= tower['cost']:
        st.session_state.coins -= tower['cost']
        st.session_state.towers.append(tower)
        st.success(f"{tower['name']}가 배치되었습니다!")
    else:
        st.warning("코인이 부족합니다!")

def fight_enemy():
    if st.session_state.enemies:
        enemy = st.session_state.enemies[0]  # 첫 번째 적과 전투
        total_damage = sum(tower['damage'] for tower in st.session_state.towers)
        if enemy == 'Boss':
            if total_damage > 5:  # 보스 적의 체력 (가정)
                defeated_enemy = st.session_state.enemies.pop(0)
                st.session_state.score += 5  # 보스 처치 점수
                st.session_state.coins += 50  # 보스 처치 보상
                st.success(f"{defeated_enemy}을(를) 처치했습니다!")
            else:
                st.warning("보스 적이 너무 강합니다! 더욱 강력한 타워가 필요합니다.")
        else:
            defeated_enemy = st.session_state.enemies.pop(0)
            st.session_state.score += 1
            st.session_state.coins += 10  # 일반 적 처치 보상
            st.success(f"{defeated_enemy}을(를) 처치했습니다!")

def reset_game():
    st.session_state.score = 0
    st.session_state.coins = 0
    st.session_state.towers = []
    st.session_state.enemies = []
    st.session_state.stage = 1

def next_stage():
    st.session_state.stage += 1
    st.success(f"다음 스테이지로 넘어갑니다! 현재 스테이지: {st.session_state.stage}")

# UI 구성
st.title("고급 디펜스 게임")
st.write("적을 방어하고 점수를 얻으세요!")

# 점수, 코인, 스테이지 표시
st.write(f"점수: {st.session_state.score}")
st.write(f"코인: {st.session_state.coins}")
st.write(f"스테이지: {st.session_state.stage}")

# 적 스폰 버튼
if st.button("적 스폰하기"):
    spawn_enemy()
    st.write("적이 스폰되었습니다:", st.session_state.enemies)

# 타워 선택
tower_names = [tower['name'] for tower in tower_types]
tower_index = st.selectbox("구매할 타워 선택하기", range(len(tower_names)), format_func=lambda x: tower_names[x])

# 타워 배치 버튼
if st.button("타워 배치하기"):
    place_tower(tower_index)

# 적과 전투 버튼
if st.button("전투하기"):
    fight_enemy()

# 다음 스테이지 버튼
if st.button("다음 스테이지로 가기"):
    next_stage()

# 게임 리셋 버튼
if st.button("게임 리셋하기"):
    reset_game()
    st.write("게임이 리셋되었습니다.")

# 남은 적 표시
if st.session_state.enemies:
    st.write("남은 적:", st.session_state.enemies)
else:
    st.write("모든 적을 처치했습니다! 새로운 적을 스폰하세요.")
게임 실행 방법

터미널에서 다음 명령어로 게임을 실행하세요:
streamlit run advanced_defense_game.py
