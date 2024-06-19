import streamlit as st

st.title('\'현대자동차\' 기업 목표')

st.subheader("현대자동차가 그리는 미래 :rainbow:")
st.write('현대자동차는 모든 사람들에게 제한 없는 이동의 자유를 제공하고자 자동차 제조업체의 틀을 넘어 스마트 모빌리티 솔루션 프로바이더(smart mobility solution provider)로 발전해 왔습니다.')

st.image("picture3.jpeg", caption = "미래를 향해 나아가는 현대자동차", use_column_width=True)

st.markdown("**현대자동차의 목표**")
st.write("다양한 방면으로 소개해왔던 자율주행, 로봇, AAM(Advanced Air Mobility)의 안전한 상용화는 물론이고, 2025년까지 소프트웨어, AI, 빅데이터 기반의 커넥티비티 기술 고도화를 통한 SDV(software-defined vehicle)로의 전환을 실현함으로써 고객에게 더욱 자유롭고, 안전하며, 평등한 주행경험을 제공하고자 합니다.")
st.write("또한, 폐배터리 재활용 사업을 통해 전기차 생산의 선순환 구조를 창출함과 동시에 폐기물로 청정 수소에너지를 생산함으로써 더욱 지속가능한 수소 생태계를 구축하여 보다 탄력성 있는 미래를 만들어 나아가려 합니다. 이처럼 현대자동차는 휴머니티를 향한 진보라는 당사의 비전하에 모든 사업영역을 영위하고 발전하고 있습니다.")

st.image("picture4.jpeg", caption="미래의 우리 생활", use_column_width=True)

a = st.checkbox("다 읽고 체크해주세요 :bell:")
if a == True:
    st.write("Music :musical_note: : :red[Cruel Summer - Taylor Swift]")