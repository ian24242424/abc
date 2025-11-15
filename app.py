import streamlit as st
import random

# 게임 상태 초기화
if 'coins' not in st.session_state:
    st.session_state.coins = 50
if 'towers' not in st.session_state:
    st.session_state.towers = []
if 'enemies' not in st.session_state:
    st.session_state.enemies = []

# 타워 종류
tower_types = [
    {'name': 'Basic Tower', 'cost': 10, 'damage': 1},
    {'name': 'Sniper Tower', 'cost': 20, 'damage': 2},
]

def spawn_enemy():
    enemy_type = random.choice(['Goblin', 'Orc'])
    st.session_state.enemies.append(enemy_type)

def place_tower(tower_index):
    tower = tower_types[tower_index]
    if st.session_state.coins >= tower['cost']:
        st.session_state.coins -= tower['cost']
        st.session_state.towers.append(tower)
        st.success(f"{tower['name']}이 배치되었습니다!")
    else:
        st.warning("코인이 부족합니다!")

def fight_enemy():
    if st.session_state.enemies:
        enemy = st.session_state.enemies.pop(0)
        total_damage = sum(tower['damage'] for tower in st.session_state.towers)
        if total_damage > 0:
            st.success(f"{enemy}을(를) 처치했습니다!")
        else:
            st.warning(f"{enemy}이(가) 살아남았습니다!")

# UI 구성
st.title("간단한 디펜스 게임")
st.write("적을 방어하고 점수를 얻으세요!")

# 점수, 코인 표시
st.write(f"코인: {st.session_state.coins}")

# 적 스폰 버튼
if st.button("적 스폰하기"):
    spawn_enemy()
    st.write("스폰된 적:", st.session_state.enemies)

# 타워 선택
tower_names = [tower['name'] for tower in tower_types]
tower_index = st.selectbox("구매할 타워 선택하기", range(len(tower_names)), format_func=lambda x: tower_names[x])

# 타워 배치 버튼
if st.button("타워 배치하기"):
    place_tower(tower_index)

# 적과 전투 버튼
if st.button("전투하기"):
    fight_enemy()

# 남은 적 표시
if st.session_state.enemies:
    st.write("남은 적:", st.session_state.enemies)
else:
    st.write("모든 적을 처치했습니다! 새로운 적을 스폰하세요.")
