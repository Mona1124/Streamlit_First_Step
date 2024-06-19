import streamlit as st

st.title('\'현대자동차\' 기업 소개 :bulb:')

st.subheader('현대자동차의 비전 : 휴머니티를 향한 진보')

st.markdown("**인류애, 사회와 국가에 대한 헌신과 기여**")
st.write("기술 발전은 인류에 바탕을 두고 있을 때 비로소 의미가 있습니다. 현대자동차는 로보틱스, AAM(Advanced Air Mobility) 등의 미래 모빌리티, 그리고 수소 에너지까지 확장된 사업 영역을 영위하며 휴머니티의 관점에서 더욱 크고 의미 있는 뜻을 실현하고, 인류를 위해 옳은 일을 하고자 합니다.")

st.write("**\"우리는 인류를 위해 옳은 일을 하고자 존재합니다.**")
st.write("**진정한 진보는 인류에 대한 깊은 공감을 바탕으로 이루어 집니다.**")
st.write("**인류애를 가질 때 우리는 하나가 되고 강해질 수 있습니다.**")
st.write("**우리는 인류가 더 나은 방향으로 나아가도록 기여하기 위해 존재합니다.\"**")
st.write("**-정주영, 현대자동차 선대 회장-**")

st.image("picture1.jpeg", caption="정주영, 현대자동차 선대 회장", use_column_width=True)

st.write("현대자동차는 모든 삶을 바꾸는 혁신은 반드시 사람에서 시작하고 사람에서 끝나야 한다고 믿습니다. 이는 한국 전쟁 이후 폐허가 된 국가를 일으키기 위해 도로를 닦고 다리를 놓으며 국토를 재건하고, 자동차를 통해 경제 성장의 기틀을 마련했던 고 정주영 선대 회장님으로부터 이어져온 현대자동차의 이념입니다. 언제나 국민의 더 나은 내일을 위해 인간 중심의 혁신을 이어온 현대자동차는 이제 전세계 모든 인류의 안전하고 자유로운 이동을 실현하기 위해 전진합니다.")

st.image("picture2.jpeg", use_column_width=True)

st.write("**현대자동차 오리지널 포니를 포함한 여러 차량이 고속도로를 달리고 있습니다.**")
st.write("**누군가가 현대자동차의 원동력이 무엇인지 묻는다면 바로 대답할 수 있습니다.**")
st.write("**그것은 더 나은 미래를 향한 열망입니다.**")
st.write("**-정주영, 현대자동차 선대 회장-**")

a = st.checkbox("다 읽고 체크해주세요 :bell:")
if a == True:
    st.write("Music :musical_note: : :red[thank u, next - Ariana Grande]")

