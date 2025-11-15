import streamlit as st

def main():
    # 제목 설정
    st.title("쉽고 재미있는 과학의 세계")

    # 사이드바 메뉴
    menu = st.sidebar.selectbox("주제를 선택하세요", 
                                 ["홈", "물리학", "화학", "생물학", "지구과학", "퀴즈", "리소스"])

    if menu == "홈":
        st.subheader("과학이란 무엇인가요?")
        st.text("과학자는 다양한 현상에 대한 이해를 돕기 위해 이론을 발전시킵니다.")

    elif menu == "물리학":
        st.subheader("물리학")
        st.write("뉴턴의 운동 법칙은 물체의 운동을 설명하는 기본적인 법칙들입니다.")
        # 추가 내용 및 애니메이션은 여기에 포함

    elif menu == "화학":
        st.subheader("화학")
        st.write("원자 구조는 모든 물질의 기본이 되는 구조입니다.")
        # 추가 내용 및 애니메이션은 여기에 포함

    elif menu == "생물학":
        st.subheader("생물학")
        st.write("세포 이론은 모든 생물체가 세포로 이루어져 있다는 이론입니다.")
        # 추가 내용 및 애니메이션은 여기에 포함

    elif menu == "지구과학":
        st.subheader("지구과학")
        st.write("지구의 구조는 지각, 맨틀, 외핵, 내핵으로 이루어져 있습니다.")
        # 추가 내용 및 애니메이션은 여기에 포함

    elif menu == "퀴즈":
        st.subheader("퀴즈")
        st.write("아래의 질문에 답해보세요!")
        # 퀴즈 추가
        answer = st.radio("물리학의 기본 법칙은?", ("뉴턴의 운동 법칙", "상대성이론", "진화론"))
        if st.button("제출"):
            if answer == "뉴턴의 운동 법칙":
                st.success("정답입니다!")
            else:
                st.error("틀렸습니다, 다시 시도해보세요.")

    elif menu == "리소스":
        st.subheader("추천 도서 및 동영상")
        st.write("1. '물리학의 개념' - 도서")
        st.write("2. '화학의 기초' - 유튜브 동영상")
        # 추가 리소스 내용

if name == "main":
    main()
