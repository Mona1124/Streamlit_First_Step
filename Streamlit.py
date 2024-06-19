# 작성한 후 '통합터미널 열기'해서 'conda activate streamlit-app'치고 'streamlit run 문서명'치면 작성한 거 반영되어 나타남.

import streamlit as st

st.title("취업하고 싶은 기업 소개 :sparkles:") # 제목
# emoji: http://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/ 

st.header("목차 :car:") # header

st.subheader("01장 \'현대자동차\' 기업 소개")
st.markdown("\'현대자동차\' 기업이 무슨 기업인지 소개합니다.")

st.subheader("02장 \'현대자동차\' 기업 목표")
st.markdown("\'현대자동차\' 기업 목표에 대해 소개합니다.")


st.subheader("03장 \'현대자동차\' 기업 히스토리")
st.markdown("연대별 \'현대자동차\' 기업의 자동차 모델을 소개합니다. ")