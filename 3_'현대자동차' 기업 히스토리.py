import streamlit as st

st.title('\'현대자동차\' 기업 히스토리 	:factory:')
st.caption('연대별 대표적인 차종만 넣었습니다.')

st.subheader('1960\'s')
st.markdown('코티나')
st.image('image1.jpeg', caption='코티나 (1968~1980)', use_column_width=True)

st.subheader('1970\'s')
st.markdown('포니, 포터')
st.image('image2.jpeg', caption='포니 (1974~1982)', use_column_width=True)

st.subheader('1980\'s')
st.markdown('포니엑셀, 쏘나타, 그랜저')
st.image('image3.jpeg', caption='그랜저 (1986~)', use_column_width=True)

st.subheader('1990\'s')
st.markdown('스쿠프, 엑센트, 아반떼, 티뷰론, 스타렉스')
st.image('image4.jpeg', caption='아반떼 (1995~)', use_column_width=True)

st.subheader('2000\'s')
st.markdown('베르나, 에쿠스, 싼타페, 투싼, i30, 제네시스')
st.image('image5.jpeg', caption='싼타페 (2000~)', use_column_width=True)

st.subheader('2010\'s')
st.markdown('i40, 벨로스터, 아이오닉, 코나, 넥쏘, 펠리세이드, 베뉴')
st.image('image6.jpeg', caption='넥쏘 (2018~))', use_column_width=True)

st.subheader('2020\'s')
st.markdown('스타리아, 캐스퍼')
st.image('image7.jpeg', caption='스타리아 (2021~)', use_column_width=True)

st.caption('출처: 현대자동차 홈페이지')

a = st.checkbox("다 읽고 체크해주세요 :bell:")
if a == True:
    st.write(":red[직진(JIKJIN) - TREASURE(트레저)]")