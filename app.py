import streamlit as st

# 1. 마인드 컨트롤 처방을 결정하는 함수 (함수 & 조건문 활용)
def get_prescription(problem, stress_level):
    if problem == "학업 및 진로 스트레스":
        if stress_level <= 2:
            return "가벼운 긴장 상태네요! 10분간 눈을 감고 명상을 하거나 좋아하는 음악을 들어보세요."
        elif stress_level <= 4:
            return "머리를 식힐 시간이 필요해요. 스마트폰을 끄고 동네 한 바퀴 산책을 다녀오거나 맛있는 간식을 먹어보세요."
        else:
            return "번아웃 직전입니다! 오늘 하루는 책상에서 완전히 벗어나 푹 잠을 자거나 보고 싶었던 OTT 정주행을 추천합니다."

    elif problem == "친구 관계 문제":
        if stress_level <= 2:
            return "사소한 오해일 수 있어요. 혼자 차분히 생각할 시간을 가지며 명상을 해보세요."
        elif stress_level <= 4:
            return "기분 전환이 필요해요. 영화를 보며 다른 세상에 몰입하거나 맛있는 음식을 먹으며 스트레스를 날려보세요."
        else:
            return "마음이 많이 지쳤군요. 나를 온전히 이해해 주는 다른 편한 친구와 수다를 떨거나, 훌쩍 근교로 여행(드라이브)을 떠나보세요."

    elif problem == "가족 관계 문제":
        if stress_level <= 2:
            return "잠시 각자의 시간이 필요해요. 방에서 조용히 좋아하는 OTT 콘텐츠를 보며 기분을 환기해 보세요."
        elif stress_level <= 4:
            return "집 밖으로 잠시 나가보세요. 바깥 공기를 마시며 산책을 하거나 카페에서 맛있는 음료를 마시는 걸 추천합니다."
        else:
            return "감정이 많이 격해진 상태예요. 밖으로 나가 드라이브를 하거나 영화를 보며 감정을 가라앉힌 뒤, 일찍 잠자리에 들어보세요."

    elif problem == "이유 없는 무기력증 및 우울감":
        if stress_level <= 2:
            return "작은 성취감이 필요해요. 가볍게 방 정리를 하거나 5분만 스트레칭과 명상을 해보세요."
        elif stress_level <= 4:
            return "오감을 자극해 보세요! 평소 먹고 싶었던 아주 맛있는 음식을 먹거나, 친한 친구와 신나게 수다를 떨어보세요."
        else:
            return "에너지가 완전히 방전되었어요. 아무 생각 없이 푹 잠을 자거나, 주말을 이용해 낯선 곳으로 여행을 다녀오는 것을 추천합니다."

# --- 웹페이지 화면 구성 ---
st.title("💊 심리적 문제 마인드 컨트롤 간단 처방")
st.write("현재 겪고 있는 고민 키워드와 스트레스 지수를 선택하면 맞춤형 해결 방법을 처방해 드립니다.")

st.divider()

# 키워드 목록
keywords = [
    "학업 및 진로 스트레스",
    "친구 관계 문제",
    "가족 관계 문제",
    "이유 없는 무기력증 및 우울감"
]

st.subheader("1. 심리적 문제 키워드 선택")
selected_problem = st.selectbox("현재 가장 고민되는 문제를 선택하세요:", keywords)

st.subheader("2. 스트레스 지수 선택 (1 ~ 5)")
stress_level = st.slider("현재 느끼는 스트레스 정도를 조절하세요 (1: 매우 낮음 ~ 5: 매우 높음)", 1, 5, 3)

# 처방받기 버튼
if st.button("처방전 받기 🩺"):
    result = get_prescription(selected_problem, stress_level)
    
    st.success(f"**[{selected_problem} / 스트레스 지수 {stress_level}단계] 맞춤 처방**")
    st.info(f"💡 **추천 해결 방법:** {result}")
    
    # 반복문(for)을 활용한 추가 힐링 팁 출력
    st.write("---")
    st.write("✨ **함께 실천하면 좋은 기본 마인드 컨트롤 수칙**")
    tips = ["깊게 심호흡 3번 하기", "물 한 잔 천천히 마시기", "오늘 나에게 수고했다고 말해주기"]
    for i, tip in enumerate(tips, 1):
        st.write(f"{i}. {tip}")
